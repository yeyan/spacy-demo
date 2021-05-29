PHONY=install

install:
	poetry install
	poetry run python -m spacy download en_core_web_lg

run:
	FLASK_APP=entity_id:app FLASK_DEBUG=1 poetry run flask run

demo:
	@curl -v -H 'content-type: text/plain' --data-binary '@data/1.txt' localhost:5000/api/english

test:
	poetry run pytest
