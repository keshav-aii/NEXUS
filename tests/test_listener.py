import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from voice.listener import listen

print("Waiting for speech...")

text = listen()

print(text)