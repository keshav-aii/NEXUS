from core.command import Command

from automation.app_launcher import open_application



PLUGIN_INFO = {

    "name": "app",

    "priority": 50;

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

]




def handle(command: Command):


    text = command.normalized.lower()



    # Website commands ko skip karo

    for site in WEBSITE_WORDS:


        if site in text:


            return None





    if command.intent != "open":

        return None




    words = text.split()



    if "open" in words:


        index = words.index(
            "open"
        )


        target = " ".join(
            words[index + 1:]
        )



        if target:


            return open_application(
                target
            )



    return None