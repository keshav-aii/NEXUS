from voice.listener import listen
from voice.speaker import speak

from core.command import Command
from core.router import process

from actions import execute



def remove_wake_word(text):

    text = text.lower().strip()


    wake_words = [

        "hey nexus",
        "hey nexa",
        "hey nexta",

        "nexus",
        "nexa",
        "nexta",

        "hey alexa",
        "alexa"

    ]


    for word in wake_words:


        if text.startswith(word):


            return text[len(word):].strip()



    return None





def speak_result(result):


    if not result:

        return



    if isinstance(result, str):

        speak(result)

        return



    if not isinstance(result, dict):

        speak(str(result))

        return



    result_type = result.get("type")



    # plugin response

    if result_type == "plugin":


        data = result.get("data")


        if isinstance(data, dict):


            if data.get("message"):

                speak(
                    data["message"]
                )


            elif data.get("ollama"):

                speak(
                    data["ollama"]
                )


        else:

            speak(
                str(data)
            )



    # tool response

    elif result_type == "tool":


        action = result.get(
            "action"
        )


        if action:


            speak(
                action.get(
                    "message",
                    ""
                )
            )


            execute(
                action
            )



    # ai

    elif result_type == "ai":


        speak(
            result.get(
                "message",
                ""
            )
        )



    # memory

    elif result_type == "memory":


        speak(
            result.get(
                "message",
                ""
            )
        )



    else:


        if result.get("message"):

            speak(
                result["message"]
            )







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
        "You:",
        text
    )




    # EXIT

    if text == "exit":


        speak(
            "Radhe Radhe"
        )


        break






    # =====================
    # WAKE WORD
    # =====================


    if not awake_mode:


        command_text = remove_wake_word(
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






    # =====================
    # CONFIRMATION
    # =====================


    if waiting_confirmation:


        if text in [


            "yes",
            "yeah",
            "yep",
            "confirm",
            "confirmed",
            "ok",
            "okay",
            "haan",
            "ha",
             "kar do",
            "delete it",
            "do it",
            "go ahead",
            "proceed",
            "sure"
        ]:


            waiting_confirmation = False



        if pending_command:


            pending_command.context["confirmed"] = True


            result = process(
            pending_command
            )


            print(
                "CONFIRM RESULT:",
                result
            )



            speak_result(
                result
            )



            pending_command = None



            awake_mode = False


            continue






        elif text in [


            "no",
            "cancel",
            "stop",
            "nahi"

        ]:


            waiting_confirmation = False

            pending_command = None


            speak(
                "Cancelled."
            )


            awake_mode = False


            continue






        else:


            speak(
                "Please say yes or no."
            )


            continue







    # =====================
    # PROCESS COMMAND
    # =====================

    print("FINAL TEXT BEFORE COMMAND:", repr(text))

    cmd = Command(
        text
    )



    result = process(
        cmd
    )



    print(
        "MAIN RESULT:",
        result
    )



    if not result:


        awake_mode = False

        continue





    # =====================
    # CONFIRMATION REQUEST
    # =====================


    if result.get("type") == "confirmation":


        waiting_confirmation = True


        pending_command = result.get(
            "command"
        )


        speak(
            result.get(
                "message",
                ""
            )
        )


        continue






    # NORMAL RESPONSE


    speak_result(
        result
    )


    awake_mode = False