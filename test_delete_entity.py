from core.command import Command
from core.normalizer import normalize
from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities


cmd = Command("delete file notes.txt")


cmd = normalize(cmd)
cmd = detect_intent(cmd)
cmd = extract_entities(cmd)


print(cmd)
print("Entities:", cmd.entities)