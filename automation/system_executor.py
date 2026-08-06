import os



# =========================
# ACTION FUNCTIONS
# =========================


def lock():

    os.system(
        "rundll32.exe user32.dll,LockWorkStation"
    )

    return True





def shutdown():

    os.system(
        "shutdown /s /t 5"
    )

    return True





def restart():

    os.system(
        "shutdown /r /t 5"
    )

    return True





def sleep():

    os.system(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    )

    return True





# =========================
# EXECUTOR REGISTRY
# =========================


EXECUTORS = {


    "lock":
    lock,


    "shutdown":
    shutdown,


    "restart":
    restart,


    "sleep":
    sleep

}





# =========================
# MAIN EXECUTOR
# =========================


def execute(action):


    executor = EXECUTORS.get(
        action
    )



    if not executor:


        print(
            "EXECUTOR NOT FOUND:",
            action
        )


        return False





    try:


        return executor()



    except Exception as e:


        print(
            "SYSTEM EXECUTOR ERROR:",
            e
        )


        return False