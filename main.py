import json
import requests
from flask import jsonify
from flask import Flask, render_template,request
from sentiment_review.predictions import predict
from sentiment_review.load_into_bigquery import load_to_bigquery
from sentiment_review.send_email import email
import logging
app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@app.route('/',  methods=['GET', 'POST'])
def hello_form():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            review = request.form['review']
            email_form=request.form["email"]
            r= predict(review)
            app.logger.info("review: %s", r)
            
            load_to_bigquery("reviews.predictions",review,r)
            
            email(email_form,r)
            
            if r == 0:
                sentiment="Negative Review"
            else:
                sentiment= "Positive Review"

            json_review=(f"Review: {review}, Sentiment: {sentiment}. Please Check your email for message from company. Thank you for the review!")
            return jsonify(json_review)

        except:
            errors.append(
                "Unable to get prediction."
            )
    return render_template('text_form.html',errors=errors, results=results)

@app.route('/hello/<name>')
def echo(name):
    print(f"This was placed in the url: {name}")
    val = {"Greeting": f"Hello {name}!"}
    return jsonify(val)

@app.route('/json/<name>')
def test(name):
    return json.dumps(f"Hi {name}!")


if __name__=='__main__':
    app.run(host='127.0.0.1', port=8088, debug=True)
