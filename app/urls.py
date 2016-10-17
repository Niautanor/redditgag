from django.conf.urls import url
from functools import partial

from . import views

urlpatterns = [
    url(r'^$', partial(views.index, subreddit=None), name='frontpage'),
    url(r'^about$', views.about, name='about'),
    url(r'^r/(?P<subreddit>[a-zA-Z0-9+_-]+)$', views.index, name='reddit'),
]
