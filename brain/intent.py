OPEN_WORDS = [
    "open",
    "launch",
    "start",
    "run",
]

GOOGLE_WORDS = [
    "search google for",
    "google",
]

YOUTUBE_WORDS = [
    "search youtube for",
    "youtube search",
]


def detect_intent(command):

    command = command.lower().strip()

    for word in OPEN_WORDS:
        if command.startswith(word):
            return {
                "intent": "open",
                "target": command.replace(word, "", 1).strip()
            }

    for word in GOOGLE_WORDS:
        if command.startswith(word):
            return {
                "intent": "google",
                "target": command.replace(word, "", 1).strip()
            }

    for word in YOUTUBE_WORDS:
        if command.startswith(word):
            return {
                "intent": "youtube",
                "target": command.replace(word, "", 1).strip()
            }

    return {
        "intent": "chat",
        "target": command
    }