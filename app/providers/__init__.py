"""
This package contains python modules that tell the application how to embed
certain types of links similar to what RES is doing
(https://github.com/honestbleeps/Reddit-Enhancement-Suite/tree/master/lib/modules/hosts)

Currently the available modules are:
    textpost (for reddit self posts (no url, just text))
    plain (for direct links to .jpe?g, .png, .webm, etc
    youtube (for youtube links) (currently not implemented)
    gfycat (for gfycat links) (currently not implemented)
    imgur (for embedding not directly linked imgur images, albums and gifvs)
    sorry (for posts that couldn't be embedded by any provider)

TODOs for the future include making this list dynamic so that you only have to
drop a python file in this directory to add a new provider and to add support
for more providers

This stackoverflow question has some possible plugin systems that I could use
https://stackoverflow.com/questions/932069/building-a-minimal-plugin-architecture-in-python#932072
"""

from django.core.cache import cache

from . import textpost
from . import plain
from . import reddituploads
from . import imgur
from . import youtube
from . import gfycat
from . import deviantart
from . import tumblr
from . import twitter
# this last one is a catch-all to prevent the front page from being empty if
# nothing was found. It is very important that this comes last in the modules
# list
from . import sorry



modules = [textpost, plain, reddituploads, imgur, youtube, gfycat, deviantart, tumblr, twitter, sorry]

def get_embeddable(submission, show_nsfw):
    for module in modules:
        try:
            embeddable = module.embed(submission)
        except Exception as e:
            embeddable = {
                'kind' : 'SORRY',
                'sorrytext' : """There was an error when getting an embeddable
                version of the link. It says %s""" % str(e)
            }

        if embeddable is not None:
            return dict(title=submission.title,
                permalink=submission.permalink,
                original_url=submission.url,
                author=submission.author.name,
                subreddit=submission.subreddit.display_name,
                num_comments=submission.num_comments,
                hidden='NSFW' if (submission.over_18 and not show_nsfw) \
                              else None,
                provider_name=module.__dict__.get('name','source'),
                provider_icon=module.__dict__.get('icon',False),
                **embeddable)
