import subprocess

from automation import app_database




ALIASES = {

    "chrome":
    "chrome",

    "google chrome":
    "chrome",

    "browser":
    "chrome",

    "git":
    "git",

    "calculator":
    "calculator",

    "calc":
    "calculator",

    "notepad":
    "notepad",

    "paint":
    "paint",

}





def find_application(name):


    name = name.lower().strip()



    name = ALIASES.get(
        name,
        name
    )



    if not app_database.APP_DATABASE:


        app_database.load_apps()





    # Exact match first


    for app, path in app_database.APP_DATABASE.items():


        if app.lower() == name:


            return path






    # Partial match


    for app, path in app_database.APP_DATABASE.items():


        if name in app.lower():


            return path





    return None





def open_application(name):


    path = find_application(
        name
    )



    if path:


        subprocess.Popen(
            path
        )


        return {

            "message":
            f"Opening {name}."

        }




    return {

        "message":
         f"Opening {name.title()}."

    }