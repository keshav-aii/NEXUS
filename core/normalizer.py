import re

from core.command import Command


FILLER_WORDS = [
    "please",
    "kindly",
    "can you",
    "could you",
    "would you",
    "hey",
]


def normalize(command: Command) -> Command:
    """
    Cleans user command text.
    Does not detect intent or entities.
    """

    text = command.raw.lower()

    # Remove punctuation but preserve dots for file extensions
    text = re.sub(r"[^\w\s.]", "", text)

    # Remove filler words
    for word in FILLER_WORDS:
        text = text.replace(word, "")

    # Remove extra spaces
    text = " ".join(text.split())

    command.normalized = text

    return command