import subprocess
import time
import psutil


# ==================================================
# GET TASKLIST
# ==================================================

def get_process_list():

    result = subprocess.run(
        [
            "tasklist"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout.lower()


# ==================================================
# FIND PROCESS NAME
# ==================================================

def find_process(name):

    processes = get_process_list()

    name = name.lower()

    for line in processes.splitlines():

        if name in line:

            return line.split()[0]

    return None


# ==================================================
# GET ALL PROCESS INSTANCES
# ==================================================

def get_processes(process_name):

    process_name = process_name.lower()

    instances = []

    for proc in psutil.process_iter(["pid", "name"]):

        try:

            running = proc.info["name"]

            if running and running.lower() == process_name:

                instances.append(proc)

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            pass

    return instances

# ==================================================
# CHECK IF PID IS RUNNING
# ==================================================

def is_pid_running(pid):

    return psutil.pid_exists(pid)


# ==================================================
# CHECK IF PROCESS IS RUNNING
# ==================================================

def is_process_running(process_name):

    return find_process(process_name) is not None


# ==================================================
# NORMAL CLOSE (PID)
# ==================================================




# ==================================================
# FORCE CLOSE (PID)
# ==================================================

def force_close(pid):

    result = subprocess.run(

        [
            "taskkill",
            "/PID",
            str(pid),
            "/F"
        ],

        capture_output=True,
        text=True

    )

    return result.returncode == 0


# ==================================================
# SMART CLOSE
# ==================================================

def close_process(name):

    process = find_process(name)

    print(
        "FOUND PROCESS:",
        process
    )

    if not process:

        return {

            "success": False,

            "message": f"{name} is not running.",

            "forced": False

        }

    # -----------------------------------------
    # GET ALL INSTANCES
    # -----------------------------------------

    instances = get_processes(process)

    print(
        "INSTANCES:",
        instances
    )

    if not instances:

        return {

            "success": False,

            "message": f"{name} is not running.",

            "forced": False

        }

    # -----------------------------------------
    # PICK LATEST INSTANCE
    # -----------------------------------------

    latest = max(
        instances,
        key=lambda p: p.pid
    )

    print(
        "LATEST PID:",
        latest.pid
    )

    print(
        "LATEST NAME:",
        latest.name()
    )
    pid = latest.pid
    # -----------------------------------------
    # TRY NORMAL CLOSE
    # -----------------------------------------
    try:
        latest.terminate()

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied
    ):
        pass

    # -----------------------------------------
    # WAIT
    # -----------------------------------------

    try:

        latest.terminate()

        latest.wait(timeout=2)

    except psutil.TimeoutExpired:

        pass

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied
    ):
        pass

    # -----------------------------------------
    # CHECK
    # -----------------------------------------

    if not is_pid_running(pid):

        return {

            "success": True,

            "message": f"{name} closed successfully.",

            "item": name,

            "forced": False

        }

    # -----------------------------------------
    # FORCE CLOSE
    # -----------------------------------------

    if force_close(pid):

        return {

            "success": True,

            "message": f"{name} was not responding. Force closed.",

            "item": name,

            "forced": True

        }

    return {

        "success": False,

        "message": f"Could not close {name}.",

        "forced": False

    }