name = "reddit"
icon = "https://www.redditstatic.com/favicon.ico"

def embed(submission):
    if submission.is_self:
        return {
            'kind' : 'TEXT',
            'selftext' : submission.selftext_html
        }
    return None
