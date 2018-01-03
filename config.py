import os

print("In config file")
class Config(object):
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN') or 'none'

    BOT_ID = os.environ.get("BOT_ID") or 'none'

    SLACK_OUTGOING_WEBHOOK_SECRET = os.environ.get('SLACK_OUTGOING_WEBHOOK_SECRET')

    FILTER_WORDS = set([
        "skank",
        "wetback",
        "bitch",
        "cunt",
        "dick",
        "douchebag",
        "dyke",
        "fag",
        "nigger",
        "tranny",
        "trannies",
        "paki",
        "pussy",
        "retard",
        "slut",
        "titt",
        "tits",
        "wop",
        "whore",
        "chink",
        "fatass",
        "shemale",
        "nigga",
        "daygo",
        "dego",
        "dago",
        "gook",
        "kike",
        "kraut",
        "spic",
        "twat",
        "lesbo",
        "homo",
        "fatso",
        "lardass",
        "jap",
        "biatch",
        "tard",
        "gimp",
        "gyp",
        "chinaman",
        "chinamen",
        "golliwog",
        "crip",
        "raghead",
        "negro",
        "hooker"])
