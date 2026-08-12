from flask import Flask, render_template, request
import uuid

import os

from generate_process import text_to_audio, create_reel
from werkzeug.utils import secure_filename
from vercel.headers import set_headers

# UPLOAD_FOLDER = "user_uploads"
UPLOAD_FOLDER = "/tmp/user_uploads"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"]) 
def create():
    set_headers(request.headers)
    myid=uuid.uuid1()
    video_url = None
    if request.method =="POST":
        print(request.files.keys())
        rec_id=request.form.get("uuid")
        desc = request.form.get("text")
        input_files=[]
        for key,value in request.files.items():
            print(key, value)
            #uploading the files 
            
            file=request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
                    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, filename))
                input_files.append(filename)
                # input_files.append(file.filename)
             # Capture the discription and save it to a file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.text"), "w") as f:
                f.write(desc)
        # for fl in input_files:
        #      with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
        #          f.write(f"file '{app.config['UPLOAD_FOLDER']}/{rec_id}/{fl}'\nduration 1\n")  
        
        input_txt_path = os.path.join(
    app.config['UPLOAD_FOLDER'],
    rec_id,
    "input.txt"
)

        with open(input_txt_path, "w", encoding="utf-8") as f:
            for fl in input_files:
                f.write(f"file '{fl}'\n")
                f.write("duration 1\n")
                
                
        text_to_audio(rec_id)
        create_reel(rec_id)        
            
           
                 
    return render_template("create.html", myid=myid, video_url=video_url)


@app.route("/gallery")
def gallery():
    reels=os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

if __name__ == "__main__":
    app.run(debug=True)