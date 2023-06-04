import streamlit as st
import pyaudio
import speech_recognition as sr

# Set page config
st.set_page_config(
    page_title="Real-time Speech-to-Text Transcription App", page_icon="🎤", layout="wide"
)

# Set max width
def _max_width_():
    max_width_str = f"max-width: 1200px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

_max_width_()

# Speech recognition setup
r = sr.Recognizer()

# Function to start the transcription
def start_transcription():
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.text(text)  # Display the transcription in real-time
    except sr.UnknownValueError:
        st.warning("Could not understand audio")
    except sr.RequestError as e:
        st.error(f"Error: {str(e)}")

# Main app
def main():
    st.title("Real-time Speech-to-Text Transcription App")
    st.info("Click the button below and start speaking!")

    if st.button("Start Transcription"):
        while True:
            start_transcription()

# Run the app
if __name__ == "__main__":
    main()
