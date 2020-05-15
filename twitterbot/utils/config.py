import json


class Config:
    def __init__(self, file):
        self.__dict__ = json.load(file)

    # app consumer credentials
    CONSUMER_KEY = "<your consumer key>"
    CONSUMER_SECRET = "<your consumer secret>"
    # user credentials
    TOKEN_KEY = "<your user token(oauth_token)>"
    TOKEN_SECRET = "<your user token secret(oauth_verifier)>"
    # retweet interval in min
    RETWEET_INTERVAL = 10
    # tweets save
    SAVE_TWEETS = False
    SAVE_TWEETS_PATH = "/tweets"
    # number of elements to skip from track but include as key word
    START_INDEX = 0
    # custom tracks(keywords) up to 400 keywords
    TRACKS = ["computer"]
    # languages of tracked tweets
    LANGUAGES = ["fa"]
    # words to filter out
    FILTER_WORDS = ["sex", "fuck"]
    # users blacklist
    BLACK_LIST = ["45645645646"]
    # telegram channel info
    TELEGRAM = False
    TELEGRAM_BOT_TOKEN = ""
    TELEGRAM_CHANNEL_ID = ""
