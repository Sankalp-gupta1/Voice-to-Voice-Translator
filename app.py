from flask import Flask, render_template_string, request, jsonify
import os
import whisper
import soundfile as sf
from gtts import gTTS
import uuid

app = Flask(__name__)
model = whisper.load_model("base")

# HTML + CSS (Modern Glassmorphic UI)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🎤 Speak & Translate</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
        }

        .container {
            background: rgba(255, 255, 255, 0.05);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            width: 90%;
            max-width: 600px;
        }

        h1 {
            font-size: 2em;
            margin-bottom: 20px;
            color: #f8f8f8;
            text-shadow: 1px 1px 5px #000;
        }

        button {
            padding: 14px 28px;
            font-size: 18px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        button:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, #fc466b, #3f5efb);
        }

        button:disabled {
            background: #555;
            cursor: not-allowed;
        }

        audio {
            margin-top: 25px;
            width: 100%;
        }

        .output {
            margin-top: 30px;
            font-size: 1.1em;
            color: #ffffffcc;
        }

        .loading {
            font-style: italic;
            color: #ccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎙 AI Voice Translator<br><small>(English ➜ Hindi)</small></h1>
        <button id="startBtn">🎤 Speak Now</button>
        <audio id="audioPlayback" controls style="display:none;"></audio>
        <div class="output" id="output"></div>
    </div>

<script>
let startBtn = document.getElementById("startBtn");
let audioPlayback = document.getElementById("audioPlayback");
let output = document.getElementById("output");

startBtn.onclick = async () => {
    startBtn.disabled = true;
    output.innerHTML = "<span class='loading'>🎙 Recording... speak now!</span>";
    
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    const audioChunks = [];

    mediaRecorder.ondataavailable = event => {
        if (event.data.size > 0) audioChunks.push(event.data);
    };

    mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const formData = new FormData();
        formData.append('audio_data', audioBlob, 'recording.wav');

        output.innerHTML = "<span class='loading'>🧠 Translating...</span>";

        const response = await fetch('/process', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            output.innerHTML = "❌ Error: " + data.error;
        } else {
            output.innerHTML = `<b>📄 Transcription:</b> ${data.text}<br><b>🔊 Hindi Translation:</b> ${data.translated}`;
            audioPlayback.src = "/audio/" + data.audio;
            audioPlayback.style.display = 'block';
            audioPlayback.play();
        }

        startBtn.disabled = false;
    };

    mediaRecorder.start();
    setTimeout(() => mediaRecorder.stop(), 5000);
};
</script>
</body>
</html>
'''

# Google Translator
from googletrans import Translator
translator = Translator()

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/process', methods=['POST'])
def process_audio():
    file = request.files['audio_data']
    filename = f"temp_{uuid.uuid4().hex}.wav"
    filepath = os.path.join("static", filename)
    file.save(filepath)

    try:
        result = model.transcribe(filepath)['text']
        translated = translator.translate(result, src='en', dest='hi').text
        
        tts = gTTS(translated, lang='hi')
        mp3name = f"{uuid.uuid4().hex}.mp3"
        mp3path = os.path.join("static", mp3name)
        tts.save(mp3path)

        return jsonify({"text": result, "translated": translated, "audio": mp3name})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/audio/<filename>')
def serve_audio(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    os.makedirs("static", exist_ok=True)
    app.run(debug=True, port=7860)
