import os

from core.command import Command


PLUGIN_INFO = {
    "name": "file",
    "intents": [
        "open"
    ]
}


FOLDER_MAP = {

    "downloads": os.path.expanduser("~/Downloads"),

    "desktop": os.path.expanduser("~/Desktop"),

    "documents": os.path.expanduser("~/Documents"),

    "pictures": os.path.expanduser("~/Pictures"),

    "music": os.path.expanduser("~/Music"),
}


def handle(command: Command):
   

    # Only handle open intent

    if command.intent != "open":
        return None


    target = command.entities.get("target")


    if not target:
        return None


    folder_path = FOLDER_MAP.get(target)


    if not folder_path:
        return None


    if os.path.exists(folder_path):
      
        
        os.startfile(folder_path)
        
        return {
            "message": f"Opening {target.title()}."
        }


    return {
        "message": f"{target.title()} folder not found."
    }