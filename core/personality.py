import random



def respond(action, name=None, **kwargs):


    name_text = ""

    if name:

        name_text = f" {name}"



    responses = {



        # ======================
        # WAKE
        # ======================

        "wake": [

            f"Haan{name_text}, main sun rahi hoon.",

            "Ji boss, main sun rahi hoon.",

            f"Haan{name_text}, bolo kya karna hai.",

            "Ready hoon boss, batao."

        ],




        # ======================
        # ATTENTION
        # ======================

        "attention": [

            "Ji boss?",

            "Haan bolo Keshav.",

            "Ji boss, batao.",

            "Main sun rahi hoon."

        ],




        # ======================
        # DELETE CONFIRM
        # ======================

        "delete_confirm": [

            f"Kya aap sure ho boss? Kya main {kwargs.get('item','ye file')} delete kar du?",

            f"Confirm karo boss, kya {kwargs.get('item','ye file')} remove karni hai?"

        ],




        # ======================
        # DELETE SUCCESS
        # ======================

        "delete_success": [

            f"Done boss, {kwargs.get('item','file')} delete kar di hai.",

            f"Ho gaya boss, {kwargs.get('item','file')} remove kar diya hai."

        ],




        # ======================
        # OPEN
        # ======================

        "open": [

            f"Okay boss, {kwargs.get('item','app')} open kar rahi hoon.",

            f"Done boss, {kwargs.get('item','app')} launch kar diya hai."

        ],




        # ======================
        # FILE CREATE
        # ======================

        "file_created": [

            f"Done boss, {kwargs.get('item','file')} bana di hai.",

            f"Ho gaya boss, {kwargs.get('item','file')} create kar di hai."

        ],




        # ======================
        # FOLDER CREATE
        # ======================

        "folder_created": [

            f"Done boss, {kwargs.get('item','folder')} folder bana diya hai.",

            f"Ho gaya boss, {kwargs.get('item','folder')} create kar diya hai."

        ],




        # ======================
        # FOLDER DELETE
        # ======================

        "folder_deleted": [

            f"Done boss, {kwargs.get('item','folder')} folder delete kar diya hai.",

            f"Ho gaya boss, {kwargs.get('item','folder')} remove kar diya hai."

        ],




        # ======================
        # FILE NOT FOUND
        # ======================

        "file_not_found": [

            f"Sorry boss, {kwargs.get('item','file')} nahi mili.",

            f"Boss, mujhe {kwargs.get('item','file')} nahi mil rahi hai."

        ],




        # ======================
        # MISSING NAME
        # ======================

        "missing_name": [

            "Boss, file ya folder ka naam batao.",

            "Kis file ko handle karna hai boss? Naam specify karo."

        ],




        # ======================
        # MEMORY
        # ======================

        "remember": [

            f"Theek hai{name_text}, main yaad rakhungi.",

            "Memory update ho gayi hai boss."

        ],




        "memory_saved": [

            "Theek hai boss, main ye yaad rakhungi.",

            "Memory update ho gayi hai boss."

        ],




        "name_recall": [

            f"Aapka naam {kwargs.get('item','Keshav')} hai boss.",

            f"Mujhe yaad hai boss, aapka naam {kwargs.get('item','Keshav')} hai."

        ],




        "memory_empty": [

            "Abhi mujhe kuch yaad nahi hai boss.",

            "Meri memory me abhi koi information save nahi hai."

        ],




        "memory_list": [

            "Boss, mujhe ye cheezein yaad hain.",

        ],




        "memory_forgotten": [

            f"Theek hai boss, {kwargs.get('item','memory')} bhool gayi.",

            f"Okay boss, {kwargs.get('item','information')} remove kar di hai."

        ],




        "memory_not_found": [

            "Sorry boss, mujhe ye memory nahi mili.",

            "Mujhe ye information yaad nahi hai boss."

        ],




        # ======================
        # CONFIRM
        # ======================

        "confirm": [

            "Okay boss, main kar rahi hoon.",

            "Sure boss, proceed kar rahi hoon."

        ],




        # ======================
        # CANCEL
        # ======================

        "cancel": [

            "Theek hai, maine cancel kar diya.",

            "Okay boss, command cancel kar di hai."

        ],




        # ======================
        # SLEEP
        # ======================

        "sleep": [

            "Main ab sleep mode me ja rahi hoon. Bulana ho toh Nexus bol dena.",

            "Okay Keshav, main standby mode me ja rahi hoon."

        ],




        # ======================
        # ERROR
        # ======================

        "error": [

            "Sorry boss, ye kaam complete nahi ho paya.",

            "Sorry boss, kuch problem aa gayi."

        ],

        # ======================
        # CODING
        # ======================

        "coding_ready": [

            "Okay boss, coding workspace ready hai.",

            "Done boss, VS Code aur coding environment ready hai."

        ],

        "ollama_running": [

            "Ollama bhi ready hai boss."

        ],


        "ollama_not_running": [

            "Boss, coding ready hai lekin Ollama abhi run nahi ho raha."

        ],



        # ======================
        # UNKNOWN
        # ======================

        "unknown": [

            "Sorry boss, mujhe ye command samajh nahi aayi.",

            "Ek baar phir bolo Keshav."

        ],

        "close": [
        
            f"Done boss, {kwargs.get('item','app')} close kar diya hai.",
        
                f"Okay boss, {kwargs.get('item','app')} band kar diya hai."
        
            ],
        




        # ======================
        # GENERAL
        # ======================

        "general": [

            "Main badhiya hoon boss, aap batao.",

            "Haan boss, bolo.",

            "Ready hoon Keshav."

        ]
    }



    if action in responses:

        return random.choice(
            responses[action]
        )



    return random.choice(
        responses["general"]
    )
    