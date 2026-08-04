from automation import app_database


app_database.load_apps()



# ==========================
# APP ALIASES
# ==========================

ALIASES = {

    "chrome": [

        "chrome",
        "chrom",
        "google chrome",
        "google chrom"

    ],


    "vscode": [

        "vscode",
        "vs code",
        "visual studio code",
        "visual code"

    ],


    "notepad": [

        "notepad",
        "note pad",
        "notes",
        "note"

    ],


    "calculator": [

        "calculator",
        "calc",
        "calculate"

    ],


}

APP_ALIASES = ALIASES

# ==========================
# BUILD ENTITY LIST
# ==========================


targets = []



# Real installed apps

for app in app_database.APP_DATABASE.keys():

    targets.append(app)



# Aliases

for alias_list in ALIASES.values():

    targets.extend(alias_list)




# ==========================
# ENTITY
# ==========================


ENTITY = {

    "intent": "open",

    "patterns": {

        "target": targets

    }

}
