from automation.app_launcher import (
    open_application,
    close_application
)

from automation.website_launcher import open_website


def resolve_open(target):

    # =====================
    # TRY APP
    # =====================

    app_result = open_application(target)

    if app_result.get("success"):

        app_result["type"] = "app"

        return app_result

    # =====================
    # TRY WEBSITE
    # =====================

    web_result = open_website(target)

    if web_result and web_result.get("success"):

        web_result["type"] = "website"

        return web_result

    # =====================
    # NOT FOUND
    # =====================

    return {

        "success": False,

        "type": "none",

        "message": f"I could not find {target}."

    }


def resolve_close(target):

    # =====================
    # CLOSE APP
    # =====================

    result = close_application(target)

    return result