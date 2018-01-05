import random
import pytest

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
    sent = "mad mad mad"
    # analyze_input(sent)
    print("IN TEST")
    resp = analyze_input(sent)
    print(previous_responses)
    assert resp not in ENCOURAGEMENT

def test_unclear():
    """The bot should ask clarifying question/noncommital statement if userinput can't be parsed"""
    sent = "1234"
    resp = analyze_input(sent)
    assert resp == UNCLEAR_RESPONSES[3]