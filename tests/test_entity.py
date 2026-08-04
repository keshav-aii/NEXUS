import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.command import Command
from core.entity_extractor import extract_entities

cmd = Command("open chrome")

cmd.intent = "open"
cmd.normalized = "open chrome"

cmd = extract_entities(cmd)

print(cmd.entities)