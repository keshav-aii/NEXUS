from faster_whisper import WhisperModel

print("Loading Faster Whisper model...")

MODEL = WhisperModel(
    "small",
    device="cuda",
    compute_type="float16"
)

print("✅ Faster Whisper ready.")