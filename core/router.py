from brain.memory_manager import handle_memory
from tools.tool_manager import choose_tool
from brain.brain import ask_nexa
from plugins.coding_plugin import handle as coding_plugin


def process(command):
    """
    Central router for every command.
    """

    # 1. Memory
    memory_reply = handle_memory(command)

    if memory_reply:
        return {
            "type": "memory",
            "message": memory_reply
        }

    # 2. Coding Plugin
    coding = coding_plugin(command)

    if coding:
        return {
            "type": "coding",
            "data": coding
        }

    # 3. Tools
    action = choose_tool(command)

    if action:
        return {
            "type": "tool",
            "action": action
        }

    # 4. AI
    reply = ask_nexa(command)

    return {
        "type": "ai",
        "message": reply
    }