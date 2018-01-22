from flask import Flask
from app import app
from slackclient import SlackClient
from textblob import TextBlob

def read_file(filename):
    with open(filename, "r") as file:
        contents = file.read().replace('\n\n',' ')
    return contents


def markov_poem():
    content = read_file("app/shakespeare_sonnets.txt")
    print(content)
