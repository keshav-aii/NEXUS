from core.command import Command

from automation.app_launcher import find_application



ALIASES = {

    "git hub": "github",

    "github.com": "github",

    "you tube": "youtube",

    "linked in": "linkedin",

    "chat gpt": "chatgpt",

}





def clean_target(text):


    text = text.lower().strip()



    for word in [

        "please",

        "for me"

    ]:


        text = text.replace(
            word,
            ""
        )


    return text.strip()





def choose_tool(command: Command):


    text = command.normalized.lower().strip()





    # ==========================
    # SEARCH YOUTUBE
    # ==========================


    if "youtube" in text or "you tube" in text:


        query = text


        for word in [

            "search",

            "youtube",

            "you tube",

            "on"

        ]:


            query = query.replace(
                word,
                ""
            )


        query = clean_target(query)



        return {

            "type": "youtube",

            "query": query,

            "message":
            f"Searching YouTube for {query}."

        }







    # ==========================
    # GOOGLE SEARCH
    # ==========================


    if text.startswith(

        (

            "search",

            "find",

            "look for"

        )

    ):


        query = text


        for word in [

            "search",

            "find",

            "look for"

        ]:


            query = query.replace(
                word,
                "",
                1
            )


        query = clean_target(
            query
        )


        return {

            "type": "google",

            "query": query,

            "message":
            f"Searching Google for {query}."

        }







    # ==========================
    # OPEN RESOLVER
    # ==========================


    if text.startswith(

        (

            "open",

            "launch",

            "start",

            "go to"

        )

    ):


        target = text


        for word in [

            "open",

            "launch",

            "start",

            "go to"

        ]:


            target = target.replace(

                word,

                "",

                1

            )


        target = clean_target(
            target
        )



        target = ALIASES.get(

            target,

            target

        )





        # First try APP


        app = find_application(
            target
        )



        if app:


            return {

                "type": "app",

                "name": target,

                "message":
                f"Opening {target}."

            }





        # Otherwise website


        return {

            "type": "website",

            "name": target,

            "message":
            f"Opening {target.title()}."

        }




    return None