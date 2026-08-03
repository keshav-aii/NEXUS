import webbrowser

from tools.websites import WEBSITES



def search_youtube(query):


    query = query.replace(
        " ",
        "+"
    )


    url = (
        "https://www.youtube.com/results?search_query="
        + query
    )


    webbrowser.open(
        url
    )


    return True





def search_google(query):


    query = query.replace(
        " ",
        "+"
    )


    url = (
        "https://www.google.com/search?q="
        + query
    )


    webbrowser.open(
        url
    )


    return True





def open_website(name):


    name = name.lower().strip()



    if name in WEBSITES:


        webbrowser.open(
            WEBSITES[name]
        )


        return True




    # direct URL support

    if name.startswith(
        "http"
    ):


        webbrowser.open(
            name
        )


        return True




    return False