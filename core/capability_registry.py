PLUGIN_MAP = {

    # ========= System =========

    "system": "system",

    # ========= Memory =========

    "memory": "memory",

    # ========= Coding =========

    "coding": "coding",

    # ========= Apps =========

    "open": "app",
    "close":"app",

    # ========= Files =========

    "create": "file",
    "delete": "file",


    "ai": "ai",

 
    "general": "general",

    # ========= Internet =========

    "search": "internet",
    "youtube": "internet"

    

}


def get_plugin(intent):

    return PLUGIN_MAP.get(intent)