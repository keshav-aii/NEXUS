from core.personality import respond


def get_message(action, name=None, **kwargs):

    return respond(
        action,
        name,
        **kwargs
    )