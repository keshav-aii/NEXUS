from core.command import Command


from core.permanent_memory import (
    remember,
    recall,
    forget,
    load_memory
)



PLUGIN_INFO = {

    "name": "memory",

    "priority": 70,

    "intents": [

        "memory"

    ],

   

        "keywords": [

        "remember",
        "forget",
        "recall",
        "what do you remember",
        "what is my name",
        "whats my name",
        "what's my name",
        "my name"

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

            "action":

            "memory_saved",


            "item":

            "name"

        }





    # =========================
    # GENERAL REMEMBER
    #
    # Example:
    # remember my editor is vscode
    #
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


                "action":

                "memory_saved",


                "item":

                key.strip()

            }





    # =========================
    # ASK NAME
    # =========================


    if (

        "what is my name" in text

        or "whats my name" in text

        or "what's my name" in text

    ):



        name = recall(

            "my name"

        )



        if name:


            return {


                "action":

                "name_recall",


                "item":

                name

            }



        return {


            "action":

            "memory_empty"

        }





    # =========================
    # SHOW ALL MEMORY
    # =========================


    if (

        "what do you remember" in text

        or "show memory" in text

        or "show my memories" in text

    ):



        memories = load_memory()



        if not memories:


            return {


                "action":

                "memory_empty"

            }




        return {


            "action":

            "memory_list",


            "data":

            memories

        }





    # =========================
    # FORGET MEMORY
    # =========================


    if "forget" in text:



        key = text.replace(

            "forget",

            "",

            1

        ).strip()



        if forget(key):


            return {


                "action":

                "memory_forgotten",


                "item":

                key

            }



        return {


            "action":

            "memory_not_found"

        }





    return None