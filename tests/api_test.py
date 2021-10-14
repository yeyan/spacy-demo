import pytest

import entity_id


@pytest.fixture
def client():
    with entity_id.app.test_client() as client:
        yield client


def test_api_home(client):
    resp = client.get("/")

    assert "version" in resp.json and resp.json["version"] == entity_id.__version__
    assert "name" in resp.json and resp.json["name"] == "Entity Identification"


def test_api_english(client):
    with open("data/1.txt") as fd:
        content = fd.read()

    resp = client.post("/api/english", data=content)

    assert "PERSON" in resp.json

    for person in resp.json["PERSON"]:
        if "Tracey West" in person:
            break
    else:
        assert False, "Target entity was not found!"
