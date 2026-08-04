import numpy as np

from voice.stream import audio_stream
from voice.vad import has_speech


for chunk in audio_stream():

    print(
        "MAX:",
        np.max(np.abs(chunk))
    )


    if has_speech(chunk):

        print(
            "SPEECH YES"
        )