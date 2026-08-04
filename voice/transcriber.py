from voice.models import MODEL


def transcribe(audio):

    segments, info = MODEL.transcribe(
    audio,
    language=None,
    beam_size=5,
    vad_filter=True,
    condition_on_previous_text=False,
    initial_prompt=(
        "NEXUS AI assistant. "
        "Wake words: Nexus, Nexa, Hey Nexus. "
        "Applications: Chrome, GitHub, VS Code, Spotify."
    )
)
    text = ""

    for segment in segments:

        text += segment.text


    return text.strip()