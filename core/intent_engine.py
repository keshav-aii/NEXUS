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

        "memory": [

         "remember",
        "what do you remember",
        "what is my",
        "what's my",
        "whats my",
        "recall",
        "forget",

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

    "remember": 10,
    "what do you remember": 10,
    "what is my": 8,
    "recall": 8,
    "forget": 5,

}



def detect_intent(command: Command) -> Command:

    text = command.normalized.lower()

    text = text.replace(
        "what's",
        "what is"
    )



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

        # Memory priority

  # Memory priority

    if (
        "remember" in text
        or "what do you remember" in text
        or "what is my" in text
        or "what's my" in text
        or "whats my" in text
        or "recall" in text
    ):

        command.intent = "memory"

        command.confidence = 1.0

        return command


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