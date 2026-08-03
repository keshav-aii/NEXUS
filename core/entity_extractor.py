from core.command import Command



def extract_entities(command: Command):


    text = command.normalized.lower().strip()

    words = text.split()


    command.entities = {}



    # =====================
    # CREATE
    # =====================

    if command.intent == "create":


        if "file" in words:


            index = words.index("file")


            name = " ".join(
                words[index + 1:]
            )


            command.entities["type"] = "file"

            command.entities["name"] = name.strip()



        elif "folder" in words:


            index = words.index("folder")


            name = " ".join(
                words[index + 1:]
            )


            command.entities["type"] = "folder"

            command.entities["name"] = name.strip()





    # =====================
    # DELETE
    # =====================

    elif command.intent == "delete":


        if "file" in words:


            index = words.index("file")


            name = " ".join(
                words[index + 1:]
            )


            command.entities["type"] = "file"

            command.entities["name"] = name.strip()



        elif "folder" in words:


            index = words.index("folder")


            name = " ".join(
                words[index + 1:]
            )


            command.entities["type"] = "folder"

            command.entities["name"] = name.strip()





    # =====================
    # OPEN
    # =====================

    elif command.intent == "open":


        if len(words) > 1:


            command.entities["target"] = " ".join(
                words[1:]
            )



    return command