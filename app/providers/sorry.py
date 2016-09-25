"""
The default provider which will *always* return an embeddable sorry post
"""

def embed(submission):
    return {
        'kind' : 'SORRY',
        'url' : submission.url
    }
