from core.command import Command
import string

from automation.resolver import resolve_open
from automation.app_launcher import close_application



PLUGIN_INFO = {

    "name": "app",

    "priority": 50,

    "intents": [

        "open",
        "close"

    ],

    "keywords": [

         "open",
        "launch",
        "start",

        "close",
        "quit",
        "exit",
        "stop",
        "kill",
        "terminate",
        "shutdown",
        "shut",
        "dismiss"

    ]

}





def handle(command: Command):


    text = command.normalized.lower().strip()



    # ==========================
    # CLOSE INTENT
    # ==========================


    if command.intent == "close":


        target = command.entities.get(
            "target"
        )


        if not target:

            return None



        result = close_application(
            target
        )


        print(
            "CLOSE RESULT:",
            result
        )



        if result.get("success"):


            return {


                "action":

                "app_closed",


                "item":

                target

            }



        return {


            "action":

            "app_close_failed",


            "item":

            target

        }






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



    target = target.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )



    if not target:


        return None





    result = resolve_open(
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