### Redditgag - a 9gag like interface for reddit

This project exists to make reddit more accessible to people who find reddit's
concept of providing links instead of images cumbersome but still want to look
at the best cat pictures on the internet.

The data flow in this project basically involves getting posts from reddit with
PRAW, checking if the link is an image by sending a HEAD request and checking
the content-type (wrapped in a `functools.lru_cache` so that we don't send too
many requests) and then serving a 9gagized version of the reddit page with
embedded images using django.
