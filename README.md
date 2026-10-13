# Voice-to-Voice Translator

## Live app

**https://voice-to-voice-translator.vercel.app/**

The original local pipeline uses Whisper for speech recognition and gTTS for speech output.

The hosted browser version in `web/` removes the heavyweight server requirement and supports:

- browser speech recognition where supported,
- typed-text fallback,
- English, Hindi, Spanish, French and German options,
- translation through a public translation endpoint,
- browser speech synthesis for translated output,
- source/target language swapping.

Browser speech-recognition support varies by browser, but typed translation remains usable.

### Run locally

```bash
cd web
python -m http.server 8000
```

---

A speech translation project with both a local AI pipeline and a deployable browser version.

## Live app


## Original local version

The Python files use:

- Flask
- OpenAI Whisper
- Google Translate wrapper
- gTTS
- local audio recording / playback

That version remains available for local experimentation.

## Deployed browser version

The `web/` version uses:

- Web Speech API for speech recognition,
- MyMemory for text translation,
- browser speech synthesis for playback.

It supports English, Hindi, Spanish, French and German in the live UI.

No private API key is required.

## Browser support

Chrome and Edge generally provide the best speech-recognition support.

If microphone recognition is unavailable, you can type text manually and still use translation and speech playback.

## Run locally

```bash
cd web
python -m http.server 8000
```

Open `http://localhost:8000`.

## Privacy note

The browser handles speech recognition / synthesis according to its own speech services. Text is sent to the translation API only when translation is requested.

## Author

Sankalp Gupta  
GitHub: https://github.com/Sankalp-gupta1
