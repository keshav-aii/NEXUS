import os

from core.command import Command



PLUGIN_INFO = {

    "name": "system",

    "priority": 100,

    "intents": [

        "system"

    ]

}





def handle(command: Command):


    text = command.normalized.lower().strip()



    # ==========================
    # LOCK
    # ==========================


    if "lock" in text:


        os.system(
            "rundll32.exe user32.dll,LockWorkStation"
        )


        return {

            "message":
            "Locking computer."

        }





    # ==========================
    # SHUTDOWN
    # ==========================


    if "shutdown" in text:


        os.system(
            "shutdown /s /t 5"
        )


        return {

            "message":
            "Shutting down computer."

        }





    # ==========================
    # RESTART
    # ==========================


    if "restart" in text:


        os.system(
            "shutdown /r /t 5"
        )


        return {

            "message":
            "Restarting computer."

        }




    return None