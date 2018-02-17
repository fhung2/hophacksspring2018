from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/"

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

if __name__ == '__main__':
    app.run(debug=True)
