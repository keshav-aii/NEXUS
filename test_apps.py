from automation import app_database
from automation.app_launcher import open_application



app_database.load_apps()



print(
    open_application("chrome")
)