from django.conf.urls import url, include
from .views import all_bugs, upvote_bug

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^upvote/(?P<id>\d+)$', upvote_bug, name='upvote_bug' )
]