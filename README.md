### Redditgag - a 9gag like interface for reddit

This project exists to make reddit more accessible to people who find reddit's
concept of providing links instead of images cumbersome but still want to look
at the best cat pictures on the internet.

The data flow in this project basically involves getting posts from reddit with
PRAW, doing some Reddit Enhancement Suite style checking with multiple content
providers (youtube, imgur, gfycat, direct image links, ...) to get an embeddable
version of the link and then serving a 9gagized version of the reddit page with
embedded images using django.

### Important notes if you want to run your own version of this project

#### Create a secret key

The first thing you have to do is copy secret\_example.py to redditgag/secret.py
and optionally change the secret key contained in this file to something random
(e.g. something from
[this](http://www.miniwebtool.com/django-secret-key-generator/) website.

#### Install the required packages (from your operating system)

You are going to have to install python3, python-virtualenv and pip. If you use
a good operating system, you probably have a package manager that can do this
for you.  Otherwise, a google search for "Install pip and virtualenv \<your
operating system here\>" will probably tell you what to do.

#### Install the required libraries (with pip and npm)

Next, run these commands from a terminal in the projects root directory. If you
want to know what they do, [go](https://pip.pypa.io/en/stable/)
[and](https://virtualenv.pypa.io/en/stable/)
[RTFM](https://ekalinin.github.io/nodeenv/). (Basically, they create a clean
environment that contains all required libraries and utilities that are needed
to run the server).

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install nodeenv
    nodeenv -p
    npm install -g bower handlebars

#### Tell Django to set itself up

    python manage.py bower install
    python manage.py migrate

#### Run the server

You are almost there,

    python manage.py runserver

will start the development server that will provide the application at
[127.0.0.1:8000/app/](http://127.0.0.1:8000/app/). It will automatically reload
itself if you change any files so there should be no need to restart it
manually.

If you stop the server, you only have to run the `python manage.py runserver` command again.
