import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text
    except sr.RequestError:
        return "API unavailable or unresponsive."
    except sr.UnknownValueError:
        return "Unable to recognize speech."

# Example usage:
mp3_file = "/workspaces/Socrates-Ai/audio/output.mp3"
wav_file = "converted_audio_file.wav"

convert_mp3_to_wav(mp3_file, wav_file)
transcription = speech_to_text(wav_file)
print("Transcribed Text:", transcription)
