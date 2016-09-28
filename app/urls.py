from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='frontpage'),
    url(r'^about$', views.about, name='about'),
    url(r'^r/(?P<subreddit>[a-zA-Z0-9+_-]+)$', views.index, name='reddit'),
]
