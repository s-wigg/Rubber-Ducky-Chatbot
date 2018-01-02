import os
from flask import Flask, request, Response


app = Flask(__name__)

SLACK_OUTGOING_WEBHOOK_SECRET = os.environ.get('SLACK_OUTGOING_WEBHOOK_SECRET')

@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_OUTGOING_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)
