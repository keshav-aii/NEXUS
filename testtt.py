from automation import app_database

app_database.load_apps()

for name in app_database.APP_DATABASE.keys():
    if "code" in name.lower() or "studio" in name.lower() or "vs" in name.lower():
        print(name)