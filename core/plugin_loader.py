import os
import importlib

PLUGIN_FOLDER = "plugins"


def load_plugins():
    plugins = []

    for file in os.listdir(PLUGIN_FOLDER):

        if not file.endswith(".py"):
            continue

        if file == "__init__.py":
            continue

        module_name = f"{PLUGIN_FOLDER}.{file[:-3]}"

        try:
            module = importlib.import_module(module_name)

            if hasattr(module, "handle"):
                plugins.append(module.handle)
                print(f"Loaded: {module_name}")

        except Exception as e:
            print(f"Failed to load {module_name}: {e}")

    return plugins