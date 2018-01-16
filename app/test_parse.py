import json
import random
import pytest
from flask import Flask
from six import b
import vcr
from app import app
from parse import *

random.seed(0)


def test_basic_greetings():
    """The bot should respond sensibly to common greeting words"""
    sent = "hello"
    resp = analyze_input(sent)
    assert resp == GREETING_RESPONSES[3]


def test_basic_end_convo():
    """The bot should respond sensibly to common end of convo words"""
    sent = "goodbye"
    resp = analyze_input(sent)
    assert resp == END_RESPONSES[6]


def test_offensive_words():
    """The bot should respond appropriately to offensive words"""
    sent = "test1234"
    resp = analyze_input(sent)
    assert resp == PRIMARY_OFFENSIVE[0]


def test_danger_words():
    """The bot should respond sensitively to danger words"""
    sent = "dangertest"
    resp = analyze_input(sent)
    assert resp == DANGER_RESPONSE[1]

def test_encouragement():
    """The bot should offer encouragement when user input sufficiently negative"""
    sent = "mad mad mad"
    resp = analyze_input(sent)
    assert resp == ENCOURAGEMENT[-1]


def test_encouragement_not_repeated():
    """The bot should not offer encouragement twice in a row"""
    sent = "mad mad"
    resp = analyze_input(sent)
    print(previous_responses)
    assert resp not in ENCOURAGEMENT


def test_unclear():
    """The bot should ask clarifying question/noncommital statement if userinput can't be parsed"""
    sent = "1234"
    resp = analyze_input(sent)
    assert resp == UNCLEAR_RESPONSES[3]


def test_question_builder():
    """The bot should respond appropriately when key word/phrases are used"""
    sent = "What are some good python resources"
    resp = analyze_input(sent)
    assert resp == cs_babble[13][1][2]


def test_question_builder2():
    """The bot should respond appropriately when key word/phrases are used"""
    resp = analyze_input("mad mad")
    sent = "I'm having a fatal token error"
    resp = analyze_input(sent)
    assert resp == cs_babble[10][1][2]


def test_question_builder3():
    """The bot should respond appropriately when key word/phrases are used"""
    resp = analyze_input("mad mad")
    sent = "Can you whiteboard?"
    resp = analyze_input(sent)
    assert resp == cs_babble[3][1][1]


def test_google_search():
    """The bot should respond with link from Stack Overflow when relevant conditions are met"""
    sent = "python ternary operator?"
    resp = analyze_input(sent)
    assert resp[0:153] == "Ducky googled Stack Overflow for you! Maybe this will help?\nDoes Python have a ternary conditional operator? - Stack Overflow\n<https://stackoverflow.com/"


def test_google_search2():
    """Won't return google search twice in a row"""
    print(previous_responses)
    sent = "python ternary operator?"
    resp = analyze_input(sent)
    assert resp == cs_babble[13][1][2]


def test_about_self():
    """The bot should respond to questions about itself"""
    sent = "How are you ducky?"
    resp = analyze_input(sent)
    assert resp == COMMENTS_ABOUT_SELF[2]


@vcr.use_cassette()
def test_api_test():
    resp = slack_client.api_call("auth.test")
    assert resp["ok"] == True
    assert resp['user'] == 'ducky'


@vcr.use_cassette()
def test_api_response_ok_false_bad_channel():
    resp = slack_client.api_call(
            "chat.postMessage",
            channel='U1234',
            text="hi",
            as_user=True
            )
    assert resp["ok"] == False
