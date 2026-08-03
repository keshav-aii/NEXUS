from core.command import Command
import re


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
    """

    text = command.normalized.lower()

    entities = {}


    # Known targets

    for entity, keywords in ENTITY_MAP.items():

        for keyword in keywords:

            if keyword in text:

                entities["target"] = entity
                break


        if "target" in entities:
            break



    # Create folder/file names

    if command.intent == "create":

        match = re.search(
            r"(folder|file)\s+(.+)",
            text
        )


        if match:

            entities["type"] = match.group(1)

            entities["name"] = (
                match.group(2)
                .strip()
            )


    command.entities = entities

    return command