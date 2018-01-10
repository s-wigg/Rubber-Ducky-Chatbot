from flask import Flask
from app import app
from slackclient import SlackClient
from textblob import TextBlob
import collections
import logging
import re
from collections import deque
import random
import pprint
from googleapiclient.discovery import build

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

if not app.config['SLACK_TOKEN']:
    raise Exception("NO SLACK TOKEN")

slack_client = SlackClient(app.config['SLACK_TOKEN'])

previous_responses = deque([None, None, None])

# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = [
    "hello",
    "hi",
    "greetings",
    "sup",
    "what's up",
    "hey",
    "you there",
    "anyone there",
    "yo"
]

GREETING_RESPONSES = [
    "Hello!",
    "Welcome!",
    "Hey!",
    "Hi!",
    "How can I help?",
    "Quack quack!"
]

END_KEYWORDS = [
    "bye",
    "kthxbai",
    "BYE!",
    "goodbye",
    "thank",
    "thanks",
    "thx",
    "good bye",
    "ttyl"
]

END_RESPONSES = [
    "Did Ducky help you?",
    "Thanks for talking with me!",
    "Bye!",
    "Fare thee well",
    "ttyl",
    "See you later alligator!",
    "Keep up the good work",
    "Catch you later!",
    "This was fun",
    "Bye friend!"
]

UNCLEAR_RESPONSES = [
    "Quack quack?",
    "Sorry, I'm not sure I understand. Can you explain to to me again?",
    "Hmm, that does sound frustrating",
    "I'm a little lost...",
    "Yea, I'm confused too.",
    "Uhm, I'm not sure...",
]

ENCOURAGEMENT = [
    "Programming can be so frustrating sometimes, but you've solved so many challenges before. I know you'll figure this one out too!",
    "It's ok! If debugging is the process of removing software bugs, then programming must be the process of putting them in.",
    "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime. You are not alone.",
    "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it.",
    "Maybe taking a break would give you a fresh perspective?",
    "Coding is hard. And that's ok!",
    "Be kind to yourself. You are not your code.",
    "Ice cream usually helps me!",
    "Would you like a hug?"
]

DANGER_RESPONSE = [
    "Ducky is sorry. It sounds like you have some serious things going on. Do you think talking to a professional might help?",
    "Ducky likes to help people, but I'm just a duck and some problems might benefit from talking to another human?",
    "Is there someone IRL you could talk to who can help?"
]

# If the user says something about duckybot
COMMENTS_ABOUT_SELF = [
    "I am just a Rubber Duck so I have many limitations",
    "I prefer stale bread, but maybe you'd like a cup of tea?",
    "I am open to the abundance of the universe.",
    "Where I am right now is exactly where I need to be.",
    "I honor the light in you.",
    "Everything I need is within me",
    "My favorite color is sunflower yellow. Why do you ask?",
    "My favorite language is Python (but real snakes scare me!)",
    "I'm just ducky! Thanks for asking.",
    "I'm too shy for selfies!"
]

PRIMARY_OFFENSIVE = [
    "I'm just a little Ducky. Could you please use less offensive words.",
    "Quack quack! I don't like that kind of talk.",
    "I don't think those are nice words.",
    "Using that word, in that way, can be hurtful to others. You are kind and creative. Can you find a word that more accurately says what you want but isn’t hurtful?",
    "Goodness, we need to find you better words!",
    "Hey, that's not cool!",
    "Let's try being nice",
    "Even if I'm a bot, you can still be nice to me.",
    "Is that the kind of language your family would want you to use?",
    "Would you talk like that in front of your parents?"
]


def check_for_danger_words(sentence):
    sentence_split = sentence.split(' ')
    for word in sentence_split:
        for w in app.config['DANGER_WORDS']:
            if word.lower().startswith(w):
                return random.choice(DANGER_RESPONSE)


def check_for_greeting(sentence):
    """If user's input was a greeting, return a greeting response"""
    logger.info("IN Check for greeting")
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
        else:
            return None


def check_for_end_convo(sentence):
    for word in sentence.words:
        if word.lower() in END_KEYWORDS:
            return random.choice(END_RESPONSES)
        else:
            return None


def sentiment_analysis(sentence):
    logger.info(sentence.sentiment)
    logger.info(previous_responses)
    if ((sentence.sentiment.polarity < -0.4)
    and (sentence.sentiment.subjectivity > 0.4)
    and (previous_responses[-1] != "encouragement")):
        return random.choice(ENCOURAGEMENT)
    else:
        return None


