import subprocess
import webbrowser
from urllib.parse import quote_plus

from automation.browser_database import BROWSERS
from automation.browser_detector import (
    get_browser_path,
    is_browser_installed
)


# ==========================================================
# LAUNCH BROWSER
# ==========================================================

def launch_browser(browser):

    browser = browser.lower()

    if not is_browser_installed(browser):

        return False

    path = get_browser_path(browser)

    if not path:

        return False

    try:

        subprocess.Popen([path])

        return True

    except Exception as e:

        print(
            "BROWSER LAUNCH ERROR:",
            e
        )

        return False


# ==========================================================
# OPEN URL
# ==========================================================

def open_url(url):

    try:

        webbrowser.open(url)

        return True

    except Exception as e:

        print(
            "URL OPEN ERROR:",
            e
        )

        return False


# ==========================================================
# GOOGLE SEARCH
# ==========================================================

def google_search(query):

    url = (
        "https://www.google.com/search?q="
        + quote_plus(query)
    )

    return open_url(url)


# ==========================================================
# YOUTUBE SEARCH
# ==========================================================

def youtube_search(query):

    url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )

    return open_url(url)


# ==========================================================
# OPEN WEBSITE
# ==========================================================

def open_website(url):

    return open_url(url)