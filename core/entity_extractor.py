from rapidfuzz import fuzz

from core.entity_registry import load_entities


ENTITY_REGISTRY = load_entities()


print(ENTITY_REGISTRY)



def extract_entities(command):

    text = command.normalized.lower()

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


            # normal match

            if value in text:

                best_value = value
                best_score = 100
                break



            # fuzzy match

            for word in words:

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