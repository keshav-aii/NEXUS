from voice.listener import listen
from voice.speaker import speak
import time
from core.command import Command
from core.router import process

from actions import execute



def is_wake_word(text):

    wake_words = [

        "hey nexus",
        "nexus",

        "hey nexa",
        "nexa",

        "hey nexta",
        "nexta"

    ]


    return any(
        word in text.lower()
        for word in wake_words
    )



print("===================================")
print("        NEXUS AI Assistant")
print(" Say 'Hey Nexus' to activate")
print(" Say 'Exit' to quit")
print("===================================")



awake_mode = False



while True:


    text = listen()



    if not text:

        continue



    text = text.lower().strip()



    print(
        f"You: {text}"
    )



    # ==========================
    # EXIT
    # ==========================

    if text == "exit":


        speak(
            "Radhe Radhe"
        )


        break




    # ==========================
    # WAKE WORD
    # ==========================


    if not awake_mode:


        if is_wake_word(text):


            awake_mode = True


            speak(
                "Yes?"
            )


        continue





    # ==========================
    # COMMAND PROCESSING
    # ==========================


    cmd = Command(
        text
    )



    result = process(
        cmd
    )



    if not result:

        continue





    # ==========================
    # MEMORY
    # ==========================


    if result["type"] == "memory":


        speak(
            result["message"]
        )


        continue





    # ==========================
    # CONFIRMATION
    # ==========================


    if result["type"] == "confirmation":


        speak(
            result["message"]
        )
        time.sleep(1)


        continue





    # ==========================
    # PLUGIN
    # ==========================


    if result["type"] == "plugin":


        data = result["data"]



        if isinstance(data, dict):


            if "message" in data:


                speak(
                    data["message"]
                )


            elif "ollama" in data:


                speak(
                    data["ollama"]
                )


        else:


            speak(
                str(data)
            )



        continue





    # ==========================
    # TOOLS
    # ==========================


    if result["type"] == "tool":


        action = result["action"]



        speak(
            action["message"]
        )



        execute(
            action
        )



        speak(
            "Anything else?"
        )


        continue





    # ==========================
    # AI FALLBACK
    # ==========================


    if result["type"] == "ai":


        speak(
            result["message"]
        )


        speak(
            "Anything else?"
        )