import os
import subprocess
import streamlit as st
from datetime import timedelta
import whisper
import srt
from moviepy import VideoFileClip

# --- step 1: audio extraction ---
def extract_audio(video_path, output_audio_path):
  try:
    video = VideoFileClip(video_path)
    if video.audio:
      video.audio.write_audiofile(output_audio_path)
      return True
    else:
      st.error(f"[!] No audio track found in the video.")
      return False
  except Exception as e:
      st.error(f"error extracting audio: {e}")
      return False

# --- step 2: transcription using whisper ---
def transcribe_audio(audio_path):
    try:
      model = whisper.load_model("base")
      result = model.transcribe(audio_path)
      return result
    except Exception as e:
      st.error(f"error transcribing audio: {e}")
      return None


# --- step 3: Generaatae SRT File ---
def generate_srt(transcription_result):
  try:
    subtitles = []
    for i, seg in enumerate(transcription_result.get('segments',[])):
      subtitle = srt.Subtitle(
        index=i+1,
        start=timedelta(seconds=seg['start']),
        end=timedelta(seconds=seg['end']),
        content=seg['text'].strip()
      )
      subtitles.append(subtitle)
    return srt.compose(subtitles)
  except Exception as e:
    st.error(f"Error generating SRT: {e}")
    return None
  
# --- step 4: Burn subtitles FFmpeg ---
def burn_subtitle(video_path, srt_relative_path, output_path, ffmpeg_path):
  # get absolute path for video and output
  video_full = os.path.abspath(video_path)
  output_full = os.path.abspath(output_path)

  # use the relative path for subtitles exactly as it worked in your manual command.
  # Make sure the working directory is the project directory.

  command = f'"{ffmpeg_path}" -i "{video_full}" -vf "subtitles={srt_relative_path}" "{output_full}"'

  print("Running command:")
  print(command)

  try:
    subprocess.run(command, shell=True, check=True)
    return True
  except subprocess.CalledProcessError as e:
    st.error(f"Error burning subtitles: {e}")
    return False
  

# --- Main Streamlit App ---
def main():
    st.title("AI-Powered Video Caption Generator")
    st.write("Upload a video to generate captions and burn them into the video.")
    
    # File uploader for video
    Upload_video = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    
    if Upload_video:
        video_path = f"videos/Upload_video.mp4"
        os.makedirs('videos', exist_ok=True)

        with open(video_path, "wb") as f:
            f.write(Upload_video.getbuffer())
        st.video(video_path)

        if st.button("Generate caption"):
            # Step 1: Extract audio
            os.makedirs('audio', exist_ok=True)
            audio_path = 'audio/uploaded_audio.wav'
            st.write("Extracting audio...")
            if not extract_audio(video_path, audio_path):
                return

            # Step 2: Transcribe audio
            st.write("Transcribing audio...")
            transcription_result = transcribe_audio(audio_path)
            if not transcription_result:
                return
            st.write("Transcription Result:")
            st.write(transcription_result.get('text', ""))

            # Step 3: Generate SRT File
            srt_content = generate_srt(transcription_result)
            os.makedirs("captions", exist_ok=True)
            srt_path = 'captions/uploaded_output.srt'
            with open(srt_path, "w", encoding='utf-8') as f:
                f.write(srt_content)
            st.success("SRT file generated.")

            # Step 4: Burn subtitles onto video
            ffmpeg_path = r"C:\\ffmpeg\\bin\\ffmpeg.exe"
            st.write("Burning subtitles onto video...")
            if burn_subtitle(video_path, srt_path, 'videos/uploaded_output_video.mp4', ffmpeg_path):
                st.success("Video with burned-in captions generted!")
                st.video("videos/uploaded_output_video.mp4")

if __name__ == "__main__":
    main()