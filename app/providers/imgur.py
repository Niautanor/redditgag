"""
Embeds imgur posts (not plain images as those are already handled by plain.py
and I don't feel like getting the captions is worth the extra api requests.

Another big reason is that I don't want to think about how to display them.

Maybe later someone will implement caption display and this will be changed to
also send api requests for direct links
"""

import re

from .. import rest

name = "imgur"
icon = "https://s.imgur.com/images/favicon-32x32.png"

domain = r'^https?://(?:i\.|m\.|www\.)?imgur\.com'
domain_regex = re.compile(domain, re.IGNORECASE)
imgur_regex = re.compile(domain + r'\/(\w{5}|\w{7})(?:\.gifv)?(?:\?.*)?$', re.IGNORECASE)

#api.imgur.com for documentation
client_id = '1d8d9b36339e0e2'
endpoint = "https://api.imgur.com/3/image/%s.json"
headers = {
    'Authorization' : "CLIENT-ID %s" % client_id
}

imgur_api = rest.Rest(endpoint, headers=headers)

def embed(submission):
    match = imgur_regex.search(submission.url)
    if match is not None:
        print("Getting imgur info for id %s" % match.group(1))

        info = imgur_api.get(match.group(1))['data']

        if 'mp4' in info:
            return {
                'kind' : 'VIDEO',
                'sources' : [{
                    'mime' : 'video/mp4',
                    'url' : info['mp4']
                }]
            }
        else:
            return {
                'kind' : 'IMAGE',
                'url' : info['link']
            }
    elif domain_regex.search(submission.url) is not None:
        print("fuck %s" % submission.url)
        return {
            'kind' : 'SORRY',
            'sorrytext' :
                '''Imgur albums are not supported at this time. If this
                isn't an album, please send the developer a message'''
        }
    return None
