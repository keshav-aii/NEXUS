import os
import importlib

PLUGIN_FOLDER = "plugins"


def load_plugins():
    plugins = []

    for file in os.listdir(PLUGIN_FOLDER):

        if file.endswith(".py") and file != "__init__.py":

            module_name = f"{PLUGIN_FOLDER}.{file[:-3]}"

            module = importlib.import_module(module_name)

            if hasattr(module, "handle"):
                plugins.append(module.handle)

    return plugins