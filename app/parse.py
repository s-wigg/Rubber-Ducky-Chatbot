from flask import Flask
from app import app
from slackclient import SlackClient
from textblob import TextBlob
import collections
from collections import deque
import random

slack_client = SlackClient(app.config['SLACK_TOKEN'])

previous_responses = deque([None, None, None])

# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = [
    "hello",
    "hi",
    "greetings",
    "sup",
    "what's up",
    "hey",
    "you there",
    "anyone there",
    "yo"
]

GREETING_RESPONSES = [
    "Hello!",
    "Welcome!",
    "Hey!",
    "Hi!",
    "How can I help?",
    "Quack quack!"
]

END_KEYWORDS = [
    "bye",
    "kthxbai",
    "BYE!",
    "goodbye",
    "thank",
    "thanks",
    "thx",
    "good bye",
    "ttyl"
]

END_RESPONSES = [
    "Did Ducky help you?",
    "Thanks for talking with me!",
    "Bye!",
    "Fare thee well",
    "ttyl",
    "See you later alligator!",
    "Keep up the good work",
    "Catch you later!",
    "This was fun",
    "Bye friend!"
]

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

DANGER_RESPONSE = [
    "Ducky is sorry. It sounds like you have some serious things going on. Do you think talking to a professional might help?",
    "Ducky likes to help people, but I'm just a duck and some problems might benefit from talking to another human?",
    "Is there someone IRL you could talk to who can help?"
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

PRIMARY_OFFENSIVE = [
    "I'm just a little Ducky. Could you please use less offensive words.",
    "Quack quack! I don't like that kind of talk.",
    "I don't think those are nice words.",
    "Using that word, in that way, can be hurtful to others. You are kind and creative. Can you find a word that more accurately says what you want but isn’t hurtful?",
    "Goodness, we need to find you better words!",
    "Hey, that's not cool!",
    "Let's try being nice",
    "Even if I'm a bot, you can still be nice to me.",
    "Is that the kind of language your family would want you to use?",
    "Would you talk like that in front of your parents?"
]


def check_for_danger_words(sentence):
    sentence_split = sentence.split(' ')
    for word in sentence_split:
        for w in app.config['DANGER_WORDS']:
            if word.lower().startswith(w):
                return random.choice(DANGER_RESPONSE)


def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    print("IN Check for greeting")
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
        else:
            return None


def check_for_end_convo(sentence):
    for word in sentence.words:
        if word.lower() in END_KEYWORDS:
            return random.choice(END_RESPONSES)
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
    return verb


def find_noun(sent):
    """Given a sentence, find the best candidate noun."""
    noun = None

    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NN':  # This is a noun
                noun = w
                break
    return noun


def find_adjective(sent):
    """Given a sentence, find the best candidate adjective."""
    adj = None
    for w, p in sent.pos_tags:
        if p == 'JJ':  # This is an adjective
            adj = w
            break
    return adj


def find_parts_of_speech(sentence):
    """Given a parsed input, find the best pronoun, direct noun, adjective, and verb to match their input.
    Returns a tuple of pronoun, noun, adjective, verb any of which may be None if there was no good match"""
    pronoun = None
    noun = None
    adjective = None
    verb = None
    for sent in sentence.sentences:
        pronoun = find_pronoun(sent)
        noun = find_noun(sent)
        adjective = find_adjective(sent)
        verb = find_verb(sent)
    return pronoun, noun, adjective, verb


def preprocess_text(sentence):
    """Handle some weird edge cases in parsing, like 'i' needing to be capitalized
    to be correctly identified as a pronoun"""
    cleaned = []
    words = sentence.split(' ')
    for w in words:
        if w == 'i':
            w = 'I'
        if w == "i'm":
            w = "I'm"
        if w == "im":
            w = "I'm"
        if '@' in w:
            w = w.replace("@", "")
        if '#' in w:
            w = w.replace("#", "")
        cleaned.append(w)

    return ' '.join(cleaned)


def check_for_offensive(sentence):
    print("In offensive check")
    sentence_split = sentence.split(' ')
    for word in sentence_split:
        for w in app.config['OFFENSIVE_WORDS']:
            if word.lower().startswith(w):
                return random.choice(PRIMARY_OFFENSIVE)

    return None


# if no noun identified and no special case matches
def unclear():
    return random.choice(UNCLEAR_RESPONSES)


def question_builder(pronoun, noun, verb):
    return "Hmm, {} does sound like an interesting problem. What do the logs say?".format(noun)


# check what kind of input and what kind of message should be returned
def analyze_input(sentence):
    cleaned_up_sentence = preprocess_text(sentence)
    sentence = TextBlob(cleaned_up_sentence)

    pronoun, noun, adjective, verb = find_parts_of_speech(sentence)
    print(pronoun)
    print(noun)
    print(adjective)
    print(verb)

    response = check_for_danger_words(sentence)
    if response:
        previous_responses.append("danger")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = check_for_offensive(sentence)
    if response:
        previous_responses.append("offensive")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = check_for_greeting(sentence)
    if response:
        previous_responses.append("greeting")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = check_for_end_convo(sentence)
    if response:
        previous_responses.append("convo end")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = sentiment_analysis(sentence)
    if response:
        previous_responses.append("encouragement")
        previous_responses.popleft()
        print(previous_responses)
        return response

    if noun is None:
        previous_responses.append("unclear")
        previous_responses.popleft()
        return unclear()

    response = question_builder(pronoun, noun, verb)
    if response:
        previous_responses.append("question")
        previous_responses.popleft()
        return response
    else:
        previous_responses.append("unclear")
        previous_responses.popleft()
        print(previous_responses)
        return random.choice(UNCLEAR_RESPONSES)

""" refactor to make a build response method ??"""

def send_message(sentence, channel):
    # cleaned_up_sentence = preprocess_text(sentence)
    # sentence = TextBlob(cleaned_up_sentence)
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
