from django.conf.urls import url
from functools import partial

from . import views

urlpatterns = [
    url(r'^$', partial(views.index, subreddit=None), name='frontpage'),
    url(r'^r/(?P<subreddit>[a-zA-Z0-9+_-]+)$', views.index, name='reddit'),
    url(r'^about$', views.about, name='about'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^auth_redirect$', views.auth_redirect, name='auth_redirect'),
]
