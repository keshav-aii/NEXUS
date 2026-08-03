import os
import json


from automation.app_scanner import scan_apps



CACHE_FILE = os.path.join(

    "data",

    "apps.json"

)



APP_DATABASE = {}





def save_cache():

    with open(
        CACHE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            APP_DATABASE,

            f,

            indent=4

        )





def load_cache():


    global APP_DATABASE



    if os.path.exists(
        CACHE_FILE
    ):


        with open(

            CACHE_FILE,

            "r",

            encoding="utf-8"

        ) as f:


            APP_DATABASE = json.load(
                f
            )


            return True



    return False





def load_apps():


    global APP_DATABASE



    # Try cache first

    if load_cache():


        return APP_DATABASE






    # Scan new apps

    APP_DATABASE = scan_apps()



    save_cache()



    return APP_DATABASE