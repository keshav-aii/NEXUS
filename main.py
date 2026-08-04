from core.personality import respond
from memory.storage import get_user_name
from core.response_engine import generate_response
from config.wakewords import WAKE_WORDS
from voice.listener import listen
from voice.speaker import speak
import string
import time
from rapidfuzz import fuzz
from config.settings import SLEEP_TIMEOUT
from core.command import Command
from core.router import process
from logs.logger import info, error
from actions import execute






# ==========================
# WAKE HELPERS
# ==========================

def is_wake_word(text):

    for word in WAKE_WORDS:

        score = fuzz.partial_ratio(
            text,
            word
        )

        if score >= 70:

            return True


    return False



def remove_wake_word(text):

    for word in sorted(
        WAKE_WORDS,
        key=len,
        reverse=True
    ):

        if word in text:

            text = text.replace(
                word,
                ""
            )

            break


    # remove punctuation

    text = text.replace(
        ".",
        ""
    )

    text = text.replace(
        ",",
        ""
    )

    return text.strip()

# ==========================
# RESPONSE HANDLER
# ==========================

def speak_result(result):


    if not result:

        return



    message = generate_response(
        result
    )


    if message:

        speak(
            message
        )

        return



    if isinstance(result, str):

        speak(result)

        return




    if result.get("type") == "plugin":


        data = result.get(
            "data"
        )


        if isinstance(data, dict):

            if data.get("message"):

                speak(
                    data["message"]
                )


        return





    if result.get("message"):

        speak(
            result["message"]
        )





# ==========================
# START
# ==========================

print("==============================")
print("       NEXUS AI Assistant")
print(" Say Hey Nexus")
print(" Say Exit")
print("==============================")



conversation_mode = False

waiting_confirmation = False

pending_command = None


last_command_time = time.time()








# ==========================
# MAIN LOOP
# ==========================

while True:



    # AUTO SLEEP

    if conversation_mode:


        if time.time() - last_command_time > SLEEP_TIMEOUT:


            conversation_mode = False


            print(
                "NEXUS: Sleeping..."
            )





    text = listen()



    if not text:

        continue




    text = text.lower().strip()

    text = text.translate(
    str.maketrans(
        "",
        "",
        string.punctuation
    )
)


    print(
        "You:",
        text
    )

    info(
        f"USER: {text}"
    )


    last_command_time = time.time()





    # ======================
    # EXIT
    # ======================


    if "exit" in text:

        speak(
            "Radhe Radhe"
        )

        break




    # ======================
    # WAKE HANDLING
    # ======================


    if is_wake_word(text):


        cleaned = remove_wake_word(
            text
        )



        # only wake word


        if not cleaned:


            conversation_mode = True


            name = get_user_name()


            speak(
                respond(
                    "wake",
                    name
                )
            )


            continue




        # wake + command


        else:


            conversation_mode = True


            text = cleaned


            print(
                "COMMAND AFTER WAKE:",
                text
            )






    # ======================
    # IGNORE SLEEPING
    # ======================


    if not conversation_mode:


        continue





    # ======================
    # PROCESS COMMAND
    # ======================


    print(
        "FINAL TEXT:",
        repr(text)
    )

    info(
    f"COMMAND: {text}"
    )
 


    cmd = Command(
        text
    )



    result = process(
        cmd
    )



    print(
        "RESULT:",
        result
    )

    info(
    f"RESULT: {result}"
    )



    if result:


        speak_result(
            result
        )



    last_command_time = time.time()