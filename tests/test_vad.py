import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from voice.microphone import record
from voice.vad import has_speech

print("Speak...")

audio = record(5)

print(audio.shape)
print(audio.max())
print(audio.min())

print(has_speech(audio))