import os
import tweepy

# fetch the secrets from our virtual environment variables
CONSUMER_KEY = os.environ['TWITTER_API_KEY']
CONSUMER_SECRET = os.environ['TWITTER_API_SECRET_KEY']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

# authenticate to the service we're accessing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create the connection
api = tweepy.API(auth)

# define a handle to inspect for quicker reference
handle = 'twitter'  # for example purposes; prop any handle you want!
user = api.get_user(handle)

num_friends = user.friends_count
print(num_friends)
