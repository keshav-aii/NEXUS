import queue
import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000
BLOCK_SIZE = 5120   # 100 ms
DEVICE = 1

_audio_queue = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status)

    _audio_queue.put(indata.copy())

import sounddevice as sd

print(sd.query_devices())

def audio_stream():

    with sd.InputStream(
    device=DEVICE,
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
    blocksize=BLOCK_SIZE,
    callback=callback
):

        while True:

            chunk = _audio_queue.get()

            yield chunk.flatten()