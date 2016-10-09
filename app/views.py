from django.shortcuts import render
from django.http import JsonResponse

from . import reddit
from .providers import sorry

# Create your views here.
def index(request, subreddit=""):
    # default set is html (None)
    # return html fast
    if request.GET.get('content_type', None) is None:
        return render(request, 'index.html', {})

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

    return JsonResponse(context)

def about(request):
    return render(request, 'about.html', {'domains' : sorry.get_unsupported_domains()})
