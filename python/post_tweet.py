import tweepy
import json

keys_file = 'keys_file.json'
api_keys = {}
with open(keys_file, 'r') as file:
    api_keys = json.loads(file.read())
consumer_key = api_keys['consumer_key']
consumer_secret = api_keys['consumer_secret']
access_token = api_keys['access_token']
access_token_secret = api_keys['access_token_secret']

def post_tweet(tweet):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(tweet)
