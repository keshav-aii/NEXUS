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
    "intents": [
        "coding"
    ]
}


def handle(command: Command):

    # Only handle coding intent

    if command.intent != "coding":
        return None


    project = PROJECTS.get("nexus")


    # Open VS Code

    subprocess.Popen(
        [VS_CODE_PATH]
    )


    # Open Project

    if project and os.path.exists(project):

        subprocess.Popen(
            [
                VS_CODE_PATH,
                project
            ]
        )


    # Open GitHub

    webbrowser.open(
        GITHUB_REPO
    )


    # Open ChatGPT

    if USE_CHATGPT:

        webbrowser.open(
            "https://chatgpt.com"
        )


    # Git Status Terminal

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


    # Check Ollama

    try:

        requests.get(
            "http://localhost:11434",
            timeout=2
        )

        ollama_status = "Ollama is running."


    except:

        ollama_status = "Warning. Ollama is not running."


    return {

        "message":
        "Coding workspace is ready.",

        "ollama":
        ollama_status
    }