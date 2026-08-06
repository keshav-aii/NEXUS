from automation.browser_launcher import (
    launch_browser,
    open_website,
    google_search,
    youtube_search
)


# ==========================================================
# OPEN BROWSER
# ==========================================================

def open_browser(browser):

    success = launch_browser(browser)

    if success:

        return {

            "success": True,

            "type": "browser",

            "action": "browser_opened",

            "item": browser

        }

    return {

        "success": False,

        "type": "browser",

        "action": "browser_failed",

        "item": browser

    }


# ==========================================================
# OPEN WEBSITE
# ==========================================================

def open_site(url, name=None):

    success = open_website(url)

    if success:

        return {

            "success": True,

            "type": "website",

            "action": "website_opened",

            "item": name if name else url,

            "url": url

        }

    return {

        "success": False,

        "type": "website",

        "action": "website_failed",

        "item": name if name else url

    }


# ==========================================================
# GOOGLE SEARCH
# ==========================================================

def search_google(query):

    success = google_search(query)

    if success:

        return {

            "success": True,

            "type": "search",

            "action": "google_search",

            "item": query

        }

    return {

        "success": False,

        "type": "search",

        "action": "search_failed",

        "item": query

    }


# ==========================================================
# YOUTUBE SEARCH
# ==========================================================

def search_youtube(query):

    success = youtube_search(query)

    if success:

        return {

            "success": True,

            "type": "youtube",

            "action": "youtube_search",

            "item": query

        }

    return {

        "success": False,

        "type": "youtube",

        "action": "search_failed",

        "item": query

    }