from brain.intent import detect_intent

ALIASES = {
    "git hub": "github",
    "github.com": "github",
    "you tube": "youtube",
    "linked in": "linkedin",
    "chat gpt": "chatgpt",
}


def choose_tool(command):

    data = detect_intent(command)

    intent = data["intent"]
    target = ALIASES.get(data["target"], data["target"])

    if intent == "open":

        return {
            "type": "website",
            "name": target,
            "message": f"Opening {target.title()}."
        }

    if intent == "google":

        return {
            "type": "google",
            "query": target,
            "message": f"Searching Google for {target}."
        }

    if intent == "youtube":

        return {
            "type": "youtube",
            "query": target,
            "message": f"Searching YouTube for {target}."
        }

    return None