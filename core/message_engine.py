from core.response_provider import respond


ACTION_MAP = {

    "app_opened":
    "open",

    "browser_opened":
    "browser_opened",

    "app_closed":
    "close",

    "app_not_running":
    "app_not_running",

    "app_close_failed":
    "error",

    "file_created":
    "file_created",

    "folder_created":
    "folder_created",

    "delete_success":
    "delete_success",

    "error":
    "error"

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