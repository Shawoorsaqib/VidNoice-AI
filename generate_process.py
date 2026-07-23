import os 
from text_to_audio import text_to_speech_file
import time
import subprocess


def text_to_audio(folder):
    print("TTA - ", folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    text_to_speech_file(text, folder)

def create_reel(folder):
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -preset ultrafast -threads 2 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True, check=True)
    
    print("CR - ", folder)

def process_folder(folder):
    """Callable function to process audio generation and video creation for a folder."""
    try:
        text_to_audio(folder)
        create_reel(folder)
        os.makedirs(os.path.dirname("done.txt") or ".", exist_ok=True)
        with open("done.txt", "a") as f:
            f.write(folder + "\n")
        print(f"Successfully processed folder: {folder}")
    except Exception as e:
        print(f"Error processing folder {folder}: {e}")

if __name__ == "__main__":
    while True:
        print("Processing queue...")
        done_folders = []
        if os.path.exists("done.txt"):
            with open("done.txt", "r") as f:
                done_folders = [line.strip() for line in f.readlines()]

        if os.path.exists("user_uploads"):
            folders = os.listdir("user_uploads") 
            for folder in folders:
                if folder not in done_folders:
                    process_folder(folder)
        time.sleep(4)