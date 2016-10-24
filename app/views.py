from django.shortcuts import render, redirect
from django.http import JsonResponse

from . import reddit
from .providers import sorry

# Create your views here.
def index(request, subreddit=""):
    # default set is html (None)
    # return html fast
    if request.GET.get('content_type', None) is None:
        return render(request, 'index.html', {})

    if subreddit is None or subreddit == "all" or "+" in subreddit:
        print_subreddit = True
    else:
        print_subreddit = False

    after = request.GET.get('after', None)
    auth = request.session.get('reddit_auth', None)
    nsfw = 'nsfw' in request.GET
    posts, last, newauth = reddit.get_posts(subreddit, after, nsfw, auth)

    # update the oauth token if it has changed
    request.session['reddit_auth'] = newauth

    context = {
        'posts' : posts,
        'print_subreddit' : print_subreddit,
        'last' : last,
    }

    return JsonResponse(context)

def about(request):
    return render(request, 'about.html', {
        'domains' : sorry.get_unsupported_domains()
    })

def login(request):
    state, url = reddit.generate_oauth_state()
    request.session['oauth_state'] = state
    return render(request, 'login.html', {
        'authorize_url' : url,
    })

def logout(request):
    request.session.flush()
    return redirect('frontpage')

def auth_redirect(request):
    # TODO: maybe replace these assertions with error messages?
    assert 'oauth_state' in request.session
    assert 'code' in request.GET
    assert request.session['oauth_state'] == request.GET['state']

    # get the auth tokens from reddit
    session_state = request.session['oauth_state']
    reddit_state = request.GET['state']
    code = request.GET['code']
    tokens = reddit.verify_auth_callback(session_state, reddit_state, code)

    # creds['scope'] is a set
    # => we have to turn it into a list to make it serializable
    tokens['scope'] = list(tokens['scope'])

    # clean up and redirect to the front page
    del request.session['oauth_state']
    request.session['reddit_auth'] = tokens

    return redirect('frontpage')
