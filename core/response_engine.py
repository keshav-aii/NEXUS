from core.message_engine import get_message



def generate_response(result):


    if not result:

        return None



    result_type = result.get(
        "type"
    )



    # ======================
    # CONFIRMATION
    # ======================

    if result_type == "confirmation":


        command = result.get(
            "command"
        )


        item = "file"


        if command:

            item = command.entities.get(
                "name",
                "file"
            )



        return get_message(

            "delete_confirm",

            item=item

        )





    # ======================
    # PLUGIN RESPONSE
    # ======================

    if result_type == "plugin":


        data = result.get(
            "data"
        )


        if not isinstance(data, dict):

            return str(data)



        action = data.get(
            "action"
        )



        item = data.get(
            "item",
            ""
        )



        extra_data = data.get(
            "data",
            {}
        )



        # normal action

        if action:


            return get_message(

                action,

                item=item,

                data=extra_data

            )



        # fallback old plugins

        if data.get(
            "message"
        ):

            return data["message"]






    # ======================
    # TOOL
    # ======================

    if result_type == "tool":


        action = result.get(
            "action"
        )


        if action:

            return action.get(
                "message"
            )






    # ======================
    # AI
    # ======================

    if result_type == "ai":


        return result.get(
            "message"
        )




    return None