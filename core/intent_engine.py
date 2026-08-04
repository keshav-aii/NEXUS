from core.plugin_loader import load_plugins

PLUGINS = load_plugins()

KEYWORD_MAP = {}

for plugin_name, plugin in PLUGINS.items():

    info = plugin["info"]
    intent_list = info.get("intents", [])

    keywords = info.get("keywords", [])

    for intent in intent_list:

        KEYWORD_MAP.setdefault(intent, [])

        KEYWORD_MAP[intent].extend(keywords)


def detect_intent(command):

    text = command.normalized.lower()

    best_intent = None
    best_score = 0

    for intent, keywords in KEYWORD_MAP.items():

        score = 0

        for keyword in keywords:

            if keyword in text:

                score += len(keyword)

        if score > best_score:

            best_score = score
            best_intent = intent

    command.intent = best_intent
    command.confidence = min(best_score / 10, 1.0) if best_intent else 0

    return command