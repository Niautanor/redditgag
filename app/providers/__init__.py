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
from . import imgur
from . import youtube
from . import gfycat
# this last one is a catch-all to prevent the front page from being empty if
# nothing was found. It is very important that this comes last in the modules
# list
from . import sorry

modules = [textpost, plain, imgur, youtube, gfycat, sorry]

def get_embeddable(submission):
    # first try to get the thing from the cache
    # TODO: the cache works with urls but the actual providers expect a reddit
    # submission which has more info. Because the sorry and textpost providers
    # are the only ones that make use of this information and don't cache
    # anything, this works well but I still think it's a bit ugly.
    embeddable = cache.get(submission.url)
    if embeddable is not None:
        return embeddable
    # if the thing wasn't found, resolve it
    for module in modules:
        embeddable = module.embed(submission)
        if embeddable is not None:
            if module.cache > 0:
                cache.set(submission.url, embeddable, module.cache)
            return embeddable
