"""
This module is responsible for embedding twitter tweets.

Like with most of my embeddable providers, portions of the code (regexes in
particular) come from the Reddit Enhancement Suite
"""

import re

from .. import rest
from requests.exceptions import RequestException

twitter_regex = re.compile(r'^https?://((m|mobile|www)\.)?twitter\.com.*')
twitter_tweet_regex = re.compile(r'^https?://((m|mobile|www)\.)?twitter\.com/(#\!/)?\w{1,15}/status/\d+.*', re.IGNORECASE)
twitter_api = rest.Rest("https://publish.twitter.com/oembed?omit_script=true&url=%s")

def embed(submission):
    match = twitter_regex.match(submission.url)
    if match is not None:
        match = twitter_tweet_regex.match(submission.url)
        if match is not None:
            try:
                info = twitter_api.get(submission.url)
                print("Got twitter info for url: %s" % info['url'])

                return {
                'kind' : 'TEXT',
                'selftext' : info['html']
            }
            except RequestException as e:
                print(e)
                return {
                    'kind' : 'SORRY',
                    'sorrytext' : 'There was an error when accessing the twitter api.',
                }
        else:
            return {
                'kind' : 'SORRY',
                'sorrytext' : 'This Twitter link could not be embedded. Currently are only tweets supported.'
            }
    return None
