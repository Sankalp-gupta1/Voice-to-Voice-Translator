import whisper

model = whisper.load_model("base")  # or "medium", "large"
def transcribe_audio(filename):
    result = model.transcribe(filename)
    return result["text"]
