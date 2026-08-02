from brain.brain import ask_nexa
from tools.tool_manager import choose_tool
from actions import execute
from voice.listener import listen
from voice.speaker import speak


def is_wake_word(text):
    wake_words = [
        "hey nexus",
        "nexus",
        "hey nexa",
        "nexa",
        "hey next us",
        "next us"
    ]

    return any(word in text for word in wake_words)


print("===================================")
print("        NEXUS AI Assistant")
print(" Say 'Hey Nexus' to activate")
print(" Say 'Exit' to quit")
print("===================================")


while True:

    # ---------- Sleep Mode ----------
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

    # ---------- Conversation Mode ----------
    while True:

        command = listen()

        if not command:
            speak("I didn't hear anything.")
            continue

        print("You:", command)

        if command in [
            "exit",
            "bye",
            "goodbye",
            "sleep",
            "go to sleep",
            "no",
            "nothing",
            "that's all",
        ]:
            speak("Okay. Going back to sleep.")
            break

        action = choose_tool(command)

        if action:

            speak(action["message"])

            execute(action)

            speak("Anything else?")

            continue

        reply = ask_nexa(command)

        speak(reply)

        speak("Anything else?")