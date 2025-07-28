🎙️ Voice Translator Web App (English → Hindi)
This is a speech-based real-time voice translator built with Flask and Python. It allows you to speak in English, recognizes the voice, and translates the speech into Hindi, all through a beautiful, modern web interface.

Perfect for quick translation, language learning, or communication.

🚀 Features
🎤 Speech Recognition using speech_recognition

🌐 Translation from English to Hindi using googletrans

⚡ Instant Response without page reload

🧠 Smart Language Detection using langdetect

🎨 Sleek UI with dark mode, glassmorphism, and animation

🖱️ One-click "Speak Now" button

🪪 Built on Flask – lightweight and fast

🖼️ UI Preview
<!<img width="1914" height="876" alt="Screenshot 2025-07-28 145807" src="https://github.com/user-attachments/assets/5629459b-645a-4a94-beb2-2cdbcc05139c" />
-->

📂 Project Folder Structure
csharp
Copy
Edit
voice_translator/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend HTML + CSS (inline)
├── static/
│   ├── favicon.ico        # Optional icon
│   └── app_preview.png    # UI Screenshot (optional)
└── README.md              # This file
🛠️ Installation Guide
1. 📥 Clone the Repository
bash
Copy
Edit
git clone https://github.com/<your-username>/voice_translator.git
cd voice_translator
2. 🐍 Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows

# OR

source venv/bin/activate  # On Linux/Mac
3. 📦 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

bash
Copy
Edit
pip install Flask SpeechRecognition googletrans==4.0.0-rc1 langdetect
🧪 How to Run
bash
Copy
Edit
python app.py
Then open your browser and visit:
👉 http://localhost:5000

🎮 Usage Instructions
Press the "Speak Now" button.

Say something in English.

The app will:

Convert speech to text

Auto-detect language

Translate to Hindi

Show the translated output instantly

📌 Current Capabilities
From Language	To Language	Status
English	Hindi	✅ Working
Hindi	English	❌ Not Yet

🔄 Future updates will include bi-directional translation and language selector.

🧩 Dependencies
Flask – Web framework (Backend)

SpeechRecognition – Convert speech to text

googletrans – Google Translate wrapper

langdetect – Detect spoken language automatically

🤝 Contributing
Pull requests are welcome! If you'd like to:

Add more language pairs

Improve UI

Add browser/mobile support

Optimize performance

👉 Create an issue or fork and submit a PR.

💡 Future Plans
🔄 Hindi → English support

🌐 Multi-language dropdown

📱 Mobile responsive view

💾 Translation history saving

🎙️ Real-time microphone waveform

👨‍💻 Author
Sankalp Gupta
📧 csjma22001390321csemockai@csjmu.ac.in

📃 License
This project is open source and free to use under the MIT License.
