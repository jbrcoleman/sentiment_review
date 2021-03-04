import json
import requests
from flask import jsonify
from flask import Flask, render_template,request
from sentiment_review.predictions import predict
app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def hello_form():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            review = request.form['review']
            r= predict(review)
            print(r)
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
    app.run(host='127.0.0.1', port=8080, debug=True)
