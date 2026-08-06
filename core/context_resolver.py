from core.context_manager import get_last_target
import re



CONTEXT_WORDS = [

    "it",
    "this",
    "that"

]



CONTEXT_ACTIONS = [

    "open",
    "close",
    "launch",
    "start",
    "quit",
    "delete",
    "remove"

]



def resolve_context(command):


    text = command.normalized.lower()



    if not command.entities:

        command.entities = {}



    # ==========================
    # APP COMMANDS
    # DO NOT APPLY CONTEXT
    # ==========================

    if command.intent in [

        "open",
        "close"

    ]:

        return command





    # ==========================
    # CHECK ACTION
    # ==========================


    has_action = False


    for action in CONTEXT_ACTIONS:

        if re.search(

            rf"\b{action}\b",

            text

        ):

            has_action = True

            break




    # no action = no context

    if not has_action:

        return command





    # ==========================
    # RESOLVE PRONOUNS
    # ==========================


    for word in CONTEXT_WORDS:


        if re.search(

            rf"\b{word}\b",

            text

        ):



            target = get_last_target()



            if target:


                command.entities["target"] = target



                if command.intent is None:


                    if "close" in text:

                        command.intent = "close"



                print(

                    "CONTEXT RESOLVED:",

                    word,

                    "=>",

                    target

                )





    return command