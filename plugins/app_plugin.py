from core.command import Command
import string

from automation.resolver import resolve_open, resolve_close

PLUGIN_INFO = {
    "name": "app",
    "priority": 50,
    "intents": ["open", "close"],
    "keywords": [
        "open",
        "launch",
        "start",
        "close",
        "quit",
        "exit",
        "stop",
        "terminate",
        "dismiss",
    ],
}


def handle(command: Command):

    text = command.normalized.lower().strip()

    # ==========================
    # CLOSE
    # ==========================

    if command.intent == "close":

        target = command.entities.get("target")

        if not target:
            return None

        result = resolve_close(target)

        print("CLOSE RESULT:", result)

        if result.get("success"):

            return {"action": "app_closed", "item": target}

        if result.get("reason") == "not_running":

            return {"action": "app_not_running", "item": target}

        return {"action": "app_close_failed", "item": target}

    # ==========================
    # OPEN
    # ==========================

    if command.intent != "open":
        return None

    # ==========================
    # FIRST USE ENTITY
    # ==========================

    target = command.entities.get("target")

    # ==========================
    # FALLBACK
    # ==========================

    if not target:

        words = text.split()

        if "open" not in words:
            return None

        index = words.index("open")

        target = " ".join(words[index + 1 :])

        target = target.translate(str.maketrans("", "", string.punctuation))

    if not target:
        return None

    # ==========================
    # RESOLVE
    # ==========================

    result = resolve_open(target)

    print("APP RESULT:", result)

    # ==========================
    # FAILED
    # ==========================

    if not result.get("success"):

        return {"action": "app_failed", "item": target}

    # ==========================


    # WEBSITE
    # ==========================

    if result.get("type") == "website":

        return {"action": "browser_opened", "item": target}

    # ==========================
    # APP ALREADY RUNNING
    # ==========================

    if result.get("action") == "app_focused":

        return {"action": "app_focused", "item": target}

    # ==========================
    # APPLICATION OPENED
    # ==========================

    if result.get("type") == "app":

        return {"action": "app_opened", "item": target}
    # ==========================
    # UNKNOWN
    # ==========================

    return {"action": "app_failed", "item": target}
