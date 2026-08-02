from tools.app_tools import run as run_app

ALIASES = {
    "git hub": "github",
    "github.com": "github",
    "you tube": "youtube",
    "linked in": "linkedin",
    "chat gpt": "chatgpt",
}


def choose_tool(command):

    command = command.lower().strip()

    if command.startswith("search youtube for "):
        query = command.replace("search youtube for ", "")

        return {
            "type": "youtube",
            "query": query,
            "message": f"Searching YouTube for {query}."
        }

    if command.startswith("search google for "):
        query = command.replace("search google for ", "")

        return {
            "type": "google",
            "query": query,
            "message": f"Searching Google for {query}."
        }

    if command.startswith("open "):

        name = command.replace("open ", "").strip()
        name = ALIASES.get(name, name)

        return {
            "type": "website",
            "name": name,
            "message": f"Opening {name.title()}."
        }

    return None