from brain.memory import remember, recall


def handle_memory(command):

    command = command.lower().strip()

    # Remember my name is Keshav
    if command.startswith("remember my name is"):

        name = command.replace("remember my name is", "").strip()

        remember("name", name)

        return "Okay, I'll remember your name."

    # What's my name
    if "what's my name" in command or "what is my name" in command:

        name = recall("name")

        if name:
            return f"Your name is {name.title()}."

        return "I don't know your name yet."

    return None