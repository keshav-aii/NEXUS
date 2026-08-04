PLUGIN_MAP = {

    # ========= System =========

    "system": "system",

    # ========= Memory =========

    "memory": "memory",

    # ========= Coding =========

    "coding": "coding",

    # ========= Apps =========

    "open": "app",

    # ========= Files =========

    "create": "file",
    "delete": "file",

    # ========= Internet =========

    "search": "internet",
    "youtube": "internet"

}


def get_plugin(intent):

    return PLUGIN_MAP.get(intent)