import subprocess



def get_running_processes():


    result = subprocess.run(
        [
            "tasklist"
        ],
        capture_output=True,
        text=True
    )


    return result.stdout.lower()





def is_running(process_name):


    processes = get_running_processes()


    return process_name.lower() in processes





def kill_process(process_name):


    try:


        result = subprocess.run(
            [
                "taskkill",
                "/IM",
                process_name,
                "/F"
            ],
            capture_output=True,
            text=True
        )


        if result.returncode == 0:

            return True



        return False



    except Exception as e:


        print(
            "PROCESS ERROR:",
            e
        )


        return False