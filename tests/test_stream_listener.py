import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from voice.listener import listen

while True:

    text = listen()

    print("TEXT:", text)