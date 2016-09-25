cache = 0

def embed(submission):
    if submission.is_self:
        return {
            'kind' : 'TEXT',
            'selftext' : submission.selftext_html
        }
    return None
