from brain.memory_manager import handle_memory
from tools.tool_manager import choose_tool
from brain.brain import ask_nexa

from core.plugin_loader import load_plugins
from core.normalizer import normalize
from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities

from brain.state_manager import (
    set_pending,
    get_pending,
    clear_pending
)



plugins = load_plugins()



def process(command):


    # ==========================
    # Confirmation Check
    # ==========================

    pending = get_pending()


    if pending:


        answer = command.raw.lower().strip()



        if answer in [

            "yes",
            "yeah",
            "yep",
            "ok",
            "okay",
            "confirm",
            "haan",
            "ha",
            "kar do",
            "do it"

        ]:


            clear_pending()


            result = pending["handler"](
                pending["command"]
            )


            return {

                "type": "plugin",

                "data": result

            }




        if answer in [

            "no",
            "cancel",
            "stop",
            "nahi",
            "mat karo"

        ]:


            clear_pending()


            return {

                "type": "system",

                "message": "Cancelled."

            }



        return {

            "type": "system",

            "message": "Please confirm yes or no."

        }





    # ==========================
    # Pipeline
    # ==========================


    command = normalize(
        command
    )


    command = detect_intent(
        command
    )


    command = extract_entities(
        command
    )





    # ==========================
    # Memory
    # ==========================

    memory = handle_memory(
        command.normalized
    )


    if memory:


        return {

            "type": "memory",

            "message": memory

        }





    # ==========================
    # Plugins
    # ==========================

    for plugin in plugins:


        intents = plugin["info"].get(
            "intents",
            []
        )


        if command.intent not in intents:

            continue




        if command.intent == "delete":


            set_pending({

                "handler": plugin["handler"],

                "command": command

            })


            return {

                "type": "confirmation",

                "message":
                f"Do you want to delete {command.entities.get('name')}?"

            }





        result = plugin["handler"](
            command
        )



        if result:


            return {

                "type": "plugin",

                "data": result

            }







    # ==========================
    # Tools
    # ==========================


    action = choose_tool(
        command
    )


    if action:


        return {

            "type": "tool",

            "action": action

        }





    # ==========================
    # AI
    # ==========================


    reply = ask_nexa(
        command.normalized
    )


    return {

        "type": "ai",

        "message": reply

    }