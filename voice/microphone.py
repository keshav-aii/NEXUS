import sounddevice as sd
import numpy as np


SAMPLE_RATE = 16000


def record(seconds=5):

    audio = sd.rec(

        int(seconds * SAMPLE_RATE),

        samplerate=SAMPLE_RATE,

        channels=1,

        dtype="float32"

    )

    sd.wait()

    return audio.flatten()