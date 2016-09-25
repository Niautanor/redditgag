"""
The default provider which will *always* return an embeddable sorry post
"""

cache = 0

def embed(submission):
    return {
        'kind' : 'SORRY',
        'url' : submission.url
    }
