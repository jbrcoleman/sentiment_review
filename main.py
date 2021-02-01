import json
from flask import jsonify
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_form():
    return render_template('text_form.html')

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
