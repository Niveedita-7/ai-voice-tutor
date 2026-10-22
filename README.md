# AI Voice Tutor

An interactive AI-powered voice tutor that allows students to ask questions using **text or speech**, learn from uploaded **PDF study material**, and receive explanations, quizzes, and interview-style practice using a locally running LLM.

## Features

- **Voice-based questions** — Record a question using the microphone.
- **Speech-to-text** — Uses Faster-Whisper to convert spoken questions into text.
- **AI tutoring** — Uses Ollama with Qwen 2.5 3B to generate responses locally.
- **PDF Q&A** — Upload a small PDF and ask questions about its contents.
- **Learning modes**
  - Explain a Concept
  - Quiz Me
  - Interview Practice
- **Subject selection** — Supports general knowledge, Python, mathematics, science, English, and computer science.
- **Conversation history** — Maintains the recent conversation for contextual responses.
- **Transcript correction** — Review and edit voice transcriptions before sending them to the tutor.
- **Text-to-speech** — Reads tutor responses aloud using the browser's speech synthesis system.
- **Local AI processing** — The LLM runs through Ollama on the user's machine.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Faster-Whisper | Speech recognition |
| Ollama | Local LLM runtime |
| Qwen 2.5 3B | AI tutoring model |
| PyPDF | PDF text extraction |
| PyAV | Audio processing |
| CTranslate2 | Fast Whisper inference |
| Browser Speech Synthesis | Text-to-speech |

## How It Works

### Voice Question

```text
User speaks
    ↓
Streamlit Audio Input
    ↓
Faster-Whisper
    ↓
Transcript
    ↓
Optional transcript correction
    ↓
Ollama / Qwen 2.5 3B
    ↓
Tutor Response
    ↓
Browser Text-to-Speech
```

### PDF Question Answering

```text
PDF Upload
    ↓
PyPDF text extraction
    ↓
PDF content stored in session
    ↓
User asks a question
    ↓
PDF context + question
    ↓
Ollama / Qwen 2.5 3B
    ↓
Answer based on the uploaded material
```

## Project Structure

```text
ai-voice-tutor/
│
├── app.py
├── test_transcription.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.12
- Ollama
- Qwen 2.5 3B model
- Microphone for voice input
- A modern web browser

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Niveedita-7/ai-voice-tutor.git
cd ai-voice-tutor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Install and run Ollama

Install Ollama and make sure it is running locally.

Then download the Qwen model:

```powershell
ollama pull qwen2.5:3b
```

The application expects Ollama at:

```text
http://localhost:11434/api/chat
```

### 6. Run the application

```powershell
streamlit run app.py
```

The application will open in your browser at the local Streamlit address.

## Using the Application

### Ask a Question

You can type a question using the chat input or record one using the microphone.

### Use a PDF

1. Upload a small, text-based PDF.
2. Wait for the PDF to be loaded.
3. Ask questions about its contents.
4. The tutor uses the extracted PDF text as reference material.

For example:

```text
Upload: Operating_Systems_Notes.pdf

Question:
"Explain the difference between a process and a thread."
```

### Learning Modes

**Explain a Concept**

The tutor explains concepts step-by-step and provides examples.

**Quiz Me**

The tutor generates educational quiz questions to help with practice.

**Interview Practice**

The tutor acts as an interviewer and provides constructive feedback.

## Privacy

The application is designed around local AI processing.

The tutoring model is accessed through a locally running Ollama server rather than a hosted LLM API. Uploaded PDF content is processed within the Streamlit application and provided to the local model as context.

## Current Limitations

- PDF question answering currently works best with **small, text-based PDFs**.
- Scanned/image-only PDFs may not contain extractable text.
- The current PDF implementation sends the extracted document text as context rather than using a vector database.
- Text-to-speech quality depends on the voices available through the user's browser and operating system.
- Whisper transcription runs on the CPU using the `tiny` model.

## Future Improvements

Planned improvements include:

- Retrieval-Augmented Generation (RAG) for larger PDFs
- PDF chunking and semantic search
- Embeddings and vector database integration
- Page-level citations for PDF answers
- More natural neural text-to-speech
- Additional subjects and learning modes
- Improved conversational voice interaction
- Progress tracking and personalized learning
- Quiz scoring and performance analytics

## Author

**Niveedita Deshpande**

GitHub: https://github.com/Niveedita-7