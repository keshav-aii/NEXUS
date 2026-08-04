import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


from voice.speaker import speak


speak(
    "Hello, main NEXA hoon"
)