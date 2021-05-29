import spacy

nlp = spacy.load("en_core_web_lg")


def find_entities(corpus):
    doc = nlp(corpus)
    entities = {}

    for ent in doc.ents:
        entity_type = ent.label_
        entity_name = ent.text

        values = entities.get(entity_type, set())
        values.add(entity_name)
        entities[entity_type] = values

    return {key: list(val) for key, val in entities.items()}
