import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_text = 'Would you like to add a task?'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('YesIntent')
def yes():
    speech_text = 'What is the task you would like to add?'
    return statement(speech_text).simple_card('yes', speech_text)

@ask.intent('NoIntent')
def no():
    speech_text = 'What would you like to do then stupid?'
    return statement(speech_text).simple_card('no', speech_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can add a task if you so desire.'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
