import tweepy

consumer_key = 'KkjyU3YeJXatJPSD2tTDvuRiY'
consumer_secret = 'UhegOObBzxdesJzeENPtkCR4lT8BiIZs8Vx5uDOrfd5GVKcd9S'
access_token = '124214588-UcIoUc2a9eKwjXJc6jmWmC6eSxi5iMRVlyz8mpId'
access_token_secret = '8HIEc6wReYuZ8VwKUIeBcJwDf7aXXcUiVL1Jg58CBcXbj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status('Test tweet...')