def find_pronoun(sent):
    """Given a sentence, find a preferred pronoun.
    Returns None if no candidate pronoun found"""
    pronoun = None

    for word, part_of_speech in sent.pos_tags:
        # Disambiguate pronouns
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            # If the user mentioned themselves,
            # then they will definitely be the pronoun
            pronoun = 'You'
    return pronoun


def find_verb(sent):
    """Pick a candidate verb for the sentence."""
    verb = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech.startswith('VB'):  # This is a verb
            verb = word
            break
    return verb


def find_noun(sent):
    """Given a sentence, find the best candidate noun."""
    noun = None

    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NN':  # This is a noun
                noun = w
                break
    return noun


def find_adjective(sent):
    """Given a sentence, find the best candidate adjective."""
    adj = None
    for w, p in sent.pos_tags:
        if p == 'JJ':  # This is an adjective
            adj = w
            break
    return adj


def find_parts_of_speech(sentence):
    """Given a parsed input, find the best pronoun, direct noun,
    adjective, and verb to match their input.
    Returns a tuple of pronoun, noun, adjective,
    verb any of which may be None if there was no good match"""
    pronoun = None
    noun = None
    adjective = None
    verb = None
    for sent in sentence.sentences:
        pronoun = find_pronoun(sent)
        noun = find_noun(sent)
        adjective = find_adjective(sent)
        verb = find_verb(sent)
    return pronoun, noun, adjective, verb


def about_self(sentence, pronoun):
    if ("?" in sentence) and (pronoun == "I" or "your" in sentence):
        return random.choice(COMMENTS_ABOUT_SELF)


def preprocess_text(sentence):
    """Handle some weird edge cases in parsing, like 'i' needing to be capitalized
    to be correctly identified as a pronoun"""
    cleaned = []
    words = sentence.split(' ')
    for w in words:
        if w == 'i':
            w = 'I'
        if w == "i'm":
            w = "I am"
        if w == "im":
            w = "I am"
        if '@' in w:
            w = w.replace("@", "")
        if '#' in w:
            w = w.replace("#", "")
        cleaned.append(w)

    return ' '.join(cleaned)


def check_for_offensive(sentence):
    logger.info("In offensive check")
    sentence_split = sentence.split(' ')
    for word in sentence_split:
        for w in app.config['OFFENSIVE_WORDS']:
            if word.lower().startswith(w):
                return random.choice(PRIMARY_OFFENSIVE)

    return None


# if no noun identified and no special case matches
def unclear():
    return random.choice(UNCLEAR_RESPONSES)


def google_search(sentence):
    service = build("customsearch", "v1",
                    developerKey=app.config['GOOGLE_API_KEY'])

    res = service.cse().list(
        q=sentence,
        cx=app.config['CSE_ID'],
        ).execute()
    if res['items']:
        result = res['items'][0]['title'] + "\n" + "<" + res['items'][0]['link'] + ">"
    logger.info(result)
    return result
    # pprint.pprint(res)


reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

