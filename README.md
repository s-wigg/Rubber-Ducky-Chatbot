[![Build Status](https://travis-ci.org/s-wigg/Rubber-Ducky-Chatbot.svg?branch=master)](https://travis-ci.org/s-wigg/Rubber-Ducky-Chatbot)

# What the Duck?! — Rubber Ducky Slack Chatbot

## Who or What is Ducky?
Ducky is a domain specific Slack chatbot to help coders think through their coding challenges, but Ducky also seeks to address common ethical issues with bots such as discouraging abuse and responding appropriately to serious personal comments.

![Say Hello to Ducky](https://github.com/s-wigg/Rubber-Ducky-Chatbot/blob/master/assets/ducky%20general%20demo%202.gif)

## Why do you need Ducky in your life?
It's 2am and you've hit a roadblock in your code. What the Duck are you supposed to do? Rubber Ducky Slackbot to the rescue! Ducky can serve as a [rubber duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging) for the purposes of thinking through your coding blockers. Ducky can ask you questions and provide links to relevant Stack Overflow questions based on your input. Ducky will help speed you to the epiphany you're looking for to solve your coding troubles!

## How to Use Ducky
### Ducky Features
[Screen shots and explanations of Ducky's features](https://github.com/s-wigg/Rubber-Ducky-Chatbot/blob/master/Ducky_demo.md)
### Keywords
* Using Ducky's name signifies you are asking them a question a personal question.
* Adding "google", "help", "documentation", or "show me" to your input will cause Ducky to return a link to a Stack Overflow answer.
* Writing "Ducky, markov chain me" or including the word "Shakespeare" in user input will cause Ducky to generate a 100 word poem in the style of a Shakespeare Sonnet generated using a [Markov Chain](http://setosa.io/ev/markov-chains/).

### FAQ
[FAQ](https://github.com/s-wigg/Rubber-Ducky-Chatbot/blob/master/FAQ.md)

### Conversation Flow Diagram
[Visualization of Ducky's Decision Making Process in Developing Responses to User Input](https://github.com/s-wigg/Rubber-Ducky-Chatbot/blob/master/assets/Conversation%20Flow%20Diagram.jpg)

### Installation

1. Clone the repo
2. [Create a bot user](https://my.slack.com/services/new/bot) if you don't have one yet, and copy the API Token
3. Set your Slack API token via the command line: `export SLACK_TOKEN="your-api-token"`
4. Download and start running [ngrok](https://ngrok.com/). [Helpful ngrok tips](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
5. Once you're running ngrok in a terminal window, copy and paste the forwarding URL into the [Slack Outgoing Webhooks page](https://api.slack.com/custom-integrations/outgoing-webhooks) on the 'outgoing webhook integration' line.
6. On the Slack Outgoing Webhooks page, scroll down to the Integration Settings section. Select “#general” (or whichever channel(s) you want to use Ducky in) as the channel to listen on. Copy your ngrok Forwarding URL plus “/slack” into the URL(s) text box. Copy the generated Token. Scroll down and press the “Save Settings” button. If deploying on AWS (for example Elastic Beanstalk) include that link (plus "/slack") instead or in addition.
7. Set the Slack secret token via the command line: `export SLACK_OUTGOING_WEBHOOK_SECRET='your-copied-token'`
8. Visit the [Google APIs Console](https://console.developers.google.com/apis to get an API key for your application. Set the Google API Key variable via the command line: `export GOOGLE_API_KEY='your-copied-token'`
9. Obtain a [Google Custom Search ID](https://cse.google.com/cse). When set, the custom search engine will be used instead of Google Web Search. Set the Google Custom Search ID via the command line: `export CSE_ID='your-copied-token'`
11. `pip install -r requirements.txt`
12. `flask run`
13. Invite Ducky into the channel(s) you designated on the Slack Outgoing Webhooks page. Ducky will respond to any message in that channel, so it's recommended to create a separate channel for just you and Ducky to talk.

These instructions can be used to develop, run, and test Ducky locally. To deploy Ducky set the necessary environment variables via the established patterns of your system. For example, if deploying on AWS, environment variables can be set through the Elastic Beanstalk console instead.

Using a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is recommended with Python applications.

##### General Slack Documentation

* [Getting started with Slack apps](https://api.slack.com/slack-apps?utm_source=events&utm_campaign=build-bot-workshop&utm_medium=workshop)  
* [Slack Events API documentation](https://api.slack.com/events?utm_source=events&utm_campaign=build-bot-workshop&utm_medium=workshop)  
* [Slack Web API documentation](https://api.slack.com/web?utm_source=events&utm_campaign=build-bot-workshop&utm_medium=workshop)

##### Documentation for Dependencies of the Application

* [virtualenv](https://virtualenv.pypa.io/en/latest/userguide/)
* [flask](http://flask.pocoo.org/)
* [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/)
* [ngrok](https://ngrok.com/docs)

#### Acknowledgements
The following tutorials were particularly helpful in the development of this project:

* [Brobot by Liza Daly](https://apps.worldwritable.com/tutorials/chatbot/)
* [Getting Started With the Slack API Using Python and Flask by Matt Makai](https://realpython.com/blog/python/getting-started-with-the-slack-api-using-python-and-flask/)
* [Implementing the Famous ELIZA chatbot in Python by Evan Dempsey](https://www.smallsurething.com/implementing-the-famous-eliza-chatbot-in-python/)
* [Markov Chains: The Imitation Game](http://www.cyber-omelette.com/2017/01/markov.html)
* [ML Basics: Markov Models Write Fairy Tales](http://thagomizer.com/blog/2017/11/07/markov-models.html)

This project is licensed under the [MIT License](https://github.com/s-wigg/Rubber-Ducky-Chatbot/blob/master/LICENSE).
