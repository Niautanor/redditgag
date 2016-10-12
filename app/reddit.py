"""
this file provides most of the functionality of the application. Reddit posts
are retrieved and converted to embeddable objects using the modules from the
providers package.
"""

import collections
import praw
import re

from . import providers

reddit = praw.Reddit(user_agent='redditgag - a 9gag like interface to reddit posts by /u/niautanor', log_requests=2, cache_timeout=120)

def get_posts(subreddit, after, show_nsfw):
    submissions = list(reddit.get_subreddit(subreddit) \
                             .get_hot(limit=5, params={'after':after}))
    last = submissions[-1].name
    # the reddit api actually returns a 'after' field to allow pagination but
    # praw won't let me access it :/

    return [ (providers.get_embeddable(s, show_nsfw)) for s in submissions], last
