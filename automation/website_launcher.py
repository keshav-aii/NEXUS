import webbrowser

from core.data_loader import load_data


WEBSITES = load_data("websites.json")


def open_website(target):

    target = target.lower().strip()

    url = WEBSITES.get(target)

    if not url:

        return None

    try:

        webbrowser.open(url)

        return {
            "success": True,
            "type": "website",
            "url": url
        }

    except Exception:

        return {
            "success": False,
            "type": "website"
        }