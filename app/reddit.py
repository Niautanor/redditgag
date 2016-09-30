"""
this file provides most of the functionality of the application. Reddit posts
are retrieved and converted to embeddable objects using the modules from the
providers package.
"""

import collections
import praw
import re

from . import providers

reddit = praw.Reddit(user_agent='redditgag - a 9gag like interface to reddit posts by /u/niautanor', log_requests=2)

def get_posts(subreddit, after, show_nsfw):
    submissions = list(reddit.get_subreddit(subreddit) \
                             .get_hot(limit=25, params={'after':after}))
    last = submissions[-1].name
    # the reddit api actually returns a 'after' field to allow pagination but
    # praw won't let me access it :/

    return [
        dict(title=s.title,
             permalink=s.permalink,
             original_url=s.url,
             author=s.author,
             subreddit=s.subreddit,
             num_comments=s.num_comments,
             hidden='NSFW' if (s.over_18 and not show_nsfw) else None,
             **providers.get_embeddable(s))
        for s in submissions
    ], last
