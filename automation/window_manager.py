import pygetwindow as gw


# ==========================================================
# FIND WINDOW
# ==========================================================

def find_window(title):

    title = title.lower()

    windows = gw.getAllTitles()

    for window in windows:

        if not window.strip():
            continue

        if title in window.lower():

            return gw.getWindowsWithTitle(window)[0]

    return None


# ==========================================================
# CHECK WINDOW OPEN
# ==========================================================

def is_window_open(title):

    return find_window(title) is not None


# ==========================================================
# FOCUS WINDOW
# ==========================================================

def focus_window(title):

    window = find_window(title)

    if not window:

        return False

    try:

        if window.isMinimized:

            window.restore()

        window.activate()

        return True

    except Exception as e:

        print(
            "WINDOW FOCUS ERROR:",
            e
        )

        return False