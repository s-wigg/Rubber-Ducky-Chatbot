from flask import Flask
from app import app
from slackclient import SlackClient
from textblob import TextBlob
from collections import deque
import random

slack_client = SlackClient(app.config['SLACK_TOKEN'])

previous_responses = deque([None, None, None])

# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "you there", "anyone there", "yo")


GREETING_RESPONSES = ["Hello!", "Welcome!", "Hey!", "Hi!", "How can I help?", "Quack quack!"]


UNCLEAR_RESPONSES = [
    "Quack quack?",
    "Sorry, I'm not sure I understand. Can you explain to to me again?",
    "Hmm, that does sound frustrating",
    "I'm a little lost...",
    "Yea, I'm confused too.",
    "Uhm, I'm not sure...",
]

ENCOURAGEMENT = [
    "Programming can be so frustrating sometimes, but you've solved so many challenges before. I know you'll figure this one out too!",
    "It's ok! If debugging is the process of removing software bugs, then programming must be the process of putting them in.",
    "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime. You are not alone.",
    "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it.",
    "Maybe taking a break would give you a fresh perspective?",
    "Coding is hard. And that's ok!",
    "Be kind to yourself. You are not your code.",
    "Ice cream usually helps me!",
    "Would you like a hug?"
]

# If the user says something about duckybot
COMMENTS_ABOUT_SELF = [
    "I am just a Rubber Duck so I have many limitations",
    "I prefer stale bread, but maybe you'd like a cup of tea?",
    "I am open to the abundance of the universe.",
    "Where I am right now is exactly where I need to be.",
    "I honor the light in you.",
    "Everything I need is within me"
]


def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    print("IN Check for greeting")
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
        else:
            return None

def sentiment_analysis(sentence):
    print(sentence.sentiment)
    print(previous_responses)
    if (sentence.sentiment.polarity < -0.1) and (sentence.sentiment.subjectivity > 0.3) and (previous_responses[-1] != "encouragement"):
        return random.choice(ENCOURAGEMENT)
    else:
        return None

def find_pronoun(sent):
    """Given a sentence, find a preferred pronoun to respond with. Returns None if no candidate pronoun is found in the input"""
    pronoun = None

    for word, part_of_speech in sent.pos_tags:
        # Disambiguate pronouns
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            # If the user mentioned themselves, then they will definitely be the pronoun
            pronoun = 'You'
    return pronoun


def find_verb(sent):
    """Pick a candidate verb for the sentence."""
    verb = None
    pos = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech.startswith('VB'):  # This is a verb
            verb = word
            pos = part_of_speech
            break
    return verb, pos


def find_noun(sent):
    """Given a sentence, find the best candidate noun."""
    noun = None

    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NN':  # This is a noun
                noun = w
                break
    if noun:
        logger.info("Found noun: %s", noun)

    return noun

def find_adjective(sent):
    """Given a sentence, find the best candidate adjective."""
    adj = None
    for w, p in sent.pos_tags:
        if p == 'JJ':  # This is an adjective
            adj = w
            break
    return adj

def analyze_input(sentence):
    response = check_for_greeting(sentence)
    if response:
        previous_responses.append("greeting")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = sentiment_analysis(sentence)
    if response:
        previous_responses.append("encouragement")
        previous_responses.popleft()
        print(previous_responses)
        return response
    else:
        previous_responses.append("unclear")
        previous_responses.popleft()
        print(previous_responses)
        return random.choice(UNCLEAR_RESPONSES)

""" refactor to make a build response method ??"""

def send_message(sentence, channel):
    sentence = TextBlob(sentence)
    response = analyze_input(sentence)
    # response = check_for_greeting(sentence)
    # print(response)
    # print(channel)
    # print(slack_client.api_call("api.test"))
    # print(slack_client.api_call("auth.test"))
    slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response,
            as_user=True
            )
