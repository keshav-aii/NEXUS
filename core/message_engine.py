from core.personality import respond


ACTION_MAP = {

    "app_opened": "open",

    "app_closed": "close",

    "file_created": "file_created",

    "folder_created": "folder_created",

    "delete_success": "delete_success",

    "error": "error"

}



def get_message(action, item="", data=None):


    action = ACTION_MAP.get(
        action,
        action
    )


    return respond(
        action,
        item=item,
        data=data
    )