########################################################################################################################
# IMPORTS

import tweepy

from ..keys.keys import CONSUMER_KEY, CONSUMER_SECRET, TOKEN_KEY, TOKEN_SECRET


########################################################################################################################
# CLASSES

class TweepyLib:
    def __init__(self):

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
        self.auth = auth

        self.api = tweepy.API(self.auth)
        self.stream = None

    def get_stream(self, listener):
        self.stream = tweepy.streaming.Stream(self.auth, listener)

    def get_friends(self):
        friends = []
        for page in tweepy.Cursor(self.api.friends).pages():
            friends.extend(page)
        return friends

    def get_followers(self):
        followers = []
        for page in tweepy.Cursor(self.api.followers).pages():
            followers.extend(page)
        return followers

    def get_friends_ids(self, friends):
        friends_ids = []
        for friend in friends:
            friends_ids.append(friend.screen_name)
        return friends_ids

    def get_followers_ids(self, followers):
        followers_ids = []
        for follower in followers:
            followers_ids.append(follower.screen_name)
        return followers_ids
