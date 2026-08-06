from core.plugin_loader import load_plugins
from rapidfuzz import fuzz


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





# ======================
# INTENT PRIORITY
# Higher number wins ties
# ======================

INTENT_PRIORITY = {


    "memory": 10,

    "system": 9,

    "coding": 8,


    # close open se upar
    "close": 8,

    "open": 7,


    "create": 6,

    "delete": 6,


    "general": 2,

    "ai": 0

}





# ======================
# WORD BOOST
# ======================


WORD_PRIORITY = {


    "close": [

        "close",

        "quit",

        "exit",

        "stop",

        "terminate",

        "kill",

        "shutdown",

        "dismiss",

        "end"

    ],



    "open": [

        "open",

        "launch",

        "start"

    ]

}





def detect_intent(command):


    text = command.normalized.lower()



    scores = {}



    for intent, keywords in KEYWORD_MAP.items():


        score = 0



        for keyword in keywords:


            keyword = keyword.lower()



            # exact match

            if keyword in text:


                score += 50



            else:


                similarity = fuzz.partial_ratio(

                    keyword,

                    text

                )



                if similarity > 75:


                    score += similarity






        # ======================
        # ACTION BOOST
        # ======================


        if intent in WORD_PRIORITY:



            for word in WORD_PRIORITY[intent]:


                if word in text:


                    score += 80



        scores[intent] = score



        print(

            "INTENT SCORE:",

            intent,

            score

        )







    # ======================
    # SPECIAL CLOSE OVERRIDE
    # ======================


    close_words = [

        "close",

        "quit",

        "exit",

        "stop",

        "kill",

        "terminate",

        "shutdown"

    ]



    if any(
        word in text
        for word in close_words
    ):


        scores["close"] = scores.get(
            "close",
            0
        ) + 100







    # ======================
    # BEST INTENT
    # ======================


    best_intent = max(

        scores,

        key=lambda intent: (

            scores[intent],

            INTENT_PRIORITY.get(

                intent,

                0

            )

        )

    )



    best_score = scores[best_intent]



    command.intent = best_intent



    if best_score == 0:


        command.intent = "ai"





    command.confidence = (

        min(

            best_score / 100,

            1.0

        )

        if best_intent

        else 0

    )



    return command