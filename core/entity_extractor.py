from core.command import Command


ENTITY_MAP = {

    "downloads": [
        "download",
        "downloads",
    ],

    "desktop": [
        "desktop",
    ],

    "documents": [
        "document",
        "documents",
    ],

    "pictures": [
        "picture",
        "pictures",
        "photos",
    ],

    "music": [
        "music",
        "songs",
    ],
}


def extract_entities(command: Command) -> Command:
    """
    Extracts objects/targets from normalized command.
    Does not execute anything.
    """

    text = command.normalized

    entities = {}

    for entity, keywords in ENTITY_MAP.items():

        for keyword in keywords:

            if keyword in text:
                entities["target"] = entity
                break

        if "target" in entities:
            break

    command.entities = entities

    return command