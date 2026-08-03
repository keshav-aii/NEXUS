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




TARGETS = [

    "chrome",
    "youtube",
    "github",
    "linkedin",
    "chatgpt",
    "google",

    "calculator",
    "notepad",
    "paint",

]





def extract_entities(command: Command) -> Command:


    text = command.normalized.lower()


    entities = {}




    # ==========================
    # Folder / Locations
    # ==========================


    for entity, keywords in ENTITY_MAP.items():


        for keyword in keywords:


            if keyword in text:


                entities["target"] = entity

                break



        if "target" in entities:

            break





    # ==========================
    # Apps / Websites
    # ==========================


    if "target" not in entities:


        for target in TARGETS:


            if target in text:


                entities["target"] = target

                break





    # ==========================
    # Create / Delete
    # ==========================


    if command.intent in [

        "create",
        "delete"

    ]:


        words = text.split()



        if "folder" in words:


            index = words.index(
                "folder"
            )


            name = " ".join(
                words[index + 1:]
            )


            entities["type"] = "folder"

            entities["name"] = name





        elif "file" in words:


            index = words.index(
                "file"
            )


            name = " ".join(
                words[index + 1:]
            )


            entities["type"] = "file"

            entities["name"] = name





    # ==========================
    # Search / Youtube Query
    # ==========================


    if command.intent in [

        "search",
        "youtube"

    ]:


        query = text


        remove_words = [

            "search",
            "youtube",
            "you",
            "tube",
            "google",
            "on",

        ]


        words = query.split()



        words = [

            word

            for word in words

            if word not in remove_words

        ]



        query = " ".join(
            words
        ).strip()



        if query:


            entities["query"] = query





    command.entities = entities


    return command