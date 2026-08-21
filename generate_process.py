
import os
import time
import subprocess
import imageio_ffmpeg


from vercel.blob import BlobClient
from text_to_audio import text_to_speech_file


def text_to_audio(folder):
    print("TTA-", folder)

    with open(f"/tmp/user_uploads/{folder}/desc.text", "r", encoding="cp1252") as f:
        text = f.read()

    print(text, folder)

    text_to_speech_file(text, folder)


def create_reel(folder):
    folder_path = os.path.join("/tmp/user_uploads", folder)
    input_file = os.path.join(folder_path, "input.txt")
    audio_file = os.path.join(folder_path, "audio.mp3")
    output_file = os.path.join("/tmp", "reels", f"{folder}.mp4")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    print("FFmpeg executable:", ffmpeg_path)
    
    # blob_client = BlobClient()
    blob_client = BlobClient(token=os.getenv("Private_BLOB_READ_WRITE_TOKEN"))

    command = [
        ffmpeg_path,
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", input_file,
        "-i", audio_file,
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=decrease,"
        "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        "-r", "30",
        "-pix_fmt", "yuv420p",
        output_file
    ]

    print("Running FFmpeg...")
    print("Input:", input_file)
    print("Audio:", audio_file)
    print("Output:", output_file)
    
    # IMPORTANT: no shell=True
    subprocess.run(command, check=True)

    uploaded = blob_client.upload_file(
        output_file,
        f"reels/{folder}.mp4",
        access="private",
        content_type="video/mp4"
    )

    print("Blob URL:", uploaded.url)
    print("CR-", folder)

    return uploaded.url

if __name__ == "__main__":
    while True:
        print("processing queue...")

        # with open("/tmp/done.txt", "r", encoding="utf-8") as f:
        #     done_folders = f.readlines()
        
        done_file = "/tmp/done.txt"

        if os.path.exists(done_file):
            with open(done_file, "r", encoding="utf-8") as f:
                done_folders = f.readlines()
        else:
            done_folders = []
            
        
        

        done_folders = [f.strip() for f in done_folders]

        folders = os.listdir("/tmp/user_uploads")

        for folder in folders:
            if folder not in done_folders:

                text_to_audio(folder)

                create_reel(folder)

                with open("/tmp/done.txt", "a", encoding="utf-8") as f:
                    f.write(folder + "\n")

        time.sleep(4)    
    