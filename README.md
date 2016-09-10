### Redditgag - a 9gag like interface for reddit

This project exists to make reddit more accessible to people who find reddit's
concept of providing links instead of images cumbersome but still want to look
at the best cat pictures on the internet.

The data flow in this project basically involves getting posts from reddit with
PRAW, checking if the link is an image by sending a HEAD request and checking
the content-type (wrapped in a `functools.lru_cache` so that we don't send too
many requests) and then serving a 9gagized version of the reddit page with
embedded images using django.

### Important notes if you want to run your own version of this project

The first thing you have to do is copy secret\_example.py to redditgag/secret.py
and optionally change the secret key contained in this file to something random
(e.g. something from
[this](http://www.miniwebtool.com/django-secret-key-generator/) website.

Next you have to run the server. If you already have experience with Django then
you probably know more about this than I do. Otherwise you can just run

    python3 manage.py runserver

From the project directory. This will start a test server that will provide the
application at [127.0.0.1:8000/app/](http://127.0.0.1:8000/app/).
