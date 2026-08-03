from tools.browser_tools import (
    open_website,
    search_google,
    search_youtube,
)

from tools.app_tools import run as run_app



def execute(action):


    if not action:

        return None



    action_type = action.get(
        "type"
    )



    # ==========================
    # WEBSITE
    # ==========================

    if action_type == "website":


        return open_website(
            action["name"]
        )





    # ==========================
    # GOOGLE SEARCH
    # ==========================

    elif action_type == "google":


        return search_google(
            action["query"]
        )





    # ==========================
    # YOUTUBE SEARCH
    # ==========================

    elif action_type == "youtube":


        return search_youtube(
            action["query"]
        )





    # ==========================
    # APP
    # ==========================

    elif action_type == "app":


        return run_app(
            action["name"]
        )




    return None