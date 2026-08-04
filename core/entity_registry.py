import os
import importlib

ENTITY_FOLDER = "entities"


def load_entities():
    registry = {}

    if not os.path.exists(ENTITY_FOLDER):
        return registry

    for file in os.listdir(ENTITY_FOLDER):

        if not file.endswith(".py"):
            continue

        if file == "__init__.py":
            continue

        module = importlib.import_module(
            f"{ENTITY_FOLDER}.{file[:-3]}"
        )

        entity = getattr(module, "ENTITY", None)

        if entity:

            registry[entity["name"]] = entity

    return registry