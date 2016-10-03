"""
i.reddituploads.com is the domain used for images that have been directly
uploaded to reddit when creating the post. Everything there is an image
basically and I hope that it stays that way for the future.
"""

import re

cache = 0

reddituploads_regex = re.compile(r'^https?://(?:i\.)?reddituploads\.com/.+')

def embed(submission):
    if reddituploads_regex.search(submission.url) is not None:
        return {
            'kind' : 'IMAGE',
            'url' : submission.url
        }
    return None
