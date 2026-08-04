from core.command import Command
from core.normalizer import normalize
from core.intent_engine import detect_intent
from core.plugin_loader import load_plugins


plugins = load_plugins()


cmd = Command(
    "lock computer"
)


# Pipeline

cmd = normalize(cmd)

cmd = detect_intent(cmd)


print(cmd)


# Plugin execute

for plugin in plugins:

    intents = plugin["info"].get(
        "intents",
        []
    )


    if cmd.intent in intents:

        result = plugin["handler"](cmd)

        print(result)

        break