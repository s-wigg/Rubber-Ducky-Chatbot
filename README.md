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
* [Markov Chains: The Imitation Game](http://www.cyber-omelette.com/2017/01/markov.html)
* [ML Basics: Markov Models Write Fairy Tales](http://thagomizer.com/blog/2017/11/07/markov-models.html)

#### Conversation Flow Diagram
[![Conversation Flow Diagram](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.xml#R1Vxtc5s4EP41nmm%2FdIxlcPyxSdNeZ%2B6ll0yn148KyKALRlQScXK%2F%2FvSGAQmnxCW8dKYtLALEs6tHq92VF%2BBq%2F%2FiJwjz5g0QoXayW0eMCfFisVlvPE%2F9KwZMW%2BMAIYoojLaoJbvF%2FyAiXRlrgCLFGQ05IynHeFIYky1DIGzJIKTk0m%2B1I2nxrDmPkCG5DmLrSbzjiiZZe%2BMtK%2FhvCcVK%2B2VuaK3cwvI8pKTLzvsUK7NQffXkPy2eZ9iyBETnUROB6Aa4oIVwf7R%2BvUCqhLWHT9308cfXYb4oy3uUGX9%2FwANMClT1W%2FeJPJRYoEtCYU0J5QmKSwfS6kl6q70XyiUtxlvB9Kg49cfgv4vzJaBcWnAhR9YTfCclNO7fX5kMYKWho%2BmF6JrtTa2M%2B6xMie8Tpk2hAUQo5fmhqEhqDiI%2Ftjrd%2BIVi8dbU0trsuVWNM19ssm4%2FgkMaIm7sqaMVBrRuVSAHeDv6qBfwgFQhcshxm4jiWx1cJCu9Fs4IhKm%2FO8oIrm6YL8L68Qbyqfo%2BjRGFnuTxM0CMU6IsmOaJY9FU88yj9UooENpeHBHN0m0MF%2F0GM8qZqT6rsAVGOHp%2FVkLkKAgtpc3qoRpxXKiOpjbaL5WmdNrTxDPTlu%2BZg%2BIEhQGV3hmD7HgtdcVttZofbaxPG0R6NGR%2B5vX%2FCCDoRxucsTAs5fQqbSZAcUIRGC9mr4EchJ5bL2wTeI5YjgV8lFC0I1XNUmKi7q2tREd4LCK7UZXpPHuTcm0CcSUHjGd3oqGkAI1DNxZBcA%2BYzZrYu13i9T7ydgWuz9xkB548F3PalPCE%2BjuOwSCFNZYcYyhhWPXLcjjcnh7gW41KA36F3tbbYbmjdDPdy1Gd3TP73Wfo3SC0piozBnewHlG9PBBZv50IyYNWRZIIeSGY1I4emHBiNwTKaSwPa3PAZIVcurUfgZ3f1%2BC1BwufQhKHYRb5Ceglkt5Ok8lDzR968hDMa%2FEBhiKHsCUsLWvot7CD8GfP0t5Mjg3UwIBmUJlFTzI3w90jGJPwoC4VJwRhnccXvwjClheQJhUwrTajoowI2Fiik2oBysUBUV3T7QjXdE%2BlGaoUbDacwi2ERo1KZEX6w%2Bf%2BO2hLxvka7kTXo2XS%2B7ahBD%2FTB53NipRbnZzUaK4GLeSMHNqPxues3fqIIcUUUE%2BPTYDkkn7pRjxvEC5opLRyJdUfJXn4nRRHa4QxFypXmavaTPGqwZKOD6Y8J5mo9n%2FF5TD7UmQ2MNT7XM%2FLx25AD44UtXYfoWrkxamCGJBNjh4lXEjmiOcVxjEpXcvzRalPfZj0k9blzwhnUZyGMsmgSPGi7eMMiOyceBC2jeTwenJFv3IbcejTfeOWGom%2BL3Q6HuFzjZSiGJvLHhAzvkclaTIkBL7qG7%2FsYp2swWePq35DaU1wb38LfxrW%2FFNfanam%2FQaanlgdMCtacd8pYBlJ2Cj6Obqq2az2oqYIZJUxA25QyWsZk3ZYymRFy64uxkAPulPJ3gZjx9OAdUWmjDzqBPLF5xFsOmaLxZ1Rs1b89tc8sF7ZC1t1mlveUwqdas1w2YC94z8aqi%2BvYr0rVugdnT3NukPK5aa45jCYwzdkrp4FHkrt0OmNRehLfscG1KhC3myGhnVH0HLRkQ%2F3Roucl%2BrNFbrwMfIc8siREmXqEnKhOxITEqV6lQhom4uAePel4nayKrdWuJSjN6xVqV42r5XNOXY9IWMi1hQldnWrGEnJY2LVwU%2FN2vK45aM%2FrgUmCGUVp%2Brf9drcisIvLnQLDHotFZxRfLPGv81EwWnzRdxeDzzpn4u%2BP2pJHJRassrkai9UYQjpytfJbfSeWjVKS6RQET1T5DFhMNRvhAX9QVplRiCNoWagHo4U4ghl5dq3IjefZuSGOyj%2BpyuUlD7AcmdK0UNdR3aD4%2BnEKKzZn3Ppdk139jNteSigKQaO6yq%2B8Z4KEuAGDAus6z0dgrZlJTEKE5oRC3ij9M3PUyDDagfOB7dN%2Fxj5TnMkNeKrk8ZZDtRvvL%2FFlu1Q5%2FTBjBwXknRjy0mAV2NMGd9ilQLmF5CcbEm5QrnKQpwtUOUyPmoCKBRTX5oiyRrhZ73uqb2PAjBVoqjsHbPUMu3OgzS9wlfOVaXUYCikZubGVbHkr92NzdvRlnc1iMBUOAcU82esVtAm4iQ9VfQqFQrl8kNpQXRaK5wTJSWFH6FG12ihetvc1pyREjA0TH%2FVtL7nrePN7UOnaXfp9n8BMGYAmKNuWlcO6BRN7Q%2BVZkLjT5J9kdEQ2yyYibdniV0PEXUmd4ZE1E%2FBj4xlsm3huutbs91Io0mVvdBa9l79PIc7CFDKGwyYG6BHzfyRc73xz9v1n6JxVEFLDw2%2BBo5T9YrjLYcHV1sJZd94Jd7m%2FymBTh%2F2gnvKEdoBu28wT%2FnLez3c9oSkw85Fkjv5hS0X4axGR7y6vJ0DNnkXNVWp6CEi6RLlemUq6VgAMQyVO4PxsJrGf5GzX6olKVrYBlS%2Fqi0sCN0w9BS7x7e%2F2W%2FLXrzVwNi6%2FToBLwMaCJHg9P0%2BcVj8fpa2q%2BokucP0%2F)

This project is licensed under the [MIT License](https://github.com/s-wigg/Rubber-Ducky-Chatbot/blob/master/LICENSE).
