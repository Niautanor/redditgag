"""
This module is responsible for embedding twitter tweets.

Like with most of my embeddable providers, portions of the code (regexes in
particular) come from the Reddit Enhancement Suite
"""

import re

from .. import rest

name = "twitter"
icon = "https://abs.twimg.com/favicons/favicon.ico"

twitter_regex = re.compile(r'^https?://((m|mobile|www)\.)?twitter\.com.*')
twitter_tweet_regex = re.compile(r'^https?://((m|mobile|www)\.)?twitter\.com/(#\!/)?\w{1,15}/status/\d+.*', re.IGNORECASE)
twitter_api = rest.Rest("https://publish.twitter.com/oembed?omit_script=true&url=%s")

def embed(submission):
    match = twitter_regex.match(submission.url)
    if not match:
        return None

    match = twitter_tweet_regex.match(submission.url)
    if not match:
        return {
            'kind' : 'SORRY',
            'sorrytext' : 'This Twitter link could not be embedded. Currently are only tweets supported.'
        }

    info = twitter_api.get(submission.url)
    print("Got twitter info for url: %s" % info['url'])

    return {
        'kind' : 'TEXT',
        'selftext' : info['html']
    }
