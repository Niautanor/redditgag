"""
Embeds tumblr posts (not plain images as those are already handled by plain.py
and I don't feel like getting the captions is worth the extra api requests.
"""

import re

from .. import rest

name = "tumblr"
icon = "https://assets.tumblr.com/images/favicons/favicon.ico"

tumblr_regex = re.compile(r'^https?://([^.]*\.tumblr\.com)/post/(\d+)',
        re.IGNORECASE)

#https://www.tumblr.com/docs/en/api/v2#posts for documentation
api_key = 'QCZFC4KO8o4lcZl8KSFULINGLtgibIxWtYEE4selJU7Eqy4CuN'
endpoint = "https://api.tumblr.com/v2/blog/%s/posts?id=%s"
params = {
    'api_key' : api_key,
    'filter' : 'raw'
}

tumblr_api = rest.Rest(endpoint, params=params)

def embed(submission):
    match = tumblr_regex.search(submission.url)
    if not match:
        return None

    print("Getting tumblr info for id [%s,%s]" %
            (match.group(1),match.group(2)))

    posts = tumblr_api.get(match.groups())['response']['posts']

    assert len(posts) == 1, "Did not expect more than one tumblr post"

    info = posts[0]

    if info['type'] == 'answer':
        return {
            'kind' : 'TEXT',
            'selftext' : info['question'] + "<br />" + info['answer']
        }
    elif info['type'] == 'text':
        from pprint import pprint; pprint(info)
        return {
            'kind' : 'TEXT',
            'selftext' : info['body']
        }
    elif info['type'] == 'photo':
        # TODO: research if there can be other things except images
        # TODO: debate whether or not it makes sense to return an IMAGE if there
        # is only one photo (applies to imgur as well)
        return {
            'kind' : 'ALBUM',
            'elements' : [{
                'kind' : 'IMAGE',
                'url' : photo['original_size']['url']
            } for photo in info['photos']]
        }
    return {
        'kind' : 'SORRY',
        'sorrytext' :
            '''Unsupported tumblr post type %s''' % info['type']
    }
