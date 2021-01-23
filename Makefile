setup: 
	python3 -m venv ~/.sentiment-reviews

install:
	pip install -r requirements.txt --user

test:
	python3 -m pytest -vv --cov=sentiment_review tests/*.py

lint:
	pylint --disable=R,C tests/*.py sentiment_review/*.py
