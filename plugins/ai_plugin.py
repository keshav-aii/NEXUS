from core.command import Command
from ai.ollama_client import ask_ollama



PLUGIN_INFO = {

    "name": "ai",

    "priority": 1,

    "intents": [

        "ai"

    ],

    "keywords": []

}





def handle(command: Command):


    if command.intent != "ai":

        return None



    prompt = command.normalized



    response = ask_ollama(
        prompt
    )



    if not response:

        return {

            "action": "error",

            "message":
            "Sorry boss, AI response nahi aa paya."

        }



    return {

        "action": "ai",

        "message": response

    }