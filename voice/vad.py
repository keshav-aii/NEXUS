import torch

from silero_vad import load_silero_vad
from silero_vad import get_speech_timestamps


model = load_silero_vad()


def has_speech(audio, sample_rate=16000):

    if not isinstance(audio, torch.Tensor):
        audio = torch.from_numpy(audio)

    audio = audio.float()

    timestamps = get_speech_timestamps(
        audio,
        model,
        sampling_rate=sample_rate,
        threshold=0.3
    )

    return len(timestamps) > 0