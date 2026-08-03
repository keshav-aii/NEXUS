from core.command import Command



ALIASES = {

    "git hub": "github",
    "github.com": "github",

    "you tube": "youtube",

    "linked in": "linkedin",

    "chat gpt": "chatgpt",

}



def choose_tool(command: Command):


    intent = command.intent


    target = command.entities.get(
        "target",
        ""
    )


    target = ALIASES.get(
        target,
        target
    )



    if intent == "open":


        return {

            "type": "website",

            "name": target,

            "message":
            f"Opening {target.title()}."

        }



    if intent == "search":


        query = command.entities.get(
            "query",
            ""
        )


        return {

            "type": "google",

            "query": query,

            "message":
            f"Searching Google for {query}."

        }



    if intent == "youtube":


        query = command.entities.get(
            "query",
            ""
        )


        return {

            "type": "youtube",

            "query": query,

            "message":
            f"Searching YouTube for {query}."

        }



    return None