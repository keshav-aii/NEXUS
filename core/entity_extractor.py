from rapidfuzz import fuzz

from core.entity_registry import load_entities

ENTITY_REGISTRY = load_entities()

IGNORE_WORDS = {
    "a",
    "an",
    "the",
    "at",
    "in",
    "to",
    "on",
    "of"
}

CONTEXT_WORDS = {
    "it",
    "this",
    "that"
}

ENTITY_SKIP_INTENTS = {
    "ai",
    "general",
    "memory",
    "system",
    "coding"
}


def normalize(text):

    text = text.lower()

    replacements = {

        "chat gpt": "chatgpt",

        "vs code": "vscode",

        "visual studio code": "vscode",

        "google chrome": "chrome"

    }

    for old, new in replacements.items():

        text = text.replace(old, new)

    return text


def extract_entities(command):

    if command.intent in ENTITY_SKIP_INTENTS:

        command.entities = {}

        return command

    text = normalize(command.normalized)

    text = (
        text
        .replace(".", "")
        .replace(",", "")
        .replace("?", "")
        .replace("!", "")
    )

    words = [

        w

        for w in text.split()

        if w not in CONTEXT_WORDS

    ]

    entities = {}

    all_entities = []

    for entity in ENTITY_REGISTRY.values():

        resolver = entity.get("resolver")

        if resolver:

            try:

                values = resolver()

                all_entities.extend(values)

            except Exception as e:

                print("ENTITY ERROR:", e)

        else:

            patterns = entity.get("patterns", {})

            for values in patterns.values():

                all_entities.extend(values)

    # ----------------------------
    # CLEAN
    # ----------------------------

    cleaned = []

    seen = set()

    for item in all_entities:

        item = normalize(item.strip().lower())

        if item in IGNORE_WORDS:

            continue

        if item in seen:

            continue

        seen.add(item)

        cleaned.append(item)

    # ----------------------------
    # LONGEST FIRST
    # ----------------------------

    cleaned.sort(

        key=len,

        reverse=True

    )

    # ----------------------------
    # EXACT PHRASE MATCH
    # ----------------------------

    for value in cleaned:

        if value in text:

            entities["target"] = value

            command.entities = entities

            return command

    # ----------------------------
    # EXACT WORD MATCH
    # ----------------------------

    for value in cleaned:

        if value in words:

            entities["target"] = value

            command.entities = entities

            return command

    # ----------------------------
    # FUZZY MATCH
    # ----------------------------

    best_score = 0

    best_value = None

    for value in cleaned:

        score = fuzz.token_set_ratio(

            text,

            value

        )

        if score > best_score:

            best_score = score

            best_value = value

    if best_score >= 90:

        entities["target"] = best_value

    command.entities = entities

    return command