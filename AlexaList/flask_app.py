from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

def update_tasks():
    pass

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like me to say something interesting?'
    return question(welcome_message)

@ask.intent("YesIntent")
def add_task():
        tasks = update_tasks()
        tasks_msg = 'Fuck you!'
        return statement(tasks_msg)

@ask.intent("NoIntent")
def no_intent():
        bye_text = 'Well, shit.'
        return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
