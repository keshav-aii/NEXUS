from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities
from core.plugin_loader import load_plugins



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

    # DELETE CONFIRMATION

    if (
        command.intent == "delete"
        and not command.context.get("confirmed")
    ):


        return {

            "type": "confirmation",

            "message":
            f"Do you want to delete {command.entities.get('name')}?",

            "command": command
        }

    print(
        "CONFIRMED FLAG:",
        command.context.get("confirmed")
    )

    # ======================
    # PLUGINS
    # ======================

    for plugin in PLUGINS:


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



    return None