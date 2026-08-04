from core.plugin_loader import load_plugins


PLUGINS = load_plugins()


KEYWORD_MAP = {}


for plugin_name, plugin in PLUGINS.items():

    info = plugin["info"]

    intents = info.get(
        "intents",
        []
    )

    keywords = info.get(
        "keywords",
        []
    )


    for intent in intents:

        KEYWORD_MAP.setdefault(
            intent,
            []
        )

        KEYWORD_MAP[intent].extend(
            keywords
        )



# priority words
INTENT_PRIORITY = {

    "close": [
        "close",
        "quit",
        "terminate",
        "kill"
    ],

    "open": [
        "open",
        "launch",
        "start"
    ]

}



def detect_intent(command):


    text = command.normalized.lower()


    best_intent = None
    best_score = 0



    for intent, keywords in KEYWORD_MAP.items():


        score = 0


        for keyword in keywords:


            if keyword == text:

                score += 100


            elif f" {keyword} " in f" {text} ":

                score += 20


            elif keyword in text:

                score += 5



        # priority boost

        if intent in INTENT_PRIORITY:


            for word in INTENT_PRIORITY[intent]:

                if word in text:

                    score += 50



        print(
            "INTENT SCORE:",
            intent,
            score
        )



        if score > best_score:

            best_score = score
            best_intent = intent



    command.intent = best_intent


    command.confidence = (
        min(best_score / 100, 1.0)
        if best_intent
        else 0
    )


    return command