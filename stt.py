import speech_recognition as sr
import streamlit as st

# Streamlit Page Config
st.set_page_config(
    page_title="Audio File Speech-to-Text", page_icon="🎙️", layout="centered"
)


# Function to handle audio file transcription
def transcribe_audio_file(audio_file):
  r = sr.Recognizer()

  # Save the uploaded file temporarily so SpeechRecognition can read it
  temp_path = "temp_audio.wav"
  with open(temp_path, "wb") as f:
    f.write(audio_file.getbuffer())

  # Load and process the audio file using your logic
  with sr.AudioFile(temp_path) as source:
    audio_data = r.record(source)
    try:
      text = r.recognize_google(audio_data)
      return f"Transcription: {text}"
    except sr.UnknownValueError:
      return "Error: Google Speech Recognition could not understand the audio."
    except sr.RequestError as e:
      return f"Error connecting to service; {e}"
    except Exception as e:
      return f"Error: {e}"


# --- Streamlit UI Layout ---
st.title("📂 Audio File Speech-to-Text")
st.write(
    "Upload a **.wav** audio file to transcribe it using your Speech-to-Text"
    " code!"
)

# File uploader widget (strictly .wav to match your working code logic)
uploaded_file = st.file_uploader(
    "Choose a WAV audio file...", type=["wav"]
)

if uploaded_file is not None:
  st.audio(uploaded_file, format="audio/wav")

  if st.button("🚀 Transcribe Audio"):
    with st.spinner("Transcribing..."):
      result = transcribe_audio_file(uploaded_file)
      st.success("Done!")
      st.write(result)