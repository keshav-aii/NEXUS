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


    pending = get_pending()


    if pending:


        text = command.raw.lower().strip()



    if text in [

        "yes",
        "yes please",
        "yeah",
        "yep",
        "confirm",
        "confirmed",
        "ok",
        "okay",
         "do it",
         "go ahead",
        "proceed",
        "haan",
        "ha",
         "kar do"

    ]:


            clear_pending()


            result = pending["handler"](
                pending["command"]
            )


            return {

                "type": "plugin",

                "data": result

            }



        if text in [
             "no",
        "cancel",
         "stop",
         "don't",
          "dont",
        "nahi",
         "mat karo"
        ]:


            clear_pending()


            return {

                "type": "system",

                "message": "Cancelled."

            }




    command = normalize(command)


    command = detect_intent(command)


    command = extract_entities(command)



    memory_reply = handle_memory(
        command.normalized
    )


    if memory_reply:


        return {

            "type": "memory",

            "message": memory_reply

        }




    for plugin in plugins:


        plugin_intents = plugin["info"].get(
            "intents",
            []
        )


        if command.intent not in plugin_intents:

            continue



        if command.intent == "delete":


            name = command.entities.get(
                "name"
            )


            if not name:


                return {

                    "type": "system",

                    "message":
                    "Please tell me the file or folder name."

                }



            set_pending({

                "handler": plugin["handler"],

                "command": command

            })


            return {

                "type": "confirmation",

                "message":
                f"Do you want to delete {name}?"

            }



        result = plugin["handler"](command)



        if result:


            return {

                "type": "plugin",

                "data": result

            }





    action = choose_tool(command)


    if action:


        return {

            "type": "tool",

            "action": action

        }




    reply = ask_nexa(
        command.normalized
    )


    return {

        "type": "ai",

        "message": reply

    }