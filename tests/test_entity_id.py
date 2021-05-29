from entity_id import __version__
import entity_id
import json


def test_version():
    assert __version__ == "0.1.0"


def test_english():
    en = entity_id.english

    with open("data/1.txt", "r") as fd:
        content = fd.read()
        ents = en.find_entities(content)

    for ent in ents["PERSON"]:
        if "Tracey West" in ent:
            break
    else:
        assert False, "Can't find entity Tracy West"
