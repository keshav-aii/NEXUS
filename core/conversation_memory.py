from collections import deque


# Last 10 messages store karega

HISTORY = deque(
    maxlen=10
)



def add_message(role, content):

    HISTORY.append({

        "role": role,

        "content": content

    })




def get_history():

    return list(HISTORY)




def clear_history():

    HISTORY.clear()