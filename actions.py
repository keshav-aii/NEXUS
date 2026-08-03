from tools.browser_tools import (
    open_website,
    search_google,
    search_youtube,
)
from tools.app_tools import run as run_app


def execute(action):

    if not action:
        return

    action_type = action["type"]

    if action_type == "website":

        result = open_website(action["name"])

        if result is None:
            run_app(action["name"])

    elif action_type == "google":

        search_google(action["query"])

    elif action_type == "youtube":

        search_youtube(action["query"])