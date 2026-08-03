from core.command import Command


SYSTEM_COMMANDS = [

    "open calculator",
    "open notepad",
    "open paint",

    "lock",
    "shutdown",
    "restart",

]


INTENT_KEYWORDS = {

    "coding": [

        "start coding",
        "coding",
        "code",
        "developer",
        "workspace",
        "development",

    ],


    "youtube": [

        "youtube",
        "you tube",

    ],


    "search": [

        "search",
        "find",
        "look for",

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

}



KEYWORD_WEIGHTS = {


    "start coding": 10,
    "coding": 8,
    "developer": 6,
    "development": 5,
    "workspace": 5,


    "youtube": 10,
    "you tube": 10,


    "search": 5,
    "find": 4,
    "look for": 4,


    "open": 5,
    "launch": 5,
    "show": 3,
    "go to": 3,


    "create": 5,
    "make": 3,
    "new": 2,


    "delete": 5,
    "remove": 4,

}



def detect_intent(command: Command) -> Command:

    text = command.normalized.lower()



    # System priority

    for item in SYSTEM_COMMANDS:

        if item in text:

            command.intent = "system"

            command.confidence = 1.0

            return command



    # YouTube priority

    if "youtube" in text or "you tube" in text:

        command.intent = "youtube"

        command.confidence = 1.0

        return command



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