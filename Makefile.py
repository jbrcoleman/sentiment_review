setup:
    python3 -m venv ~/sentiment-reviews

install:
    pip install -r requirements.txt

test:
    PYTHONPATH=. && pytest -vv --cov=sentiment_reviews tests/*.py

lint:
    pylint --disable=R,C sentiment_reviews
