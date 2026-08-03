from voice.listener import listen
from voice.speaker import speak
from core.command import Command
from core.router import process
from actions import execute

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

    # Wake Mode
    text = listen()

    if not text:
        continue

    print(f"You: {text}")

    if text == "exit":
        speak("Radhe Radhe")
        break

    if not is_wake_word(text):
        continue

    speak("Yes?")

    time.sleep(0.3)

    # Command Mode
    command = listen()

    if not command:
        speak("I didn't hear anything.")
        continue

    print(f"You: {command}")

    if command == "exit":
        speak("Goodbye!")
        break

    # Process command
    cmd = Command(command)

    result = process(cmd)

    if not result:
        continue

    # ==========================
    # MEMORY
    # ==========================

    if result["type"] == "memory":

        speak(result["message"])

        continue



    if result["type"] == "system":

        speak(result["message"])

        continue



    if result["type"] == "confirmation":

        speak(result["message"])

        continue

    # ==========================
    # CONFIRMATION
    # ==========================

    if result["type"] == "confirmation":

        speak(result["message"])

        continue
   
   
  

   # ==========================
     #  PLUGINS
# ==========================

    if result["type"] == "plugin":

        if "ollama" in result["data"]:
             speak(result["data"]["ollama"])

        if "message" in result["data"]:
            speak(result["data"]["message"])

        continue
    # ==========================
    # TOOLS
    # ==========================

    if result["type"] == "tool":

        action = result["action"]

        speak(action["message"])

        execute(action)

        speak("Anything else?")

        continue

    # ==========================
    # AI
    # ==========================

    if result["type"] == "ai":

        speak(result["message"])

        speak("Anything else?")