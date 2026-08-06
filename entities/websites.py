from core.data_loader import load_data

WEBSITES = load_data("websites.json")


def resolve_targets():

    return list(WEBSITES.keys())


ENTITY = {

    "name": "websites",

    "type": "target",

    "resolver": resolve_targets

}