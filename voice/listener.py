import numpy as np

from voice.stream import audio_stream
from voice.vad import has_speech
from voice.transcriber import transcribe


def listen():

    print("Waiting for speech...")

    recording = False

    silence_count = 0

    chunks = []


    for chunk in audio_stream():


        if has_speech(chunk):

            if not recording:

                print("🎤 Speech detected...")

                recording = True


            silence_count = 0

            chunks.append(chunk)


        else:


            if recording:

                silence_count += 1

                chunks.append(chunk)


                if silence_count >= 15:

                    break



    if not chunks:

        return ""


    audio = np.concatenate(chunks)


    print(
        "📝 Transcribing..."
    )


    text = transcribe(audio)


    return text