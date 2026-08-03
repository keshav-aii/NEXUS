from core.command import Command
from core.normalizer import normalize
from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities
from core.plugin_loader import load_plugins


plugins = load_plugins()


cmd = Command("create file notes.txt")


cmd = normalize(cmd)
cmd = detect_intent(cmd)
cmd = extract_entities(cmd)


print(cmd)


for plugin in plugins:

    result = plugin["handler"](cmd)

    if result:
        print(result)
        break
    