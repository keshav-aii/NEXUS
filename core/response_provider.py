import random

from core.data_loader import load_data


RESPONSES = load_data("responses.json")


def respond(action, name=None, **kwargs):

    responses = RESPONSES.get(
        action,
        RESPONSES.get("general", ["Okay boss."])
    )

    response = random.choice(responses)

    values = dict(kwargs)
    values["name"] = name or ""

    try:
        return response.format(**values)
    except Exception:
        return response