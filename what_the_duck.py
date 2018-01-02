import os
from slackclient import SlackClient
from textblob import TextBlob


# setting slack authentication token and bot id as environment variable
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

BOT_ID = os.environ.get("BOT_ID")

slack_client = SlackClient(SLACK_TOKEN)

def sendMessage
