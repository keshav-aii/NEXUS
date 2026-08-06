from core.command import Command



PLUGIN_INFO = {

    "name": "general",

    "priority": 5,

    "intents": [

        "general"

    ],

    "keywords": [

        "hello",
        "hi",
        "hey",
        "how are you",
        "how r u",
        "who are you",
        "whats my name",
        "what's my name",
       
       
        "thank you",
        "thanks",
        "good morning",
        "good night",
        "bye",
        "what can you do",
        "are you there",
        "wake up"

    ]

}





def handle(command: Command):


    text = command.normalized.lower()



    if command.intent != "general":

        return None





    # ======================
    # HOW ARE YOU
    # ======================

    if (
        "how are you" in text
        or
        "how r u" in text
    ):

        return {

            "action": "general",

            "message":
            "Main badhiya hoon boss, aap batao."

        }






    # ======================
    # IDENTITY
    # ======================

    if (
        "who are you" in text
        or
        "what is your name" in text
    ):

        return {

            "action": "general",

            "message":
            "Main NEXA hoon boss, aapki AI assistant."

        }






    # ======================
    # THANKS
    # ======================

    if (
        "thank" in text
        or
        "thanks" in text
    ):

        return {

            "action": "general",

            "message":
            "Welcome boss."

        }






    # ======================
    # GOOD MORNING
    # ======================

    if "good morning" in text:

        return {

            "action": "general",

            "message":
            "Good morning boss, umeed hai aapka din accha rahega."

        }






    # ======================
    # GOOD NIGHT
    # ======================

    if "good night" in text:

        return {

            "action": "general",

            "message":
            "Good night boss, rest kijiye. Main standby me hoon."

        }






    # ======================
    # WHAT CAN YOU DO
    # ======================

    if "what can you do" in text:

        return {

            "action": "general",

            "message":
            "Main apps open kar sakti hoon, files handle kar sakti hoon, memory manage kar sakti hoon aur coding me help kar sakti hoon."

        }






    # ======================
    # ARE YOU THERE
    # ======================

    if "are you there" in text or "wake up" in text:

        return {

            "action": "general",

            "message":
            "Haan boss, main yahin hoon."

        }






    # ======================
    # BYE
    # ======================

    if "bye" in text:

        return {

            "action": "general",

            "message":
            "Okay boss, milte hain."

        }






    # ======================
    # DEFAULT
    # ======================

    return {

        "action": "general",

        "message":
        "Haan boss, bolo."

    }