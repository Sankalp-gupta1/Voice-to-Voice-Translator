from audio_input import record_audio
from whisper_model import transcribe_audio
from translation import translate_to_hindi
from tts_output import speak_hindi

if __name__ == "__main__":
    audio_file = record_audio()
    english_text = transcribe_audio(audio_file)
    print("📝 English:", english_text)
    
    hindi_text = translate_to_hindi(english_text)
    print("🔁 Hindi:", hindi_text)

    speak_hindi(hindi_text)
