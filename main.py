from flask import Flask, render_template, request, redirect, url_for, jsonify
import uuid
from werkzeug.utils import secure_filename
import os
import shutil
import threading
from generate_process import process_folder

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("static/reels", exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text", "")
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(folder_path, exist_ok=True)

        input_files = []
        for key in request.files:
            file = request.files[key]
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(folder_path, filename))
                input_files.append(filename)

        # Save description script
        with open(os.path.join(folder_path, "desc.txt"), "w", encoding="utf-8") as f:
            f.write(desc)

        # Save input.txt for ffmpeg concatenation
        with open(os.path.join(folder_path, "input.txt"), "w", encoding="utf-8") as f:
            for fl in input_files:
                f.write(f"file '{fl}'\nduration 1\n")

        # Run the reel generation in a background thread to prevent Gunicorn timeout
        thread = threading.Thread(target=process_folder, args=(rec_id,), daemon=True)
        thread.start()

        return redirect(url_for("gallery"))

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    os.makedirs("static/reels", exist_ok=True)
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

@app.route("/delete/<filename>", methods=["POST"])
def delete_reel(filename):
    safe_filename = secure_filename(os.path.basename(filename))
    reel_path = os.path.join("static", "reels", safe_filename)
    
    if os.path.exists(reel_path):
        try:
            os.remove(reel_path)
        except Exception as e:
            print(f"Error deleting reel file {reel_path}: {e}")
            
    # Clean up corresponding user_uploads folder if present
    rec_id = os.path.splitext(safe_filename)[0]
    upload_folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
    if os.path.exists(upload_folder_path):
        try:
            shutil.rmtree(upload_folder_path, ignore_errors=True)
        except Exception as e:
            print(f"Error deleting upload folder {upload_folder_path}: {e}")

    # Remove rec_id entry from done.txt if present
    if os.path.exists("done.txt"):
        try:
            with open("done.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open("done.txt", "w", encoding="utf-8") as f:
                for line in lines:
                    if line.strip() != rec_id:
                        f.write(line)
        except Exception as e:
            print(f"Error updating done.txt: {e}")

    if request.is_json or request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"success": True, "message": "Reel deleted successfully"})

    return redirect(url_for("gallery"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)