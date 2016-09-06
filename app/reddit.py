# this file provides most of the functionality of the application. Reddit posts
# are retrieved and filtered here.
import collections
import praw
import re

Post = collections.namedtuple('Post', ['title', 'image', 'permalink'])

reddit = praw.Reddit(user_agent='redditgag - a 9gag like interface to reddit posts by /u/niautanor')

image_regex = re.compile(r'.(png|jpe?g|gifv?)$', re.IGNORECASE)
def is_image(url):
    #TODO: other things besides images are potentially embeddable (text posts,
    # youtube/gfycat links, imgur albums, etc). I should think about how this
    # could be realized
    return image_regex.search(url) is not None

def get_posts(subreddit):
    if subreddit == "":
        subreddit = 'all'
    #TODO: support other lists (e.g. new, top)
    #TODO: pagination
    submissions = reddit.get_subreddit(subreddit).get_hot(limit=25)
    return (Post(s.title, s.url, s.permalink)
            for s in submissions
            if is_image(s.url))
