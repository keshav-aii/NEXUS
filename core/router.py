from brain.memory_manager import handle_memory
from tools.tool_manager import choose_tool
from brain.brain import ask_nexa
from core.plugin_loader import load_plugins
from core.normalizer import normalize
from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities
from brain.state_manager import (
    set_pending,
    get_pending,
    clear_pending
)


plugins = load_plugins()
pending_action = None


def process(command):
        # Check pending confirmation

    pending = get_pending()


    if pending:

        text = command.raw.lower().strip()


        if text in ["yes", "yes please", "confirm", "ok"]:

            clear_pending()


            result = pending["handler"](
                pending["command"]
            )


            return {
                "type": "plugin",
                "data": result
            }



        if text in ["no", "cancel", "stop"]:

            clear_pending()


            return {
                "type": "system",
                "message": "Cancelled."
            }
    global pending_action


    text = command.raw.lower().strip()


    if pending_action:

        if text in ["yes", "confirm", "ok"]:

            action = pending_action
            pending_action = None


            result = action["handler"](action["command"])


            return {
                "type": "plugin",
                "data": result
            }


        if text in ["no", "cancel"]:

            pending_action = None

            return {
                "type": "system",
                "message": "Cancelled."
            }

    """
    Central NEXUS command pipeline.
    """

    # 1. Normalize
    command = normalize(command)

    # 2. Detect Intent
    command = detect_intent(command)

    # 3. Extract Entities
    command = extract_entities(command)


    # 4. Memory
    memory_reply = handle_memory(command.normalized)

    if memory_reply:
        return {
            "type": "memory",
            "message": memory_reply
        }


    # 5. Plugins

        # 5. Plugins

    for plugin in plugins:

        plugin_intents = plugin["info"].get(
            "intents",
            []
        )

        if command.intent not in plugin_intents:
            continue

        if command.intent == "delete":

            pending_action = {
                "handler": plugin["handler"],
                "command": command
            }


            return {
                "type": "confirmation",
                "message":
                f"Do you want to delete {command.entities.get('name')}?"
            }

        if command.intent == "delete":

            set_pending({
                "handler": plugin["handler"],
                "command": command
            })


            return {
                "type": "confirmation",
                "message":
                f"Do you want to delete {command.entities.get('name')}?"
            }


        result = plugin["handler"](command)


        if result:

            return {
                "type": "plugin",
                "data": result
            }

    # 6. Tools

    action = choose_tool(command.normalized)

    if action:

        return {
            "type": "tool",
            "action": action
        }


    # 7. AI fallback

    reply = ask_nexa(command.normalized)

    return {
        "type": "ai",
        "message": reply
    }