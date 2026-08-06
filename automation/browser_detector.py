import psutil

from automation.browser_database import BROWSERS


# ==========================================================
# CHECK INSTALLED
# ==========================================================

def is_browser_installed(browser):

    browser = browser.lower()

    info = BROWSERS.get(browser)

    if not info:
        return False

    return info["installed"]


# ==========================================================
# CHECK RUNNING
# ==========================================================

def is_browser_running(browser):

    browser = browser.lower()

    info = BROWSERS.get(browser)

    if not info:
        return False

    process_name = info["process"].lower()

    for proc in psutil.process_iter(["name"]):

        try:

            running = proc.info["name"]

            if running and running.lower() == process_name:

                return True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            pass

    return False


# ==========================================================
# GET RUNNING BROWSER
# ==========================================================

def get_running_browser():

    for browser, info in BROWSERS.items():

        process_name = info["process"].lower()

        for proc in psutil.process_iter(["name"]):

            try:

                running = proc.info["name"]

                if running and running.lower() == process_name:

                    return browser

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied
            ):
                pass

    return None


# ==========================================================
# GET BROWSER PATH
# ==========================================================

def get_browser_path(browser):

    browser = browser.lower()

    info = BROWSERS.get(browser)

    if not info:
        return None

    return info["path"]


# ==========================================================
# GET PROCESS NAME
# ==========================================================

def get_browser_process(browser):

    browser = browser.lower()

    info = BROWSERS.get(browser)

    if not info:
        return None

    return info["process"]