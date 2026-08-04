import requests


from core.conversation_memory import (
    add_message,
    get_history
)



OLLAMA_URL = "http://localhost:11434/api/generate"


MODEL = "qwen3:latest"



PERSONALITY = """
You are NEXA, a personal AI assistant.

Rules:
- Talk like a friendly Indian AI assistant.
- Call the user "boss" naturally.
- Prefer Hinglish.
- Keep voice responses short and natural.
- Keep answers under 3-5 sentences for voice responses.
- Speak naturally like a personal assistant.
- Avoid emojis.
- Do not use markdown unless asked.
- Do not say you are ChatGPT.
- Your name is NEXA.
"""





def ask_ollama(prompt):


    try:


        # =========================
        # GET OLD CONVERSATION
        # =========================

        history = get_history()



        conversation = ""



        for msg in history:


            conversation += (

                msg["role"]
                +
                ": "
                +
                msg["content"]
                +
                "\n"

            )





        # =========================
        # SEND TO OLLAMA
        # =========================


        response = requests.post(

            OLLAMA_URL,


            json={


                "model": MODEL,


                "prompt":

                    PERSONALITY

                    +

                    "\nConversation:\n"

                    +

                    conversation

                    +

                    "\nUser: "

                    +

                    prompt,



                "stream": False


            },


            timeout=60


        )





        data = response.json()



        answer = data.get(

            "response",

            ""

        )






        # =========================
        # SAVE MEMORY
        # =========================


        add_message(

            "user",

            prompt

        )



        add_message(

            "assistant",

            answer

        )





        return answer







    except Exception as e:


        print(

            "OLLAMA ERROR:",

            e

        )


        return None