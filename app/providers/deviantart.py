"""
Embeds deviantart images.

For api reference see https://www.deviantart.com/developers/oembed
"""

import re
import logging

from .. import rest

logger = logging.getLogger(__name__)

name = "deviantart"
icon = "http://i.deviantart.net/icons/da_favicon.ico"

deviantart_regex = re.compile(r'^https?://(?:fav\.me/.*|sta\.sh/.*|(?:.+\.)?deviantart.com/(?:art/.*|[^#]*#/d.*))$', re.IGNORECASE)
image_regex = re.compile(r'\.(?:jpe?g|gif|png|svg)$', re.IGNORECASE)
deviantart_api = rest.Rest("https://backend.deviantart.com/oembed?url=%s")

def embed(submission, api=deviantart_api.get):
    if not deviantart_regex.search(submission.url):
        return None

    info = api(submission.url)
    logger.info("Got deviantart info %s", info['author_name'])
    if info['type'] != 'photo':
        return {
            'kind' : 'SORRY',
            'sorrytext' : 'Deviant art things other than phot are not supported',
        }

    src = info['url'] if image_regex.search(info['url']) \
                      else info['thumbnail_url']

    return {
        'kind' : 'IMAGE',
        'url' : src
    }
