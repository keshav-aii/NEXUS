from core.intent_engine import detect_intent
from core.entity_extractor import extract_entities
from core.plugin_loader import load_plugins
from core.capability_registry import get_plugin
from core.message_engine import get_message
from core.context_resolver import resolve_context

PLUGINS = load_plugins()


def process(command):

    print(
        "ROUTER COMMAND:",
        command.normalized
    )

    # ======================
    # INTENT
    # ======================

    command = detect_intent(command)

    print(
        "INTENT:",
        command.intent
    )

    # ======================
    # ENTITIES
    # ======================

    command = extract_entities(command)

    print(
        "ENTITIES:",
        command.entities
    )

    command = resolve_context(command)

    print(
    "AFTER CONTEXT:",
    command.entities
    )

   
    # ======================
    # DELETE CONFIRMATION
    # ======================

    if (
        command.intent == "delete"
        and not command.context.get("confirmed")
    ):

        return {

            "type": "confirmation",

            "message": get_message(
                "delete_confirm",
                item=command.entities.get(
                    "name",
                    "file"
                )
            ),

            "command": command

        }

    print(
        "CONFIRMED FLAG:",
        command.context.get("confirmed")
    )

    # ======================
    # CAPABILITY REGISTRY
    # ======================

    plugin_name = get_plugin(
        command.intent
    )

    print(
        "TARGET PLUGIN:",
        plugin_name
    )

    if not plugin_name:

        return None

    plugin = PLUGINS.get(
        plugin_name
    )

    if not plugin:

        print(
            f"PLUGIN NOT FOUND: {plugin_name}"
        )

        return None

    print(
        "RUNNING:",
        plugin_name
    )

    try:

        result = plugin["handler"](
            command
        )

        if result:

            return {

                "type": "plugin",

                "data": result

            }

    except Exception as e:

        print(
            "PLUGIN ERROR:",
            e
        )

    # ======================
    # UNKNOWN
    # ======================

    return None