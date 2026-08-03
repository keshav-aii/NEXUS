from core.command import Command

from memory.storage import (
    remember,
    recall,
    get_all_memory,
    save_memory,
)


PLUGIN_INFO = {

    "name": "memory",

    "priority": 50,

    "intents": [

        "memory"

    ]

}



def handle(command: Command):


    if command.intent != "memory":

        return None



    text = command.normalized.lower().strip()


    print(
        "MEMORY TEXT:",
        text
    )



    # =========================
    # REMEMBER NAME
    # =========================

    if (
        "remember my name is" in text
        or "remember that my name is" in text
    ):


        name = text.split(
            "name is",
            1
        )[1].strip()



        remember(
            "my name",
            name
        )



        return {

            "message":
            f"I will remember that your name is {name}."

        }





    # =========================
    # GENERAL REMEMBER
    # Example:
    # remember my editor is vscode
    # =========================


    if "remember" in text:


        data = text.replace(
            "remember",
            "",
            1
        ).strip()



        if " is " in data:


            key, value = data.split(
                " is ",
                1
            )


            remember(
                key.strip(),
                value.strip()
            )


            return {

                "message":
                f"I will remember that {key.strip()} is {value.strip()}."

            }




    # =========================
    # ASK NAME
    # =========================


    if (
        "what is my name" in text
        or "what's my name" in text
        or "whats my name" in text
    ):


        name = recall(
            "my name"
        )


        if name:


            return {

                "message":
                f"Your name is {name}."

            }


        return {

            "message":
            "I don't remember your name."

        }





    # =========================
    # SHOW ALL MEMORY
    # =========================


    if (
        "what do you remember" in text
        or "show memory" in text
        or "show my memories" in text
    ):


        memories = get_all_memory()



        if not memories:

            return {

                "message":
                "I don't remember anything yet."

            }



        result = ", ".join(

            [
                f"{key} is {value}"

                for key, value in memories.items()

            ]

        )



        return {

            "message":
            "I remember: " + result

        }





    # =========================
    # FORGET MEMORY
    # =========================


    if "forget" in text:


        key = text.replace(
            "forget",
            ""
        ).strip()



        memories = get_all_memory()



        if key in memories:


            del memories[key]


            save_memory(
                memories
            )


            return {

                "message":
                f"I forgot {key}."

            }



        return {

            "message":
            "I could not find that memory."

        }




    return None