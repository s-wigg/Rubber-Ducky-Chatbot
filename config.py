import os
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info("In config file")
class Config(object):
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN') or 'none'

    SLACK_OUTGOING_WEBHOOK_SECRET = os.environ.get('SLACK_OUTGOING_WEBHOOK_SECRET')

    CSE_ID = os.environ.get('CSE_ID')

    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

    OFFENSIVE_WORDS = set([
        "skank",
        "wetback",
        "bitch",
        "blow job",
        "blowjob",
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
        "shit",
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
        "hooker",
        "damn",
        "god damn",
        "goddamn",
        "fuck",
        "test1234",
        "loser",
        "murder",
        "slaughter",
        "kill"
        ])

    DANGER_WORDS = set([
        "suicidal",
        "suicide",
        "abortion",
        "pregnant",
        "miscarry",
        "miscarriage",
        "abuse",
        "abusive",
        "self-harm",
        "anorexia",
        "bulemia"
        "mental illness",
        "assault",
        "rape",
        "sexual assault",
        "dangertest"
        ])
