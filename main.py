from core.personality import respond
from memory.storage import get_user_name
from core.response_engine import generate_response
from voice.listener import listen
from voice.speaker import speak

import time

from core.command import Command
from core.router import process

from actions import execute



# ==========================
# WAKE WORDS
# ==========================

WAKE_WORDS = [

    "nexus",
    "hey nexus",

    "nexa",
    "hey nexa",

    "nexta",
    "hey nexta",

    "alexa",
    "hey alexa",

    "nex",
    "hey nex"

]



# ==========================
# HELPERS
# ==========================


def speak_result(result):


    message = generate_response(
        result
    )


    if message:

        speak(
            message
        )


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





# ==========================
# START
# ==========================


print("===================================")
print("          NEXUS AI Assistant")
print(" Say 'Hey Nexus' to activate")
print(" Say 'Exit' to quit")
print("===================================")



awake_mode = False

conversation_mode = False

waiting_confirmation = False


pending_command = None


last_command_time = time.time()


SLEEP_TIMEOUT = 120




# ==========================
# MAIN LOOP
# ==========================


while True:



    # ==========================
    # AUTO SLEEP
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



    print(
        "You:",
        text
    )



    last_command_time = time.time()



    # ==========================
    # EXIT
    # ==========================


    if text == "exit":


        speak(
            "Radhe Radhe"
        )


        break





    # ==========================
    # WAKE / ATTENTION
    # ==========================


    if text in WAKE_WORDS:


        name = get_user_name()



        if conversation_mode:


            speak(
                respond(
                    "attention",
                    name
                )
            )


        else:


            conversation_mode = True

            awake_mode = True


            speak(
                respond(
                    "wake",
                    name
                )
            )



        last_command_time = time.time()


        continue





    # ==========================
    # IGNORE WHEN SLEEPING
    # ==========================


    if not conversation_mode:


        continue





    # ==========================
    # CONFIRMATION
    # ==========================


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






    # ==========================
    # PROCESS COMMAND
    # ==========================


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





    # ==========================
    # DELETE CONFIRMATION
    # ==========================


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






    # ==========================
    # NORMAL RESPONSE
    # ==========================


    speak_result(
        result
    )



    last_command_time = time.time()