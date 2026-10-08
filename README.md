# Voice-to-Voice Translator — English to Hindi

A speech translation project that converts spoken English into Hindi text and then synthesizes the translated result back into speech.

The repository contains both a **Flask browser interface** and a **command-line audio pipeline**.

## Web App Flow

```text
Browser microphone
      │
      ▼
5-second audio recording
      │
      ▼
Flask upload
      │
      ▼
OpenAI Whisper transcription
      │
      ▼
English text
      │
      ▼
English → Hindi translation
      │
      ▼
gTTS Hindi speech
      │
      ▼
Browser audio playback
```

## Features

- Browser microphone recording
- English speech transcription
- English-to-Hindi translation
- Hindi text-to-speech generation
- Automatic audio playback
- Glassmorphism-style Flask UI
- Separate CLI translation pipeline

## Tech Stack

### Web App

- Python
- Flask
- OpenAI Whisper
- googletrans
- gTTS
- HTML / CSS / JavaScript
- Browser MediaRecorder API

### CLI Pipeline

- sounddevice
- SciPy
- OpenAI Whisper
- Hugging Face Transformers
- MarianMT (`Helsinki-NLP/opus-mt-en-hi`)
- gTTS
- playsound

## Project Structure

```text
Voice-to-Voice-Translator/
├── app.py
├── main.py
├── audio_input.py
├── whisper_model.py
├── translation.py
├── tts_output.py
├── input.wav
├── output.mp3
└── README.md
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it and install the main packages:

```bash
pip install flask openai-whisper googletrans==4.0.0-rc1 gTTS soundfile sounddevice scipy transformers sentencepiece playsound torch
```

Whisper also requires **FFmpeg** to be installed and available on your system path.

## Run the Web App

```bash
python app.py
```

Open:

```text
http://127.0.0.1:7860
```

Click **Speak Now**, allow microphone access, and speak in English.

The application records a short audio sample, transcribes it, translates it to Hindi, generates Hindi speech, and plays the output.

## Run the CLI Pipeline

```bash
python main.py
```

The CLI version:

1. records microphone audio
2. transcribes it with Whisper
3. translates it with MarianMT
4. generates Hindi speech with gTTS
5. plays the resulting audio

## Current Scope

The current project is centered on **English → Hindi** translation.

## Limitations

- Translation and gTTS paths require internet connectivity.
- Whisper model loading can take time on the first run.
- Browser microphone access requires user permission.
- This is a prototype rather than a low-latency streaming speech-to-speech system.

## Author

**Sankalp Gupta**

GitHub: https://github.com/Sankalp-gupta1
