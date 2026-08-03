import os
import shutil

from core.command import Command


PLUGIN_INFO = {
    "name": "file",
    "intents": [
        "open",
        "create",
        "delete"
    ]
}


FOLDER_MAP = {

    "downloads": os.path.expanduser("~/Downloads"),
    "desktop": os.path.expanduser("~/Desktop"),
    "documents": os.path.expanduser("~/Documents"),
    "pictures": os.path.expanduser("~/Pictures"),
    "music": os.path.expanduser("~/Music"),
}


DESKTOP = os.path.expanduser("~/Desktop")


def handle(command: Command):


    if command.intent == "open":

        target = command.entities.get("target")

        if not target:
            return None


        folder_path = FOLDER_MAP.get(target)


        if folder_path and os.path.exists(folder_path):

            os.startfile(folder_path)

            return {
                "message": f"Opening {target.title()}."
            }



    if command.intent == "create":

        entity_type = command.entities.get("type")
        name = command.entities.get("name")


        if not name:
            return None


        path = os.path.join(
            DESKTOP,
            name
        )


        if entity_type == "folder":

            os.makedirs(
                path,
                exist_ok=True
            )


            return {
                "message": f"Created folder {name}."
            }



        if entity_type == "file":

            with open(path, "w") as f:
                f.write("")


            return {
                "message": f"Created file {name}."
            }



    if command.intent == "delete":

        entity_type = command.entities.get("type")
        name = command.entities.get("name")


        if not name:
            return None


        path = os.path.join(
            DESKTOP,
            name
        )


        if not os.path.exists(path):

            return {
                "message": f"{name} not found."
            }


        if entity_type == "file":

            os.remove(path)

            return {
                "message": f"Deleted file {name}."
            }


        if entity_type == "folder":

            shutil.rmtree(path)

            return {
                "message": f"Deleted folder {name}."
            }


    return None