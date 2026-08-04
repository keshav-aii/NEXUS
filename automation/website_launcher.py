import webbrowser



WEBSITES = {

    "github":
    "https://github.com",

    "youtube":
    "https://youtube.com",

    "google":
    "https://google.com",

    "linkedin":
    "https://linkedin.com",

    "chatgpt":
    "https://chat.openai.com",

    "gmail":
    "https://gmail.com"

}



def open_website(name):

    name = name.lower().strip()


    url = WEBSITES.get(name)


    if not url:

        return None



    webbrowser.open(url)


    return {

        "success": True,

        "message":
        f"Opening {name}."

    }