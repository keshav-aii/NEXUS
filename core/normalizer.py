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


VOICE_FIXES = {

    # conversation

    "hu r u": "who are you",
    "who r u": "who are you",
    "h r u": "how are you",
    "what is ur name": "what is your name",
    "whats your name": "what is your name",


    # open mistakes

    "oppen": "open",
    "opem": "open",
    "openin": "open",


    # close mistakes

    "nos": "close",
    "rose": "close",
    "post": "close",
    "cloze": "close",
    "closes": "close",
    "closs": "close",


    # exit mistakes

    "exet": "exit",
    "exist": "exit",
    "egzit": "exit",

}



def normalize(command: Command) -> Command:
    """
    Cleans user command text.
    Does not detect intent or entities.
    """


    # Original text

    text = command.raw.lower()



    # Voice corrections

    for wrong, correct in VOICE_FIXES.items():

        text = re.sub(
            rf"\b{wrong}\b",
            correct,
            text
        )


    # Remove punctuation

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )



    # Remove filler words

    for word in FILLER_WORDS:

        text = text.replace(
            word,
            ""
        )



    # Extra spaces

    text = " ".join(
        text.split()
    )



    command.normalized = text


    return command