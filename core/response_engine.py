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



        # ======================
        # DIRECT PLUGIN MESSAGE
        # PRIORITY 1
        # ======================

        if data.get(
            "message"
        ):

            return data["message"]




        # ======================
        # MESSAGE ENGINE
        # PRIORITY 2
        # ======================

        if action:


            return get_message(

                action,

                item=item,

                data=extra_data

            )



        return None





    # ======================
    # TOOL
    # ======================

    if result_type == "tool":


        action = result.get(
            "action"
        )


        if action:


            if isinstance(action, dict):

                return action.get(
                    "message"
                )


            return str(action)





    # ======================
    # AI
    # ======================

    if result_type == "ai":


        return result.get(
            "message"
        )





    # ======================
    # UNKNOWN
    # ======================

    if result_type == "unknown":


        return result.get(

            "message",

            "I did not understand that."

        )





    return None