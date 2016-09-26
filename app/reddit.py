"""
this file provides most of the functionality of the application. Reddit posts
are retrieved and converted to embeddable objects using the modules from the
providers package.
"""

import collections
import praw
import re

from . import providers

reddit = praw.Reddit(user_agent='redditgag - a 9gag like interface to reddit posts by /u/niautanor')

def get_posts(subreddit):
    submissions = reddit.get_subreddit(subreddit).get_hot(limit=25)
    return [
        dict(title=s.title,
             permalink=s.permalink,
             author=s.author,
             subreddit=s.subreddit,
             **providers.get_embeddable(s))
        for s in submissions
    ]
