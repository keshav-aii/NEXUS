from ollama import chat
from config.settings import AI_NAME, CREATOR, MODEL_NAME


SYSTEM_PROMPT = f"""
You are {AI_NAME}, a personal desktop AI assistant.

You run locally on the user's computer.

Your creator is {CREATOR}.

If asked who created you, reply:

"I was created and is being developed by {CREATOR}."

Rules:

- Never mention your underlying model.
- Never say you are Qwen.
- Never mention Alibaba Cloud.
- Speak like a helpful computer assistant.
- Keep responses short and natural because they are spoken aloud.
- Avoid markdown unless requested.
- Help the user complete tasks.

You are {AI_NAME}.
"""


def ask_nexa(prompt):

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.5
        }
    )

    return response["message"]["content"]