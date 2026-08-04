from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities
from core.plugin_loader import load_plugins

from core.message_engine import get_message



PLUGINS = load_plugins()




def process(command):


    print(
        "ROUTER COMMAND:",
        command.normalized
    )



    # ======================
    # INTENT
    # ======================

    command = detect_intent(
        command
    )


    print(
        "INTENT:",
        command.intent
    )




    # ======================
    # ENTITIES
    # ======================

    command = extract_entities(
        command
    )


    print(
        "ENTITIES:",
        command.entities
    )





    # ======================
    # DELETE CONFIRMATION
    # ======================


    if (
        command.intent == "delete"
        and not command.context.get("confirmed")
    ):


        return {


            "type":
            "confirmation",



            "message":

            get_message(

                "delete_confirm",

                item=command.entities.get(
                    "name",
                    "file"
                )

            ),



            "command":
            command

        }





    print(
        "CONFIRMED FLAG:",
        command.context.get("confirmed")
    )




    print(
        "LOADED PLUGINS:",
        [
            p["info"].get("name")
            for p in PLUGINS
        ]
    )





    # ======================
    # PLUGINS
    # ======================


    for plugin in PLUGINS:



        print(
            "TRY PLUGIN:",
            plugin["info"].get("name")
        )



        handler = plugin["handler"]




        try:



            result = handler(
                command
            )



            if result:



                return {


                    "type":

                    "plugin",



                    "data":

                    result

                }





        except Exception as e:


            print(
                "PLUGIN ERROR:",
                e
            )





    # ======================
    # UNKNOWN
    # ======================


    return None