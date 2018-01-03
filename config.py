import os

print("In config file")
class Config(object):
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN') or 'none'

    BOT_ID = os.environ.get("BOT_ID") or 'none'

    SLACK_OUTGOING_WEBHOOK_SECRET = os.environ.get('SLACK_OUTGOING_WEBHOOK_SECRET')
