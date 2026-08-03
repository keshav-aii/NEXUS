from core.command import Command


INTENT_KEYWORDS = {

    "coding": [
        "start coding",
        "coding",
        "code",
        "developer",
        "workspace",
        "development",
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


KEYWORD_WEIGHTS = {

    "start coding": 10,
    "coding": 8,
    "developer": 6,
    "development": 5,
    "workspace": 5,

    "open": 5,
    "launch": 5,
    "show": 3,
    "go to": 3,

    "create": 5,
    "make": 3,
    "new": 2,

    "delete": 5,
    "remove": 4,

    "search": 5,
    "find": 4,
    "look for": 4,
}



def detect_intent(command: Command) -> Command:
    """
    Intent detection using keyword scoring.
    """

    text = command.normalized


    scores = {}


    for intent, keywords in INTENT_KEYWORDS.items():

        score = 0


        for keyword in keywords:

            if keyword in text:

                score += KEYWORD_WEIGHTS.get(
                    keyword,
                    1
                )


        if score > 0:

            scores[intent] = score



    if scores:

        best_intent = max(
            scores,
            key=scores.get
        )

        best_score = scores[best_intent]


        command.intent = best_intent

        command.confidence = min(
            best_score / 10,
            1.0
        )


    else:

        command.intent = None

        command.confidence = 0.0



    return command