cs_babble = [

    [r'(.*)(frontend|backend|front-end|back-end)(.*)',
     ["Hmm, Ducky's more of a full stack Duck-veloper.",
      "Do you prefer frontend or backend?",
      "Have you done integration testing?"]],

    [r'(.*)database(.*)',
     ["What's up with your database?",
      "Do you need to migrate your database?",
      "Should you reset the database?",
      "Ugh, data overload!",
      "Is it the structure that's the problem?",
      "Is there a way to make your database faster?",
      "Does the data your importing match the model?",
      "Is your CSV file the problem?"]],

    [r'(.*)docker(.*)',
     ["Ducky lives in a Docker container!",
      "Docker images are confusing!",
      "Docker images are extensible, but Ducky is not :("]],

    [r'(.*)whiteboard(.*)',
     ["Ooof, whiteboard!",
      "Can you reverse a string for me?",
      "Just keep talking!",
      "My nightmares involve being asked to balance a binary tree."]],

    [r'(.*)javascript(.*)',
     ["Java is to javascript as car is to carpet.",
      "Is it an ansynchoronos problem?",
      "What is this?",
      "But really, what is this?",
      "Could jQuery fix it?",
      "Are you missing a semicolon?",
      "Sometimes Ducky feels like a fatal token too."]],

    [r'(.*)java(.*)',
     ["Java is to javascript as car is to carpet.",
      "Ducky wants to learn a strictly typed language.",
      "I'm sorry your java is giving you trouble.",
      "Should Ducky learn Java too?",
      "Is it because it's immutable?",
      "Do you think it's a memory leak?"]],

    [r'(.*)(react|native|angular)(.*)',
     ["What backend are you using?.",
      "Ducky has definitely heard that {0} can be a problem!",
      "Have you checked Stack Overflow for {0}."]],

    [r'(.*)app(.*)',
     ["Tell me about your app!",
      "Can I get your app in the App store?",
      "What does your app do?",
      "Where did you get the idea for your app?"]],

    [r'(.*)(TDD|test)(.*)',
     ["Ducky thinks TDD is the best thing since stale bread!",
      "Passing tests make Ducky feel on top of the world. Failing tests make Ducky determined to fix them!",
      "What's the error message say?",
      "Did you google the error message?"]],

    [r'(.*)(strict|typed)(.*)',
     ["Ducky wants to learn a strictly typed language.",
      "I'm sorry your java is giving you trouble.",
      "Did you declare your variables properly?",
      "Is it because it's immutable?",
      "Do you think it's a memory leak?"]],

    [r'(.*)error(.*)',
     ["Did you google that error?",
      "What does the error tell you?",
      "What do you think is causing the error?",
      "What have you tried to fix the error?",
      "What else could you try?",
      "Is the server running?"]],

    [r'(.*)(nil|null|none)(.*)',
     ["Yep, that definitely sounds like a problem",
      "What does the error tell you?",
      "What do you think is causing the error?"]],

    [r'(.*)ruby(.*)',
     ["Did you forget an 'end'?",
      "What's the error message say?",
      "Did you check the Ruby documentation for {0}?",
      "Did you search Stack Overflow for Ruby and {0}?"]],

    [r'(.*)python(.*)',
     ["Did you forget a colon?",
      "Have you checked the Python documentation?",
      "Hmmm, tell me more about your python problems",
      "Did you google python and {0}?",
      "Do you like programming in python?"]],

    [r'(.*)code(.*)',
     ["Tell me more about your code?",
      "Can you walk me through your code?",
      "Don't forget that coding is fun even when it's frustrating sometimes.",
      "And then what did you try?",
      "Did you check Stack Overflow?",
      "Are there any error logs to look at?"]],

    [r'(.*)firewall(.*)',
     ["Yea, it's always the firewall?",
      "Ugh, firewalls.",
      "A firewall is a digital wall that prevents users from doing what they want"]],

    [r'(.*)hack(.*)',
     ["Do you think that's a good idea?",
      "Is this something you're sure is a good idea?",
      "Is this illegal?",
      "Ducky is a quacker but not a hacker"]],

    [r'(.*)internet(.*)',
     ["Did you turn the wifi off and back on again?",
      "Is it the firewall?",
      "The internet is a big pond for a little Ducky like me.",
      "Many things on the internet scare me."]],

    [r'(quit|give up)',
     ["Don't quit!",
     "Don't give up!",
     "Persevere! You've solved so many bugs in the past. Odds are with you that you can solve this one too.",
     "May the odds be ever in your favor!",
      "You shouldn't quit, but sometimes a break can help.",
      "Maybe a break will give you some fresh perspective?"]],

    [r'I need help (.*)',
     ["Who can help you with {0}?",
      "Can the internet help you with {0}?",
      "What about {0} isn't working?",
      "Did you check the logs for {0}?"]],

    [r'Why don\'?t you ([^\?]*)\??',
     ["Would it help if I could {0}?",
      "Is {0} something a Ducky should be able to do?",
      "I really want to help. I'd {0} if I could."]],

    [r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "What do you think it would fix if you could {0}?",
      "I don't know -- why can't you {0}?"]],

    [r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Is there another way to {0}",
      "Can you try a different way to {0}?",
      "Have you checked Stack Overflow for {0}?"]],

    [r'(.*)stuck on(.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]],

    [r'(.*) isn\'?t working',
     ["What's wrong with {0}?",
      "What are some reasons it might not be working?",
      "Is there something else you haven't tried?",
      "Can you think about it from a different perspective?",
      "What else can you do to figure out why {0} isn't working?"]],

    [r'Are you ([^\?]*)\??',
     ["How does whether I am {0} affect your code?",
      "Does your code care if I am {0}?",
      "If I am {0} what would that mean for the project?"]],

    [r'Because (.*)',
     ["Are you sure that's the reason?",
      "What other explanations come to mind?",
      "Does that reason apply to anything else?",
      "If {0}, what else must be true?"]],

    [r'(.*)sorry(.*)',
     ["There are many times when no apology is needed.",
      "I'm sorry too."]],

    [r'I think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "But you're not sure {0}?",
      "How can you confirm your hypothesis?"]],

    [r'(.*)friend (.*)',
     ["Can your friend help?.",
      "Phone a friend?",
      "Is Ducky your friend?"]],

    [r'Yes',
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]],

    [r'(.*)computer(.*)',
     ["Is it a hardware issue?",
      "Have you tried restarting it to fix {0}?"]],

    [r'Is it (.*)',
     ["Do you think it is {0}?",
      "Perhaps it's {0} -- what do you think?",
      "If it were {0}, what would you do?",
      "If it were {0}, how would you go about fixing it?"
      "It could well be that {0}. How can you check?"]],

    [r'It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what else would you try?"]],

    [r'Can you ([^\?]*)\??',
     ["Ducky probably can't, but can you {0}?",
      "If I could {0}, what would you do next?",
      "Did you already try {0}?"]],

    [r'Can I ([^\?]*)\??',
     ["Ducky probably can't, but could you {0}?",
      "What would change if I could {0}?",
      "How would it help if I could {0}?"]],

    [r'You are (.*)',
     ["Why do you think I am {0}?",
      "Does it please you to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Perhaps you're really talking about yourself?"]],

    [r'You\'?re (.*)',
     ["How does me being {0} pertain to your code?",
      "Does your code care that I'm {0}?",
      "Are we talking about me or your code?"]],

    [r'I don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?",
      "Do you want to {0}?"]],

    [r'I feel (.*)',
     ["Do you often feel {0}?",
      "What's making you feel {0}?",
      "Since you feel {0}, what can you do about it?"]],

    [r'Why doesn\'?t (.*)',
     ["Why do youthink {0}?"]],

    [r'Why (.*)',
     ["Why do you think {0}?"]],

    [r'I want (.*)',
     ["How would {0} help your project?",
      "What differene does {0} make for your code?",
      "How would it work if it {0}?",
      "If you got {0}, then what would you do?"]]
]


