########################################################################################################################
# IMPORTS

import time
from traceback import print_exc

from .input.targets import RAW_TARGETS, DIRECT_REFERENCES, FALSE_DIRECT_REFERENCES
from .lib.tweepy_lib import TweepyLib
from .listeners.tweet_listener import TweetReader


########################################################################################################################
# REQUEST FUNCTIONS

def send_answer(text, author, tweet_id, acolyte=None):
    api = TweepyLib()

    user_head = '@'
    space = ' '
    if acolyte is not None:
        api.api.update_status(user_head + author + space + user_head + acolyte + space + text, tweet_id)
    else:
        api.api.update_status(user_head + author + space + text, tweet_id)


def run(request):
    api = TweepyLib()
    api.get_stream(TweetReader(RAW_TARGETS, DIRECT_REFERENCES, FALSE_DIRECT_REFERENCES))

    while True:
        try:
            # Filter tweets
            api.stream.filter(track=RAW_TARGETS)
        except:
            print_exc()
            time.sleep(15)
