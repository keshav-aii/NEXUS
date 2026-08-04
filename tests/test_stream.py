
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from voice.stream import audio_stream

print("Streaming...")

for chunk in audio_stream():

    print(chunk.shape)