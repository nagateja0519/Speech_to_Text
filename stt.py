import streamlit as st
import sounddevice as sd
import speech_recognition as sr
import soundfile as sf
import tempfile
import os

def transcribe_audio():
    samplerate = 16000  
    duration = 10

    recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_filename = temp_file.name
        sf.write(temp_filename, recording, samplerate)

    recognizer = sr.Recognizer()
    audio_text = ""

    with sr.AudioFile(temp_filename) as audio:
        audio_data = recognizer.record(audio)
        audio_text = recognizer.recognize_google(audio_data)

    if temp_filename:
        os.remove(temp_filename)

    return audio_text

def main():
    st.title("Speech-to-Text Web App")
    st.write("Click the 'Start' button, speak into your microphone, and see the transcribed text.")

    if st.button("Start"):
        audio_text = transcribe_audio()
        st.write("Transcribed Text:")
        st.write(audio_text)

if __name__ == "__main__":
    main()
