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



def normalize_name(name):

    name = name.lower().strip()

    name = (
        name
        .replace(".", "")
        .replace(",", "")
    )

    return ALIASES.get(
        name,
        name
    )





def find_application(name):


    name = normalize_name(name)


    if not app_database.APP_DATABASE:

        app_database.load_apps()



    # Exact match

    for app, path in app_database.APP_DATABASE.items():

        clean = app.lower().replace(".exe", "")


        if clean == name:

            return path




    # Partial match

    for app, path in app_database.APP_DATABASE.items():

        clean = app.lower().replace(".exe", "")


        if name in clean:

            return path



    return None





def launch_path(path, name):

    try:


        print(
            "LAUNCHING:",
            path
        )



        # Windows Store App

        if name in STORE_APPS:


            subprocess.Popen(
                [
                    "explorer.exe",
                    f"shell:AppsFolder\\{STORE_APPS[name]}"
                ]
            )


            return True





        # Normal exe


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


    clean_name = normalize_name(name)



    path = find_application(
        clean_name
    )



    print(
        "FOUND PATH:",
        path
    )



    if not path:


        return {

            "success": False,

            "type": "app",

            "message":
            f"I could not find {clean_name}.",

            "item":
            clean_name

        }





    success = launch_path(
        path,
        clean_name
    )




    if success:


        return {

            "success": True,

            "type": "app",

            "message":
            f"Opening {clean_name}.",

            "item":
            clean_name

        }





    return {


        "success": False,

        "type": "app",

        "message":
        f"Could not open {clean_name}.",

        "item":
        clean_name

    }




def close_application(name):

    name = name.lower().strip()


    PROCESS_MAP = {

        "chrome": "chrome.exe",
        "calculator": "CalculatorApp.exe",
        "notepad": "notepad.exe",
        "paint": "mspaint.exe"

    }


    process = PROCESS_MAP.get(name)


    if not process:

        return {

            "success": False,

            "message": f"I don't know how to close {name}."

        }



    try:

        subprocess.run(
            [
                "taskkill",
                "/IM",
                process,
                "/F"
            ],
            capture_output=True,
            text=True
        )


        return {

            "success": True,

            "message": f"Closing {name}.",

            "item": name

        }



    except Exception as e:


        print(
            "CLOSE ERROR:",
            e
        )


        return {

            "success": False,

            "message": f"Could not close {name}."

        }