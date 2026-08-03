import os
import subprocess
import webbrowser
import requests

from config.user_config import (
    PROJECTS,
    GITHUB_REPO,
    USE_CHATGPT,
    VS_CODE_PATH,
)


def handle(command):

    command = command.lower().strip()

    if command not in [
        "start coding",
        "coding mode",
        "lets code",
        "let's code",
    ]:
        return None

    # Open Project
    project = PROJECTS.get("nexus")

    # Open VS Code
    subprocess.Popen([VS_CODE_PATH])

    # Open Project in VS Code
    if project and os.path.exists(project):
          subprocess.Popen([VS_CODE_PATH, project])

    # Open GitHub
    webbrowser.open(GITHUB_REPO)

    # Open ChatGPT
    if USE_CHATGPT:
        webbrowser.open("https://chatgpt.com")

    # Open Windows Terminal and run git status
    if project and os.path.exists(project):
        try:
            subprocess.Popen([
                 "wt",
                 "-d",
                 project,
                 "powershell",
                 "-NoExit",
                 "-Command",
                 "git status"
            ])
        except FileNotFoundError:
            print("Windows Terminal not found.") 

    # Check Ollama
    try:
        requests.get("http://localhost:11434", timeout=2)
        ollama_status = "Ollama is running."
    except:
        ollama_status = "Warning. Ollama is not running."

    return {
        "message": "Workspace is ready. Git status loaded. Enjoy coding.",
        "ollama": ollama_status
    }