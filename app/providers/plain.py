"""
This module is responsible for embedding images and videos that are linked
directly (as plain files)
"""

import re

image_regex = re.compile(r'.(png|jpe?g|gif)$', re.IGNORECASE)
video_regex = re.compile(r'.(webm|mp4)', re.IGNORECASE)

cache = 0

def embed(submission):
    # img tags don't require a type so we can take a shortcut here
    if image_regex.search(submission.url):
        return {
            'kind' : 'IMAGE',
            'url' : submission.url
        }
    # video source tags do require a type so we have to check the match to
    # find it
    match = video_regex.search(submission.url)
    if match is not None:
        # TODO: the regex could probably be dynamically generated from a mime
        # type -> file extension mapping
        if match.group().lower() == 'webm':
            mime = 'video/webm'
        elif match.group.lower() == 'mp4':
            mime = 'video/mp4'
        else:
            # something terrible has happened
            return None
        return {
            'kind' : 'VIDEO',
            'sources' : {
                'mime' : mime,
                'url' : submission.url
                }
            }
    return None
