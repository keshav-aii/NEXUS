from rapidfuzz import fuzz

from core.entity_registry import load_entities


ENTITY_REGISTRY = load_entities()


print(
    "ENTITY REGISTRY:",
    ENTITY_REGISTRY
)



IGNORE_WORDS = {

    "a",
    "an",
    "the",
    "at",
    "in",
    "to",
    "on",
    "of"

}



CONTEXT_WORDS = {

    "it",
    "this",
    "that"

}





def extract_entities(command):


    text = command.normalized.lower()



    # remove punctuation

    text = (
        text
        .replace(".", "")
        .replace(",", "")
        .replace("?", "")
        .replace("!", "")
    )



    entities = {}



    # ======================
    # COLLECT ALL ENTITIES
    # ======================


    all_entities = []



    for name, entity in ENTITY_REGISTRY.items():


        resolver = entity.get(
            "resolver"
        )



        if resolver:


            try:

                values = resolver()


                all_entities.extend(
                    values
                )


            except Exception as e:

                print(
                    "ENTITY RESOLVER ERROR:",
                    e
                )



        else:


            patterns = entity.get(
                "patterns",
                {}
            )


            for key, values in patterns.items():


                all_entities.extend(
                    values
                )




    # ======================
    # WORD CLEANING
    # ======================


    words = text.split()



    words = [

        word

        for word in words

        if word not in CONTEXT_WORDS

    ]





    # ======================
    # FIND BEST MATCH
    # ======================


    best_score = 0

    best_value = None





    for value in all_entities:


        value = value.lower().strip()



        if value in IGNORE_WORDS:

            continue





        # exact match

        if value in words:


            best_value = value

            best_score = 100

            break






        # fuzzy match


        for word in words:


            score = fuzz.partial_ratio(
                word,
                value
            )



            if score > best_score:


                best_score = score

                best_value = value







    # ======================
    # SAVE ENTITY
    # ======================


    if best_score >= 75:


        entities["target"] = best_value



    command.entities = entities



    return command