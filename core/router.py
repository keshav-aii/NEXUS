from brain.memory_manager import handle_memory
from tools.tool_manager import choose_tool
from brain.brain import ask_nexa

from core.plugin_loader import load_plugins
from core.normalizer import normalize
from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities


plugins = load_plugins()


def process(command):

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