"""
this file provides most of the functionality of the application. Reddit posts
are retrieved and converted to embeddable objects using the modules from the
providers package.
"""

import collections
import random
import string
import praw
import re

from django.conf import settings
from django.urls import reverse

from praw.errors import OAuthInvalidToken

from . import providers

reddit = praw.Reddit(user_agent='redditgag - a 9gag like interface to reddit posts by /u/niautanor', cache_timeout=120)

reddit.set_oauth_app_info(
    client_id=settings.REDDIT_AUTH_CLIENT_ID,
    client_secret=settings.REDDIT_AUTH_CLIENT_SECRET,
    redirect_uri=settings.REDDIT_AUTH_REDIRECT_URI)

def get_posts(subreddit, after, show_nsfw, auth):
    """
    Requests a few (5) posts from the subreddit subreddit (frontpage if
    subreddit is None) and add the hidden attribute to nsfw posts unless
    show_nsfw is True.

    auth is a tuple consisting of a scope, an access token and a refresh token
    from the reddit API that can be used to access private subreddits / the
    personalized front page.

    The function returns a 3-tuple consisting of the list of embeddables, the id
    of the last retrieved post (used to request the next batch) and the updated
    auth token (tokens expire after a while and are automatically refreshed by
    praw)
    """
    if auth is not None:
        reddit.set_access_credentials(**auth)
    else:
        reddit.clear_authentication()

    fun = reddit.get_front_page if subreddit is None \
                                else reddit.get_subreddit(subreddit).get_hot

    try:
        submissions = list(fun(limit=5, params={'after':after}))
        last = submissions[-1].name
        # the reddit api actually returns a 'after' field to allow pagination
        # but praw won't let me access it :/

        return [
            providers.get_embeddable(s, show_nsfw) for s in submissions
        ], last, {
            'scope' : list(reddit._authentication),
            'access_token' : reddit.access_token,
            'refresh_token' : reddit.refresh_token,
        } if auth is not None else None
    except OAuthInvalidToken:
        return [{
            'title' : 'Reddit Authentication Failure',
            'author' : 'redditgag',
            'subreddit' : 'redditgag',
            'hidden' : None,
            'kind' : 'SORRY',
            'sorrytext' : """The Reddit authentication token is invalid. This
            usually means that you have revoked this apps access in your reddit
            app preferences but haven't <a href="%s">cleared your session cookie
            yet</a>. If this isn't the case, I would appreciate it if you
            reported the issue on github.""" % reverse('logout'),
        }], -1, auth

def generate_oauth_state():
    """
    Generates a random string of 6 lower case characters to make sure we only
    finish reddit authentication requests that we started.

    See: https://github.com/reddit/reddit/wiki/OAuth2
    """
    state =  ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    return state, reddit.get_authorize_url(state, 'read', True)

def verify_auth_callback(session_state, reddit_state, code):
    assert session_state == reddit_state
    # False because we don't want to automatically bind the reddit object to
    # the retrieved credentials
    return reddit.get_access_information(code, False)
