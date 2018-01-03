from flask import Flask
from app import app
from slackclient import SlackClient
from textblob import TextBlob
import random

print(app.config['SLACK_TOKEN'])
slack_client = SlackClient(app.config['SLACK_TOKEN'])
# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "you there", "anyone there", "yo")

GREETING_RESPONSES = ["Hello!", "Welcome!", "Hey!", "Hi!", "How can I help?", "Quack quack!"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    print("IN Check for greeting")
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)


def send_message(sentence, channel):
    sentence = TextBlob(sentence)
    response = check_for_greeting(sentence)
    print(response)
    print(channel)
    print(slack_client.api_call("api.test"))
    print(slack_client.api_call("auth.test"))
    slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response,
            as_user=True
            )

    #  slack_client.api_call(
    #         "chat.postMessage",
    #         channel=channel_id,
    #         text=message,
    #         username='pythonbot',
    #         icon_emoji=':robot_face:'
    #     )
