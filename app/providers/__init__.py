"""
This directory contains python modules that tell the application how to embed
certain types of links similar to what RES is doing
(https://github.com/honestbleeps/Reddit-Enhancement-Suite/tree/master/lib/modules/hosts)

Currently the available modules are:
    plain (for direct links to .jpe?g, .png, .webm, etc
    youtube (for youtube links) (currently not implemented)
    gfycat (for gfycat links) (currently not implemented)
    imgur (for embedding not directly linked imgur images, albums and gifvs)

TODOs for the future include making this list dynamic so that you only have to
drop a python file in this directory to add a new provider and to add support
for more providers

This stackoverflow question has some possible plugin systems that I could use
https://stackoverflow.com/questions/932069/building-a-minimal-plugin-architecture-in-python#932072
"""
from . import plain
from . import imgur
from . import youtube
from . import gfycat

modules = [plain, imgur, youtube, gfycat]
