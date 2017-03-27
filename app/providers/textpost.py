name = "reddit"
icon = "https://www.redditstatic.com/favicon.ico"

def embed(submission):
    if not submission.is_self:
        return None

    return {
        'kind' : 'TEXT',
        'selftext' : submission.selftext_html
    }
