from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<subreddit>[a-zA-Z0-9+_-]*)$', views.index, name='index'),
]
