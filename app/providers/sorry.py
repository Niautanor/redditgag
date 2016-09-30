"""
The default provider which will *always* return an embeddable sorry post
"""

from urllib.parse import urlparse

cache = 0

SORRY_TEMPLATE = """
There currently isn't a way to embed this link from the domain %s.
Maybe someone will send the developer a pull request to fix this ;)
"""

def embed(submission):
    domain = urlparse(submission.url).netloc
    return {
        'kind' : 'SORRY',
        'sorrytext' : SORRY_TEMPLATE % domain
    }
