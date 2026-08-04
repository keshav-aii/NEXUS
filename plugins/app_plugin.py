from core.command import Command

from automation.app_launcher import open_application



PLUGIN_INFO = {

    "name": "app",

    "priority": 50,

    "intents": [

        "open"

    ]

}




WEBSITE_WORDS = [

    "github",
    "youtube",
    "google",
    "linkedin",
    "chatgpt",
    "gmail",

]





def handle(command: Command):


    text = command.normalized.lower().strip()



    # ==========================
    # WEBSITE SKIP
    # ==========================


    for site in WEBSITE_WORDS:


        if site in text:


            return None






    # ==========================
    # ONLY OPEN INTENT
    # ==========================


    if command.intent != "open":


        return None






    words = text.split()



    if "open" not in words:


        return None






    index = words.index(
        "open"
    )



    target = " ".join(
        words[index + 1:]
    )



    if not target:


        return None






    result = open_application(
        target
    )



    print(
        "APP RESULT:",
        result
    )





    # ==========================
    # SUCCESS
    # ==========================


    if result:


        return {

            "action":

            "app_opened",


            "item":

            target

        }






    # ==========================
    # FAILED
    # ==========================


    return {

        "action":

        "app_failed",


        "item":

        target

    }