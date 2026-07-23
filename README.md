# 🎙️ VidNoice-AI

> Transform your images and videos into narrated content using AI-powered voice generation.

VidNoice-AI is an AI SaaS web application built with **Flask** and **ElevenLabs** that converts user-provided text into natural-sounding speech and automatically merges it with uploaded images or videos to generate a final narrated video.

---

## ✨ Features

- 📷 Upload Images (`.png`, `.jpg`, `.jpeg`)
- 🎥 Upload Videos (`.mp4`)
- 📝 Enter custom narration/script
- 🤖 AI-powered Text-to-Speech using ElevenLabs
- 🔊 Generates high-quality MP3 narration
- 🎬 Automatically merges narration with uploaded media
- 📱 Outputs a ready-to-share video
- 🖥️ Clean and responsive Flask web interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| HTML/CSS | Frontend |
| ElevenLabs API | AI Voice Generation |
| FFmpeg | Video & Audio Processing |
| Werkzeug | Secure File Uploads |

---

## 📂 Project Structure

```
VidNoice-AI/
│
├── static/
│   ├── css/
│   ├── reels/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   └── gallery.html
│
├── user_uploads/
│
├── main.py
├── generate_process.py
├── text_to_audio.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shawoorsaqib/VidNoice-AI.git
cd VidNoice-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

Download and install FFmpeg:

https://ffmpeg.org/download.html

Ensure FFmpeg is added to your system PATH.

---

## 🔑 Configure API Key

Create a `config.py` file:

```python
ELEVENLABS_API_KEY = "YOUR_API_KEY"
```

Or preferably use environment variables.

---

## ▶️ Running the Project

Start the Flask application:

```bash
python main.py
```

In another terminal, start the processing service:

```bash
python generate_process.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 🚀 How It Works

```
Upload Image / Video
          │
          ▼
Enter Narration Text
          │
          ▼
ElevenLabs AI
(Text → Speech)
          │
          ▼
Generate MP3 Audio
          │
          ▼
FFmpeg
(Audio + Media)
          │
          ▼
Final Narrated Video
```

---

## 📸 Screenshots

### Home Page

_Add screenshot here_

### Create Page

_Add screenshot here_

### Gallery

_Add screenshot here_

---

## 🎯 Future Improvements

- Multiple AI Voices
- Voice Speed & Pitch Controls
- Subtitle Generation
- Drag & Drop Upload
- User Authentication
- Download History
- Background Music
- Multiple Languages
- Cloud Storage
- Video Progress Indicator
- REST API
- Docker Support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shawoor Saqib**

- GitHub: https://github.com/Shawoorsaqib

---

⭐ If you found this project useful, consider giving it a star!
