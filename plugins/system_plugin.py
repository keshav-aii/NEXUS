from core.command import Command
from core.data_loader import load_data
from automation.system_executor import execute



SYSTEM_ACTIONS = load_data(
    "system_actions.json"
)



PLUGIN_INFO = {

    "name": "system",

    "priority": 100,

    "intents": [

        "system"

    ],

    "keywords": [

        "lock",
        "shutdown",
        "restart",
        "sleep",
        "reboot",
        "standby"

    ]

}





def find_action(text):


    text = text.lower()



    for action, data in SYSTEM_ACTIONS.items():


        keywords = data.get(
            "keywords",
            []
        )


        for word in keywords:


            if word in text:

                return data.get(
                    "executor"
                )



    return None







def handle(command: Command):


    if command.intent != "system":

        return None



    text = command.normalized.lower()



    action = find_action(
        text
    )



    print(
        "SYSTEM ACTION:",
        action
    )



    if not action:


        return {

            "action": "error"

        }




    result = execute(
        action
    )



    if result:


        return {

            "action":
            "system_" + action

        }



    return {

        "action":
        "error"

    }