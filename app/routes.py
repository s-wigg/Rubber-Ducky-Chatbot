import os
from flask import Flask, request, Response
from app import app
from app.parse import send_message


@app.route('/slack', methods=['POST'])
def inbound():
    print("in INBOUND")
    if request.form.get('token') == app.config['SLACK_OUTGOING_WEBHOOK_SECRET']:
        channel = request.form.get('channel_id')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
        if username != 'ducky':
            send_message(text, channel)
    # return Response(), 200
    return Response(text, status=200)


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)
