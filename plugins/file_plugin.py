import os

from core.command import Command


PLUGIN_INFO = {
    "name": "file",
    "intents": [
        "open",
        "create"
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


    if command.intent == "open":

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


    if command.intent == "create":

        entity_type = command.entities.get("type")
        name = command.entities.get("name")


    if not name:
        return None


    if entity_type == "folder":

        path = os.path.join(
            os.path.expanduser("~/Desktop"),
            name
        )

        os.makedirs(
            path,
            exist_ok=True
        )


        return {
            "message": f"Created folder {name}."
        }



    if entity_type == "file":

        path = os.path.join(
            os.path.expanduser("~/Desktop"),
            name
        )


        with open(path, "w") as f:
            f.write("")


        return {
            "message": f"Created file {name}."
        }  
    
        return None