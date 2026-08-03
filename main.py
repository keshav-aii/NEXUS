from brain.brain import ask_nexa
from brain.memory_manager import handle_memory

from tools.tool_manager import choose_tool
from actions import execute

from voice.listener import listen
from voice.speaker import speak

import time


def is_wake_word(text):

    wake_words = [
        "hey nexus",
        "nexus",
        "hey nexa",
        "nexa",
        "hey nexta",
        "nexta"
    ]

    return any(word in text for word in wake_words)


print("===================================")
print("        NEXUS AI Assistant")
print(" Say 'Hey Nexus' to activate")
print(" Say 'Exit' to quit")
print("===================================")


while True:

    # -------- Wake Mode --------

    text = listen()

    if not text:
        continue

    print(f"You: {text}")

    if text == "exit":
        speak("Goodbye!")
        break

    if not is_wake_word(text):
        continue

    speak("Yes?")

    time.sleep(0.3)

    # -------- Command Mode --------

    command = listen()

    if not command:
        speak("I didn't hear anything.")
        continue

    print(f"You: {command}")

    if command == "exit":
        speak("Goodbye!")
        break

    # -------- Memory --------

    memory_reply = handle_memory(command)

    if memory_reply:
        speak(memory_reply)
        continue

    # -------- Tools --------

    action = choose_tool(command)

    if action:

        print("DEBUG:", action)

        speak(action["message"])

        execute(action)

        speak("Anything else?")

        continue

    # -------- AI --------

    reply = ask_nexa(command)

    speak(reply)

    speak("Anything else?")