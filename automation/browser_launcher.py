import webbrowser


def open_url(url):

    try:

        webbrowser.open(url)

        return True

    except Exception:

        return False