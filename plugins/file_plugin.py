import os
import shutil

from core.command import Command



PLUGIN_INFO = {

    "name": "file",

    "priority": 30,

    "intents": [

        "open",
        "create",
        "delete"

    ]

}




FOLDER_MAP = {

    "downloads":
    os.path.expanduser("~/Downloads"),

    "desktop":
    os.path.expanduser("~/Desktop"),

    "documents":
    os.path.expanduser("~/Documents"),

    "pictures":
    os.path.expanduser("~/Pictures"),

    "music":
    os.path.expanduser("~/Music"),

}



DESKTOP = os.path.expanduser(
    "~/Desktop"
)





def handle(command: Command):


    intent = command.intent





    # ==========================
    # OPEN FOLDER
    # ==========================


    if intent == "open":


        target = command.entities.get(
            "target"
        )


        if not target:

            return None



        folder_path = FOLDER_MAP.get(
            target
        )



        if folder_path and os.path.exists(folder_path):


            os.startfile(
                folder_path
            )


            return {

                "action":
                "open",

                "item":
                target

            }




        return {

            "action":
            "file_not_found",

            "item":
            target

        }







    # ==========================
    # CREATE
    # ==========================


    if intent == "create":


        entity_type = command.entities.get(
            "type"
        )


        name = command.entities.get(
            "name"
        )



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

                "action":
                "folder_created",

                "item":
                name

            }






        if entity_type == "file":


            with open(
                path,
                "w"
            ) as f:

                f.write("")



            return {

                "action":
                "file_created",

                "item":
                name

            }







    # ==========================
    # DELETE
    # ==========================


    if intent == "delete":



        entity_type = command.entities.get(
            "type"
        )


        name = command.entities.get(
            "name"
        )



        if not name:


            return {

                "action":
                "missing_name"

            }






        path = os.path.join(
            DESKTOP,
            name
        )




        if not os.path.exists(path):


            return {

                "action":
                "file_not_found",

                "item":
                name

            }






        if entity_type == "file":


            os.remove(
                path
            )



            return {

                "action":
                "delete_success",

                "item":
                name

            }






        if entity_type == "folder":


            shutil.rmtree(
                path
            )



            return {

                "action":
                "folder_deleted",

                "item":
                name

            }





    return None