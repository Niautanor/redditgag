"""
i.reddituploads.com is the domain used for images that have been directly
uploaded to reddit when creating the post. Everything there is an image
basically and I hope that it stays that way for the future.
"""

import re

name = "reddit"
icon = "https://www.redditstatic.com/favicon.ico"

reddituploads_regex = re.compile(r'^https?://(?:i\.)?reddituploads\.com/.+')

def embed(submission):
    if not reddituploads_regex.search(submission.url):
        return None

    return {
        'kind' : 'IMAGE',
        'url' : submission.url
    }