def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


def question_builder(sentence, noun, pronoun):
    logger.info("in question_builder")
    for pattern, responses in cs_babble:
        print(pattern)
        match = re.match(pattern, sentence, re.IGNORECASE)
        print(match)
        if match:
            response = random.choice(responses)
            print(response)
            print(match.groups())
            return response.format(*[reflect(match.groups()[1]
                                   if match.groups()[1]
                                   else match.groups()[0])])


# check what kind of input and what kind of message should be returned
def analyze_input(sentence):
    logger.info("analyze_input")
    cleaned_up_sentence = preprocess_text(sentence)
    textBlobSentence = TextBlob(cleaned_up_sentence)

    pronoun, noun, adjective, verb = find_parts_of_speech(textBlobSentence)

    # this will need to move to more approp place eventually
    response = google_search(cleaned_up_sentence)
    if response:
        previous_responses.append("google")
        previous_responses.popleft()
        print(previous_responses)
        return response
        # will need to return something eventually

    response = check_for_danger_words(textBlobSentence)
    if response:
        previous_responses.append("danger")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = check_for_offensive(textBlobSentence)
    if response:
        previous_responses.append("offensive")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = check_for_greeting(textBlobSentence)
    if response:
        previous_responses.append("greeting")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = check_for_end_convo(textBlobSentence)
    if response:
        previous_responses.append("convo end")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = sentiment_analysis(textBlobSentence)
    if response:
        previous_responses.append("encouragement")
        previous_responses.popleft()
        print(previous_responses)
        return response

    response = question_builder(cleaned_up_sentence, noun, pronoun)
    if response:
        previous_responses.append("question")
        previous_responses.popleft()
        return response

    response = about_self(textBlobSentence, pronoun)
    if response:
        previous_responses.append("about ducky")
        previous_responses.popleft()
        print(previous_responses)
        return response
    else:
        previous_responses.append("unclear")
        previous_responses.popleft()
        print(previous_responses)
        return random.choice(UNCLEAR_RESPONSES)


def send_message(sentence, channel):
    response = analyze_input(sentence)
    # print(response)
    # print(channel)
    # print(slack_client.api_call("api.test"))
    # print(slack_client.api_call("auth.test"))
    slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response,
            as_user=True
            )
