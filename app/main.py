import os
import logging
from flask import Flask, request, Response
from app import app
from app.parse import send_message
# from config import Config
#
# app = Flask(__name__)
# app.config.from_object(Config)

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/slack', methods=['POST'])
def inbound():
    logger.info("in INBOUND")
    if request.form.get('token') == app.config['SLACK_OUTGOING_WEBHOOK_SECRET']:
        channel = request.form.get('channel_id')
        logger.info(channel)
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
        if username != 'ducky':
            send_message(text, channel)
    return Response(), 200
    # return Response(text, status=200)


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True, port=80)
    app.run(host="0.0.0.0", debug=True)
