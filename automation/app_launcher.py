import subprocess

from automation import app_database


ALIASES = {

    "chrome": "chrome",

    "google chrome": "chrome",

    "browser": "chrome",

    "calculator": "calculator",

    "calc": "calculator",

    "notepad": "notepad",

    "paint": "paint",

    "git": "git",

}

STORE_APPS = {

    "calculator":
    "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"

}




def find_application(name):


    name = name.lower().strip()



    # remove punctuation
    name = name.replace(".", "")
    name = name.replace(",", "")



    # alias convert

    name = ALIASES.get(
        name,
        name
    )



    if not app_database.APP_DATABASE:

        app_database.load_apps()





    # Exact match

    for app, path in app_database.APP_DATABASE.items():

        if app.lower() == name:

            return path





    # Partial match

    for app, path in app_database.APP_DATABASE.items():

        if name in app.lower():

            return path





    return None








def launch_path(path, name):

    try:

        print(
            "LAUNCHING:",
            path
        )


        # Microsoft Store apps

        if name in STORE_APPS:


            subprocess.Popen(
                [
                    "explorer.exe",
                    f"shell:AppsFolder\\{STORE_APPS[name]}"
                ]
            )


            return True




        # Normal exe apps

        subprocess.Popen(
            path
        )


        return True



    except Exception as e:

        print(
            "LAUNCH ERROR:",
            e
        )

        return False


def open_application(name):


    path = find_application(
        name
    )



    print(
        "FOUND PATH:",
        path
    )




    if path:


        success = launch_path(
        path,
        name.lower()
    )

        if success:


            return {


                "message":

                f"Opening {name}."

            }




        return {


            "message":

            f"Could not open {name}."

        }





    return {


        "message":

        f"I could not find {name}."

    }