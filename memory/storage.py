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
            indent=4,
            ensure_ascii=False
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




# ==========================
# USER PROFILE
# ==========================

def get_user_name():

    memory = load_memory()


    # direct name key
    if "name" in memory:

        return memory["name"]



    # profile based memory support
    if "profile" in memory:

        return memory["profile"].get(
            "name"
        )


    return None