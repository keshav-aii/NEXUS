from voice.listener import listen
from voice.speaker import speak
import time
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




    elif result_type == "tool":

        action = result.get("action")


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



    elif result_type == "ai":

        speak(
            result.get(
                "message",
                ""
            )
        )



    elif result.get("message"):

        speak(
            result["message"]
        )






print("===================================")
print("          NEXUS AI Assistant")
print(" Say 'Hey Nexus' to activate")
print(" Say 'Exit' to quit")
print("===================================")



awake_mode = False

# NEW
conversation_mode = False
last_command_time = time.time()

SLEEP_TIMEOUT = 120   # 5 minutes

waiting_confirmation = False

pending_command = None





while True:

    # ==========================
# AUTO SLEEP CHECK
# ==========================

    if conversation_mode:

        if time.time() - last_command_time > SLEEP_TIMEOUT:


            conversation_mode = False

            awake_mode = False


            print(
                "NEXUS: Sleeping..."
            )


    text = listen()



    if not text:

        continue



    text = text.lower().strip()
    last_command_time = time.time()



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






    # =========================
    # WAKE SYSTEM
    # =========================


    if not conversation_mode:


        command_text = remove_wake_word(
            text
        )


        if command_text is None:

            continue



        conversation_mode = True


        speak(
            "Yes?"
        )



        if command_text:

            text = command_text


        else:

            continue







    # =========================
    # CONFIRMATION
    # =========================


    if waiting_confirmation:


        yes_words = [

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

        ]



        no_words = [

            "no",
            "cancel",
            "stop",
            "nahi"

        ]




        if text in yes_words:


            waiting_confirmation = False



            if pending_command:


                pending_command.context[
                    "confirmed"
                ] = True



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



            continue





        elif text in no_words:


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








    # =========================
    # COMMAND PROCESS
    # =========================



    print(
        "FINAL TEXT:",
        repr(text)
    )



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

        continue






    # =========================
    # DELETE CONFIRM
    # =========================


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







    # =========================
    # NORMAL
    # =========================


    speak_result(
        result
    )
    last_command_time = time.time()