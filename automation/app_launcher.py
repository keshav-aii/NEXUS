import subprocess

from automation import app_database
from automation.process_manager import close_process
from automation.window_manager import (
    is_window_open,
    focus_window
)

# ==========================================================
# APP ALIASES
# ==========================================================

ALIASES = {

    "chrome": "chrome",
    "google chrome": "chrome",
    "browser": "chrome",

    "calculator": "calculator",
    "calc": "calculator",

    "notepad": "notepad",

    "paint": "paint",

    "git": "git",

    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",

}


# ==========================================================
# MICROSOFT STORE APPS
# ==========================================================

STORE_APPS = {

    "calculator":
    "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"

}


# ==========================================================
# NORMALIZE NAME
# ==========================================================

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


# ==========================================================
# FIND APPLICATION
# ==========================================================

def find_application(name):

    name = normalize_name(name)

    if not app_database.APP_DATABASE:
        app_database.load_apps()

    # -------------------------
    # Exact Match
    # -------------------------

    for app, path in app_database.APP_DATABASE.items():

        clean = (
            app.lower()
            .replace(".exe", "")
            .strip()
        )

        if clean == name:
            return path

    # -------------------------
    # Alias Match
    # -------------------------

    alias = ALIASES.get(name)

    if alias:

        for app, path in app_database.APP_DATABASE.items():

            clean = (
                app.lower()
                .replace(".exe", "")
                .strip()
            )

            if clean == alias:
                return path

    # -------------------------
    # Partial Match
    # -------------------------

    for app, path in app_database.APP_DATABASE.items():

        clean = (
            app.lower()
            .replace(".exe", "")
            .strip()
        )

        if (
            name in clean
            or clean in name
        ):
            return path

    return None


# ==========================================================
# LAUNCH APP
# ==========================================================

def launch_path(path, name):

    try:

        print(
            "LAUNCHING:",
            path
        )

        if name in STORE_APPS:

            subprocess.Popen(
                [
                    "explorer.exe",
                    f"shell:AppsFolder\\{STORE_APPS[name]}"
                ]
            )

            return True

        subprocess.Popen([path])

        return True

    except Exception as e:

        print(
            "LAUNCH ERROR:",
            e
        )

        return False


# ==========================================================
# OPEN APPLICATION
# ==========================================================

def open_application(name):

    clean_name = normalize_name(name)

    # -----------------------------------------
    # Already Running?
    # -----------------------------------------

    if is_window_open(clean_name):

        print(
            "APP ALREADY RUNNING:",
            clean_name
        )

        focus_window(clean_name)

        return {

            "success": True,

            "type": "app",

            "action": "app_focused",

            "message":
            f"{clean_name} is already running.",

            "item":
            clean_name

        }

    # -----------------------------------------
    # Find Application
    # -----------------------------------------

    path = find_application(clean_name)

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

    # -----------------------------------------
    # Launch
    # -----------------------------------------

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
    
    

# ==========================================================
# CLOSE APPLICATION
# ==========================================================

def close_application(name):

    clean_name = normalize_name(name)

    result = close_process(clean_name)

    if result.get("success"):

        return {

            "success": True,

            "process": clean_name,

            "forced": result.get(
                "forced",
                False
            )

        }

    if result.get("message"):

        if "not running" in result["message"].lower():

            return {

                "success": False,

                "reason": "not_running",

                "process": clean_name

            }

    return {

        "success": False,

        "reason": "close_failed",

        "process": clean_name

    }