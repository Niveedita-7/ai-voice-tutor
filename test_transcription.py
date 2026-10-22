from faster_whisper import WhisperModel

print("Loading Whisper model...")

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8",
)

print("Whisper loaded successfully!")
print("Now record a short audio clip in the main app to test transcription.")