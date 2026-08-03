from automation.app_scanner import scan_apps



APP_DATABASE = {}



def load_apps():

    global APP_DATABASE


    APP_DATABASE = scan_apps()


    return APP_DATABASE