# Rubber-Ducky-Chatbot


## Installation

1. Clone the repo
2. [Create a bot user](https://my.slack.com/services/new/bot) if you don't have one yet, and copy the API Token
3. In the command line type: `export SLACK_TOKEN="your-api-token"`
4. Download and start running [ngrok](https://ngrok.com/). [Helpful ngrok tips](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
5. Once you're running ngrok in a terminal window, copy and paste the forwarding URL into the [Slack Outgoing Webhooks page](https://api.slack.com/custom-integrations/outgoing-webhooks) on the 'outgoing webhook integration' line.
6. On the Slack Outgoing Webhooks page, scroll down to the Integration Settings section. Select “#general” (or whatever channel(s) you want to use Ducky in) as the channel to listen on. Copy your ngrok Forwarding URL plus “/slack” into the URL(s) text box. Copy the generated Token. Scroll down and press the “Save Settings” button.
7. In the command line type: `export SLACK_OUTGOING_WEBHOOK_SECRET='your-copied-token'`
8. `flask run`
9. Invite Ducky into the channel(s) you designated on the Slack Outgoing Webhooks page. Ducky will respond to any message in that channel, so it's recommended to create a separate channel for those

I recommend that you always run limbo in a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) so that you are running in a clean environment.
