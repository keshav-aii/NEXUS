import os



SEARCH_PATHS = [

    r"C:\Program Files",

    r"C:\Program Files (x86)",

    os.path.expanduser(
        r"~\AppData\Local\Programs"
    ),

]





IGNORE_WORDS = [

    "uninstall",

    "update",

    "helper",

    "service",

    "setup",

    "crash",

    "report",

    "updater",

]






def is_valid_app(name):


    for word in IGNORE_WORDS:


        if word in name:


            return False



    return True






def scan_apps():


    apps = {}




    for base_path in SEARCH_PATHS:



        if not os.path.exists(
            base_path
        ):


            continue





        for root, dirs, files in os.walk(
            base_path
        ):



            for file in files:



                if not file.lower().endswith(
                    ".exe"
                ):


                    continue





                name = file[:-4].lower()





                if not is_valid_app(
                    name
                ):


                    continue





                path = os.path.join(

                    root,

                    file

                )





                # Keep first found

                if name not in apps:


                    apps[name] = path





    return apps