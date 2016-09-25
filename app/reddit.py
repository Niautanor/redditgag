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
    #TODO: support other lists (e.g. new, top)
    #TODO: pagination
    submissions = reddit.get_subreddit(subreddit).get_hot(limit=25)
    posts = []
    for s in submissions:
        for provider in providers.modules:
            post = provider.embed(s)
            if post is not None:
                posts.append(dict(title=s.title, permalink=s.permalink,
                    author=s.author, subreddit=s.subreddit, **post))
                break
    return posts
