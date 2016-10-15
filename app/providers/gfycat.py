import re

from .. import rest

name = "gfycat"
icon = "https://gfycat.com/favicon2.ico"

gfycat_regex = re.compile(r'^https?:\/\/gfycat.com\/(\w+)(?:\.gif)?', re.IGNORECASE)

# for documentation about the API see https://gfycat.com/api and the Reddit
# Enhancement Suite source code
# cache for a day
gfycat_api = rest.Rest("https://gfycat.com/cajax/get/%s")

def embed(submission):
    # extract gfy id from url
    match = gfycat_regex.match(submission.url)
    if match is not None:
        # get info from gfycat api
        print("Getting gfycat info")
        info = gfycat_api.get(match.group(1))['gfyItem']

        return {
            'kind' : 'VIDEO',
            'sources' : [{
                'mime' : 'video/webm',
                'url' : info['webmUrl']
            }, {
                'mime' : 'video/mp4',
                'url' : info['mp4Url']
            }]
        }
    return None
