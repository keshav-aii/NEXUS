from core.command import Command


INTENT_KEYWORDS = {

    "coding": [
        "start coding",
        "coding",
        "code",
        "developer",
    ],

    "open": [
        "open",
        "launch",
        "show",
        "go to",
    ],

    "create": [
        "create",
        "make",
        "new",
    ],

    "delete": [
        "delete",
        "remove",
    ],

    "search": [
        "search",
        "find",
        "look for",
    ],
}


def detect_intent(command: Command) -> Command:
    """
    Detects user intention.
    Does not execute anything.
    """

    text = command.normalized

    best_intent = None
    confidence = 0.0

    for intent, keywords in INTENT_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:

                best_intent = intent
                confidence = 0.9

                break

        if best_intent:
            break

    command.intent = best_intent
    command.confidence = confidence

    return command