from voice.listener import listen
from voice.speaker import speak

from core.command import Command
from core.router import process

from actions import execute



def extract_command(text):

    text = text.lower().strip()


    print("BEFORE WAKE REMOVE:", text)


    wake_words = [

        "hey nexus",
        "hey nexa",
        "hey nexta",

        "nexus",
        "nexa",
        "nexta",

        "nexas",
        "nexus ai",

        "hey alexa",
        "alexa"

    ]


    for word in wake_words:

        if word in text:

            text = text.replace(
                word,
                ""
            )

            print("AFTER WAKE REMOVE:", text.strip())

            return text.strip()


    return None



print("===================================")
print("          NEXUS AI Assistant")
print(" Say 'Hey Nexus' to activate")
print(" Say 'Exit' to quit")
print("===================================")



awake_mode = False

waiting_confirmation = False

pending_command = None



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


        command_text = extract_command(
            text
        )


        if command_text is None:

            continue



        awake_mode = True


        speak(
            "Yes?"
        )


        if command_text:

            text = command_text


        else:

            continue




    # ==========================
    # CONFIRMATION
    # ==========================

    if waiting_confirmation:


        if text in [

            "yes",
            "yeah",
            "yep",
            "confirm",
            "ok",
            "okay",
            "haan",
            "ha",
            "kar do",
            "do it"

        ]:


            waiting_confirmation = False



            if pending_command:


                result = process(
                    pending_command
                )


        elif text in [

            "no",
            "cancel",
            "stop",
            "nahi",
            "mat karo"

        ]:


            waiting_confirmation = False

            pending_command = None


            speak(
                "Cancelled."
            )


            continue



        else:


            speak(
                "Please say yes or no."
            )


            continue


    # Remove wake word if assistant already awake

    wake_removed = extract_command(text)


    if wake_removed is not None:

        if wake_removed:

            text = wake_removed

            

    # ==========================
    # PROCESS COMMAND
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
    # CONFIRMATION REQUEST
    # ==========================

    if result["type"] == "confirmation":


        waiting_confirmation = True


        pending_command = cmd


        speak(
            result["message"]
        )


        continue




    # ==========================
    # PLUGIN RESULT
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
    # TOOL RESULT
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