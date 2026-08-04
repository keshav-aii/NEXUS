from rapidfuzz import fuzz

from core.entity_registry import load_entities


ENTITY_REGISTRY = load_entities()


print(
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



    entity = ENTITY_REGISTRY.get(
        command.intent
    )



    if not entity:

        command.entities = {}

        return command





    patterns = entity.get(
        "patterns",
        {}
    )



    words = text.split()





    for key, values in patterns.items():


        best_score = 0

        best_value = None





        for value in values:


            value = value.lower().strip()



            # ignore tiny useless entities

            if value in IGNORE_WORDS:

                continue





            # ======================
            # EXACT WORD MATCH
            # ======================

            if value in words:


                best_value = value

                best_score = 100

                break





            # ======================
            # FUZZY MATCH
            # ======================

            for word in words:


                if word in IGNORE_WORDS:

                    continue



                score = fuzz.ratio(
                    word,
                    value
                )



                if score > best_score:

                    best_score = score

                    best_value = value






        if best_score >= 75:


            entities[key] = best_value





    command.entities = entities


    return command