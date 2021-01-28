install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt --user

format:
	black *.py

test:
	python3 -m pytest -vv --cov=sentiment_review tests/*.py

lint:
	python3 -m pylint --disable=R,C tests/*.py sentiment_review/*.py
all: install lint test
