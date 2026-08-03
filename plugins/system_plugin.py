import os
import subprocess
from automation.automation import open_app
from core.command import Command


PLUGIN_INFO = {
    "name": "system",
    "intents": [
        "system"
    ]
}







def handle(command: Command):


    text = command.normalized.lower()



    # Open Apps
    apps = [
        "calculator",
        "notepad",
        "paint",
        "chrome",
    ]


    for app in apps:

        if app in text:

            result = open_app(app)

            return {
                "message": result

            }

    # Lock PC

    if "lock" in text:

        os.system(
            "rundll32.exe user32.dll,LockWorkStation"
        )

        return {
            "message": "Locking computer."
        }



    # Shutdown

    if "shutdown" in text:

        os.system(
            "shutdown /s /t 5"
        )

        return {
            "message": "Shutting down computer."
        }



    # Restart

    if "restart" in text:

        os.system(
            "shutdown /r /t 5"
        )

        return {
            "message": "Restarting computer."
        }



    return None