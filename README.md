# 🎥 AI-Powered Video Caption Generator

An intelligent tool that automatically generates captions/subtitles for videos using OpenAI's Whisper model. Built with Streamlit for a smooth and interactive user interface.

---

## 🚀 Features

- ✅ Upload and process any video file
- ✅ Generates accurate captions using OpenAI Whisper ASR
- ✅ Downloads captions in `.srt` format
- ✅ Extracts and processes audio using `ffmpeg` & `moviepy`
- ✅ Clean and fast Streamlit interface

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – Web Interface
- [OpenAI Whisper](https://github.com/openai/whisper) – Speech-to-Text Model
- [ffmpeg](https://ffmpeg.org/) – Audio/Video Processing
- [moviepy](https://zulko.github.io/moviepy/) – Video Editing
- [srt](https://pypi.org/project/srt/) – Subtitle Formatting

---

## 🖥️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/ai-video-caption-generator.git
cd ai-video-caption-generator
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


3. **Install the dependencies**
```bash
pip install -r requirements.txt
```

4. **Make sure ffmpeg is installed and added to your PATH**
You can download it from: https://ffmpeg.org/download.html

## ▶️ Run the App
To start the Streamlit application, run:
uv run streamlit run app.py

## 📌 Notes
- Make sure your system supports ffmpeg properly
- For large files, processing time may vary depending on system resources
- Whisper supports multilingual transcription!

## 🙌 Acknowledgements
- OpenAI -> for the Whisper model
- Streamlit -> for the intuitive UI framework
- Python -> community for the awesome libraries

## 🌐 Connect with Me
- LinkedIn: https://www.linkedin.com/in/jugal-kishore-61b48b246/
- Portfolio: https://jugal-portfolio-ten.vercel.app/