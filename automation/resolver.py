from automation.app_launcher import open_application
from automation.website_launcher import open_website



def resolve_open(target):

    # 1. Try app

    app_result = open_application(target)


    if app_result.get("success"):

        return app_result



    # 2. Try website

    web_result = open_website(target)


    if web_result:

        return web_result



    return {

        "success": False,

        "message":
        f"I could not find {target}."

    }