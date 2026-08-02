import asyncio
import edge_tts
import tempfile
import os
from playsound import playsound

VOICE = "en-US-GuyNeural"


async def _generate(text, filename):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)


def speak(text):
    print(f"NEXUS: {text}")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.close()

    try:
        asyncio.run(_generate(text, temp_file.name))
        playsound(temp_file.name)

        import time
        time.sleep(0.5)
    finally:
        try:
            os.remove(temp_file.name)
        except:
            pass