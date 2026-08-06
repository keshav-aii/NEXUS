import json
import os



BASE_PATH = os.path.join(
    os.getcwd(),
    "data"
)



def load_data(filename):


    path = os.path.join(
        BASE_PATH,
        filename
    )


    if not os.path.exists(path):

        print(
            "DATA FILE NOT FOUND:",
            path
        )

        return {}



    try:


        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:


            return json.load(file)



    except Exception as e:


        print(
            "DATA LOAD ERROR:",
            e
        )


        return {}