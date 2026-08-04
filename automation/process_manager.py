import subprocess



def get_process_list():

    result = subprocess.run(
        [
            "tasklist"
        ],
        capture_output=True,
        text=True
    )


    return result.stdout.lower()





def find_process(name):

    processes = get_process_list()


    name = name.lower()



    for line in processes.splitlines():

        if name in line:

            return line.split()[0]


    return None





def close_process(name):


    process = find_process(
        name
    )


    print(
        "FOUND PROCESS:",
        process
    )


    if not process:


        return {

            "success": False,

            "message":
            f"{name} is not running."

        }




    result = subprocess.run(

        [
            "taskkill",
            "/IM",
            process,
            "/F"
        ],

        capture_output=True,

        text=True

    )



    if result.returncode == 0:


        return {

            "success": True,

            "message":
            f"Closing {name}.",

            "item":
            name

        }



    return {


        "success": False,

        "message":
        f"Could not close {name}."

    }