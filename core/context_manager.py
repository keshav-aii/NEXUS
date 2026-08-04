CURRENT_CONTEXT = {


    "last_command": None,

    "last_intent": None,

    "last_target": None,

    "last_action": None

}





def update_context(command, result=None):


    if command:


        CURRENT_CONTEXT["last_command"] = (
            command.normalized
        )


        CURRENT_CONTEXT["last_intent"] = (
            command.intent
        )



        if command.entities:

            CURRENT_CONTEXT["last_target"] = (
                command.entities.get("target")
            )



    if result:


        if isinstance(result, dict):


            data = result.get(
                "data"
            )


            if isinstance(data, dict):


                CURRENT_CONTEXT["last_action"] = (
                    data.get("action")
                )




def get_context():

    return CURRENT_CONTEXT




def get_last_target():

    return CURRENT_CONTEXT.get(
        "last_target"
    )





def clear_context():

    global CURRENT_CONTEXT


    CURRENT_CONTEXT = {

        "last_command": None,

        "last_intent": None,

        "last_target": None,

        "last_action": None

    }