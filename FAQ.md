# Ducky FAQ

## Why did you make Ducky?

I wanted to play with some natural language processing tools and techniques and also make a bot that grapples with some ethical consideration.

## What can Ducky do?

Ducky specializes in largely domain specific conversation related to coding, computers, and software development. Ducky can generate responses based on coding key words and can also return search results based on user input from Stack Overflow. Ducky can generate unique 100-word Shakespearian-style poems. Ducky can offer encouragement to the user where user input is sufficiently negative. Ducky can respond to greetings and end of conversation phrases and a limited variety of general conversational phrases. The best way to figure out what Ducky can do is just chat to Ducky and meet Ducky for yourself!

## Why is Ducky a Duck?

Making Ducky a Rubber Ducky fits with the coding specific domain of the Slackbot. According to the [Wikipedia entry on Rubber Duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging) "The name is a reference to a story in the book [The Pragmatic Programmer](https://pragprog.com/book/tpp/the-pragmatic-programmer) in which a programmer would carry around a rubber duck and debug their code by forcing themselves to explain it, line-by-line, to the duck."

Additionally, making Ducky an inanimate object avoids the trends toward making bots that impersonate women or teenagers with the unfortunate implication that those kinds of people are easier to impersonate with a deeply imperfect bot because they are in some way not fully human.

## What ethical considerations did you have to take into account while making Ducky?

There were two types of potential user input that were particularly of concern.

1) Deeply personal and/or serious input. Such as a user saying "I feel unsafe at home" or "I'm thinking about self-harm."

It beyond the scope of this project to provide any meaningful support in this situation, but Ducky is programmed to at least be aware that this is a possibility, to monitor for a number of words indicating particularly serious topics, and to offer an appropriate response (i.e. gently suggesting the user talk to a real person instead of Ducky).  

2) Offensive user input.

Unfortunately, bots are all too often subject to abuse. [Companies take a variety of approaches in response](https://qz.com/911681/we-tested-apples-siri-amazon-echos-alexa-microsofts-cortana-and-googles-google-home-to-see-which-personal-assistant-bots-stand-up-for-themselves-in-the-face-of-sexual-harassment/). I very intentionally did not want to Ducky to just ignore abuse. I settled on having Ducky either gently reprimand or attempt to more positively redirect the conversation.
