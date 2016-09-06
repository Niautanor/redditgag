from django.shortcuts import render

from . import reddit

# Create your views here.
def index(request, subreddit):
    posts = reddit.get_posts(subreddit)
    context = { 'posts' : posts }
    return render(request, 'index.html', context)
