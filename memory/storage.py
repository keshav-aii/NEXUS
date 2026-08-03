import json
import os


MEMORY_FILE = os.path.join(
    "data",
    "memory.json"
)



def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {}


    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)




def save_memory(memory):

    os.makedirs(
        "data",
        exist_ok=True
    )


    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )




def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(
        memory
    )




def recall(key):

    memory = load_memory()

    return memory.get(
        key
    )




def get_all_memory():

    return load_memory()