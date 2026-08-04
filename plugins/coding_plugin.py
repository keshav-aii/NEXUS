import os
import subprocess
import webbrowser
import requests


from core.command import Command


from config.user_config import (
    PROJECTS,
    GITHUB_REPO,
    USE_CHATGPT,
    VS_CODE_PATH,
)



PLUGIN_INFO = {

    "name": "coding",

    "priority": 40,

    "intents": [

        "coding"

    ]

}





def handle(command: Command):


    if command.intent != "coding":

        return None





    project = PROJECTS.get(
        "nexus"
    )




    # ==========================
    # OPEN VS CODE
    # ==========================


    if os.path.exists(
        VS_CODE_PATH
    ):


        if project and os.path.exists(project):


            subprocess.Popen(
                [
                    VS_CODE_PATH,
                    project
                ]
            )


        else:


            subprocess.Popen(
                [
                    VS_CODE_PATH
                ]
            )







    # ==========================
    # GITHUB
    # ==========================


    if GITHUB_REPO:


        webbrowser.open(
            GITHUB_REPO
        )







    # ==========================
    # CHATGPT
    # ==========================


    if USE_CHATGPT:


        webbrowser.open(
            "https://chatgpt.com"
        )







    # ==========================
    # TERMINAL
    # ==========================


    if project and os.path.exists(project):


        try:


            subprocess.Popen(
                [
                    "wt",
                    "-d",
                    project,
                    "powershell",
                    "-NoExit",
                    "-Command",
                    "git status"
                ]
            )


        except FileNotFoundError:


            pass







    # ==========================
    # OLLAMA CHECK
    # ==========================


    try:


        requests.get(

            "http://localhost:11434",

            timeout=2

        )


        ollama_status = "running"



    except requests.RequestException:


        ollama_status = "not_running"







    return {


        "action":

        "coding_ready",



        "ollama":

        ollama_status

    }