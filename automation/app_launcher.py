import subprocess

from automation import app_database



ALIASES = {

    "chrome": "chrome",

    "google chrome": "chrome",

    "browser": "chrome",

    "git": "git",

    "calculator": "calculator",

    "calc": "calculator",

}



def open_application(name):


    name = name.lower().strip()



    name = ALIASES.get(
        name,
        name
    )



    # Load apps

    if not app_database.APP_DATABASE:

        app_database.load_apps()



    for app, path in app_database.APP_DATABASE.items():


        if name in app.lower():


            subprocess.Popen(
                path
            )


            return {

                "message":
                f"Opening {name}."

            }



    return {

        "message":
        f"I couldn't find {name}."

    }