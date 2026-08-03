OPEN_WORDS = [
    "open",
    "launch",
    "start",
    "run",
]


SEARCH_WORDS = [
    "search",
    "find",
    "look for",
]


GOOGLE_WORDS = [
    "search google for",
    "google",
]


YOUTUBE_WORDS = [
    "youtube",
    "you tube",
]



def detect_intent(command):

    command = command.lower().strip()



    # Open

    for word in OPEN_WORDS:

        if command.startswith(word):

            return {
                "intent": "open",
                "target": command.replace(word, "", 1).strip()
            }



    # YouTube (before generic search)

    for word in YOUTUBE_WORDS:

        if word in command:

            query = (
                command
                .replace(word, "")
                .replace("search", "")
                .replace("on", "")
                .strip()
            )

            return {
                "intent": "youtube",
                "target": query
            }



    # Google explicit

    for word in GOOGLE_WORDS:

        if command.startswith(word):

            return {
                "intent": "google",
                "target": command.replace(word, "", 1).strip()
            }



    # Generic search

    for word in SEARCH_WORDS:

        if command.startswith(word):

            return {
                "intent": "google",
                "target": command.replace(word, "", 1).strip()
            }



    return {
        "intent": "chat",
        "target": command
    }