"""
This module is responsible for embedding youtube videos.

Like with most of my embeddable providers, portions of the code (regexes in
particular) come from the Reddit Enhancement Suite
"""

import re

name = "youtube"
icon = "https://s.ytimg.com/yts/img/favicon_96-vfldSA3ca.png"

youtube_regex = re.compile(r'^https?://(?:youtu\.be|(?:www\.|m\.)?youtube\.com)/?(?:watch|embed)?(?:.*\?v=|v/|/)([\w-]+)', re.IGNORECASE)

def embed(submission):
    match = youtube_regex.match(submission.url)
    if match is not None:
        return {
            'kind' : 'IFRAME',
            'url' : "https://www.youtube.com/embed/%s" % match.group(1)
        }
    return None
