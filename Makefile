setup:
	python3 -m venv ~/.sentiment
install:
	pip3 install --upgrade pip &&\
	pip3 install -r requirements.txt --user

format:
	python3 -m black sentiment_review/*.py tests/*.py

test:
	python3 -m pytest -vv --cov=sentiment_review tests/*.py

lint:
	python3 -m pylint --disable=R,C tests/*.py sentiment_review/*.py
all: install lint test
