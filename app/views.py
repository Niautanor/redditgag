from django.shortcuts import render

from . import reddit

# Create your views here.
def index(request, subreddit=""):
    if subreddit == "":
        subreddit = "all"

    if subreddit == "all" or "+" in subreddit:
        print_subreddit = True
    else:
        print_subreddit = False

    after = request.GET.get('after', None)
    nsfw = 'nsfw' in request.GET
    posts, last = list(reddit.get_posts(subreddit, after, nsfw))

    context = {
        'posts' : posts,
        'print_subreddit' : print_subreddit,
        'last' : last,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})
