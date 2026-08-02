from brain.brain import ask_nexa
from tools.tool_manager import choose_tool
from tools.browser_tools import search_google, search_youtube
from voice.listener import listen
from voice.speaker import speak
from actions import execute
import time


def is_wake_word(text):

    wake_words = [
        "hey nexus",
        "nexus",
        "hey nexa",
        "nexa",
    ]

    return any(word in text for word in wake_words)


print("===================================")
print("        NEXUS AI Assistant")
print(" Say 'Hey Nexus' to activate")
print(" Say 'Exit' to quit")
print("===================================")


while True:

    text = listen()

    if not text:
        continue

    print("You:", text)

    if text == "exit":
        speak("Goodbye!")
        break

    if not is_wake_word(text):
        continue

    speak("Yes?")

    command = listen()

    if not command:
        speak("I didn't hear anything.")
        continue

    print("You:", command)

    if command == "exit":
        speak("Goodbye!")
        break

    action = choose_tool(command)

    if action:

       print("DEBUG: Action =", action)

       print("DEBUG: Before speak")
       speak(action["message"])
       print("DEBUG: After speak")

       import time
       time.sleep(2)

       execute(action)

       continue

    reply = ask_nexa(command)

    speak(reply)