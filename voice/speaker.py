import asyncio
import tempfile
import os

import edge_tts
from playsound import playsound


VOICE = "hi-IN-SwaraNeural"
RATE = "+10%"
PITCH = "+5Hz"



async def _generate(text, filename):

    communicate = edge_tts.Communicate(
        text,
        VOICE,
        rate=RATE,
        pitch=PITCH
    )

    await communicate.save(
        filename
    )





def speak(text):


    if isinstance(text, dict):

        text = text.get(
            "message",
            ""
        )


    if not text:

        return



    text = str(text)



    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    ) as temp_file:

        file_path = temp_file.name



    try:


        asyncio.run(
            _generate(
                text,
                file_path
            )
        )


        playsound(
            file_path
        )



    finally:


        try:

            os.remove(
                file_path
            )

        except:

            pass