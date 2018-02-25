########################################################################################################################
# IMPORTS

import tweepy
from django.utils import timezone

from ..models import Tweet, User


########################################################################################################################
# CLASSES

class TweetReader(tweepy.StreamListener):
    def __init__(self, targets, direct_references, false_direct_references):
        tweepy.StreamListener.__init__(self)

        self.targets = targets
        self.direct_references = direct_references
        self.false_direct_references = false_direct_references

        self.status = None
        self.author = None

        self.is_retweet = False
        self.retweet_status = None
        self.retweet_acolyte = None
        self.retweet_count = 0

        self.direct_reference_flag = False

    def on_status(self, status):
        self.status = status

        if hasattr(self.status, 'retweeted_status'):
            self.is_retweet = True

        for target in self.targets:
            if target in self.status.text:
                self.add_member()
                break

    def add_member(self):

        self.add_users()

        self.check_references()

        self.add_tweet()

    def add_users(self):

        if self.is_retweet:
            rt_status = self.status.retweeted_status
            rt_acolyte_author = self.status.author
            author = rt_status.author
            retweet_acolyte = User(name=rt_acolyte_author.screen_name, followers=rt_acolyte_author.followers_count,
                                   place=rt_acolyte_author.location)
            retweet_acolyte.save()
            self.retweet_count = rt_status.retweet_count
        else:
            author = self.status.author
            self.retweet_count = self.status.retweet_count

        self.author = User(name=author.screen_name, followers=author.followers_count, place=author.location)
        self.author.save()

    def check_references(self):
        text_lower = self.status.text.lower()
        if self.check_false_reference(text_lower):
            return

        self.check_direct_reference(text_lower)

    def check_false_reference(self, text):
        for false_reference in self.false_direct_references:
            if false_reference in text:
                return True
        return False

    def check_direct_reference(self, text):
        for reference in self.direct_references:
            if reference in text:
                self.direct_reference_flag = True
                break

    def add_tweet(self):
        tweet = Tweet(pub_date=timezone.now(), tweet_id=self.status.id, author=self.author,
                      retweet_acolyte=self.retweet_acolyte, retweet_count=self.retweet_count,
                      direct_reference=self.direct_reference_flag, text=self.status.text)
        tweet.save()

        print(self.status.text)
