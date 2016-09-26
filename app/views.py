from django.shortcuts import render

from . import reddit

# Create your views here.
def index(request, subreddit):
    if subreddit == "":
        print_subreddit = True
        subreddit = "all"
    elif "+" in subreddit:
        print_subreddit = True
    else:
        print_subreddit = False

    posts = reddit.get_posts(subreddit)
    context = {
        'posts' : posts,
        'print_subreddit' : print_subreddit
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})
