from gtts import gTTS
import playsound

def speak_hindi(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='hi')
    tts.save(filename)
    playsound.playsound(filename)
