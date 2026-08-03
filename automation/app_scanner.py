import os


SEARCH_PATHS = [

    r"C:\Program Files",

    r"C:\Program Files (x86)",

    os.path.expanduser(
        r"~\AppData\Local\Programs"
    ),

]



def scan_apps():

    apps = {}



    for base_path in SEARCH_PATHS:


        if not os.path.exists(base_path):

            continue



        for root, dirs, files in os.walk(base_path):


            for file in files:


                if file.lower().endswith(".exe"):


                    name = file[:-4].lower()


                    path = os.path.join(
                        root,
                        file
                    )


                    apps[name] = path



    return apps