[![Build Status](https://travis-ci.org/s-wigg/Rubber-Ducky-Chatbot.svg?branch=master)](https://travis-ci.org/s-wigg/Rubber-Ducky-Chatbot)

# What the Duck?! — Rubber Ducky Slack Chatbot

## Why do you need Ducky in your life?
It's 2am and you've hit a roadblock in your code. What the Duck are you supposed to do? Rubber Ducky Slackbot to the rescue! Rubber Ducky can serve as a Rubber Duck for the purposes of thinking through your coding roadblocks. Rubber Ducky can ask you questions and provide links to relevant Stack Overflow questions based on your input. Rubber Ducky will help speed you to the epiphany you're looking for to solve your coding troubles!

## Installation

1. Clone the repo
2. [Create a bot user](https://my.slack.com/services/new/bot) if you don't have one yet, and copy the API Token
3. In the command line type: `export SLACK_TOKEN="your-api-token"`
4. Download and start running [ngrok](https://ngrok.com/). [Helpful ngrok tips](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
5. Once you're running ngrok in a terminal window, copy and paste the forwarding URL into the [Slack Outgoing Webhooks page](https://api.slack.com/custom-integrations/outgoing-webhooks) on the 'outgoing webhook integration' line.
6. On the Slack Outgoing Webhooks page, scroll down to the Integration Settings section. Select “#general” (or whatever channel(s) you want to use Ducky in) as the channel to listen on. Copy your ngrok Forwarding URL plus “/slack” into the URL(s) text box. Copy the generated Token. Scroll down and press the “Save Settings” button. If deploying on AWS (for example Elastic Beanstalk) include that link (plus "/slack") instead or in addition.
7. In the command line type: `export SLACK_OUTGOING_WEBHOOK_SECRET='your-copied-token'`
8. Visit the Google APIs Console <https://console.developers.google.com/apis> to get an API key for your own application. In the command line type: `export GOOGLE_API_KEY='your-copied-token'`
9. Google Custom Search ID from https://cse.google.com/cse. When set the custom search engine will be used instead of Google Web Search. In the command line type: `export CSE_ID='your-copied-token'`
10. If deploying on AWS, environment variables can be set through the Elastic Beanstalk console instead.
11. `pip install -r requirements.txt`
12. `flask run`
13. Invite Ducky into the channel(s) you designated on the Slack Outgoing Webhooks page. Ducky will respond to any message in that channel, so it's recommended to create a separate channel for those

I recommend using a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) so that you are running in a clean environment.

## Ducky Key Words
* Using Ducky's name let's Ducky know you are asking them a question a personal question
* Adding "google", "help", "documentation", or "show me" to your input will cause Ducky to return a link to a Stack Overflow answer

### Documentation

##### Slack Documentation

* [Getting started with Slack apps](https://api.slack.com/slack-apps?utm_source=events&utm_campaign=build-bot-workshop&utm_medium=workshop)  
* [Slack Events API documentation](https://api.slack.com/events?utm_source=events&utm_campaign=build-bot-workshop&utm_medium=workshop)  
* [Slack Web API documentation](https://api.slack.com/web?utm_source=events&utm_campaign=build-bot-workshop&utm_medium=workshop)

##### Documentation for Tools

* [virtualenv](https://virtualenv.pypa.io/en/latest/userguide/)
* [flask](http://flask.pocoo.org/)
* [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/)
* [ngrok](https://ngrok.com/docs)

#### Thank Yous
The following tutorials were particularly helpful in the development of this project:

* [Brobot by Liza Daly](https://apps.worldwritable.com/tutorials/chatbot/)
* [Getting Started With the Slack API Using Python and Flask by Matt Makai](https://realpython.com/blog/python/getting-started-with-the-slack-api-using-python-and-flask/)
* [Implementing the Famous ELIZA chatbot in Python by Evan Dempsey](https://www.smallsurething.com/implementing-the-famous-eliza-chatbot-in-python/)

This project is licensed under the [MIT License](https://github.com/s-wigg/Rubber-Ducky-Chatbot/blob/master/LICENSE).
