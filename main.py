from flask import Flask, render_template, request, Response
import uuid
import json
import os

from dotenv import load_dotenv
load_dotenv(".env.local")

from generate_process import text_to_audio, create_reel
from werkzeug.utils import secure_filename
from vercel.headers import set_headers
from vercel.blob import BlobClient


UPLOAD_FOLDER = "/tmp/user_uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    set_headers(request.headers)

    myid = uuid.uuid1()
    video_url = None
    reel_created = False

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text") or ""
        input_files = []

        folder_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            rec_id
        )

        os.makedirs(folder_path, exist_ok=True)

        blob_files = request.form.get("blob_files")

        if not blob_files:
            return "No uploaded images found", 400

        blob_files = json.loads(blob_files)

        blob_client = BlobClient(
            token=os.getenv("Private_BLOB_READ_WRITE_TOKEN")
        )

        for blob_file in blob_files:
            pathname = blob_file.get("pathname")

            if not pathname:
                continue

            result = blob_client.get(
                pathname,
                access="private"
            )

            filename = secure_filename(
                os.path.basename(pathname)
            )

            file_path = os.path.join(
                folder_path,
                filename
            )

            with open(file_path, "wb") as f:
                f.write(result.content)

            input_files.append(filename)

        # Save description
        with open(
            os.path.join(folder_path, "desc.text"),
            "w",
            encoding="utf-8"
        ) as f:
            f.write(desc)

        # Create FFmpeg input file
        input_txt_path = os.path.join(
            folder_path,
            "input.txt"
        )

        with open(
            input_txt_path,
            "w",
            encoding="utf-8"
        ) as f:
            for filename in input_files:
                f.write(f"file '{filename}'\n")
                f.write("duration 1\n")

        text_to_audio(rec_id)
        create_reel(rec_id)

        reel_created = True

    return render_template(
        "create.html",
        myid=myid,
        video_url=video_url,
        reel_created=reel_created
    )


@app.route("/reel/<path:pathname>")
def serve_reel(pathname):
    blob_client = BlobClient(
        token=os.getenv("Private_BLOB_READ_WRITE_TOKEN")
    )

    result = blob_client.get(
        pathname,
        access="private"
    )

    if result.status_code != 200:
        return "Reel not found", 404

    return Response(
        result.content,
        status=200,
        content_type=result.content_type or "video/mp4",
        headers={
            "Content-Disposition": "inline",
            "Accept-Ranges": "bytes",
        }
    )


@app.route("/gallery")
def gallery():
    blob_client = BlobClient(
        token=os.getenv("Private_BLOB_READ_WRITE_TOKEN")
    )

    result = blob_client.list_objects()

    reels = []

    for blob in result.blobs:
        reels.append({
            "url": f"/reel/{blob.pathname}",
            "pathname": blob.pathname
        })

    return render_template(
        "gallery.html",
        reels=reels
    )


if __name__ == "__main__":
    app.run(debug=True)