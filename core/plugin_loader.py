import os
import importlib



PLUGIN_FOLDER = "plugins"



def load_plugins():


    plugins = {}



    files = sorted(
        os.listdir(
            PLUGIN_FOLDER
        )
    )



    for file in files:



        if not file.endswith(".py"):

            continue



        if file == "__init__.py":

            continue




        module_name = (
            f"{PLUGIN_FOLDER}.{file[:-3]}"
        )



        try:


            module = importlib.import_module(
                module_name
            )



            if hasattr(
                module,
                "handle"
            ):



                plugin = {


                    "handler":
                    module.handle,


                    "info":
                    getattr(
                        module,
                        "PLUGIN_INFO",
                        {}
                    )

                }



                plugins[plugin["info"]["name"]] = plugin


                print(
                    f"Loaded: {module_name}"
                )



        except Exception as e:


            print(
                f"Failed {module_name}: {e}"
            )



    

    return plugins