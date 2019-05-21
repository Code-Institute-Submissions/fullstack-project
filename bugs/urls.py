from django.conf.urls import url, include
from .views import all_bugs, upvote_bug, add_bug, edit_bug

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^upvote/(?P<id>\d+)$', upvote_bug, name='upvote_bug' ),
    url(r'^add$', add_bug),
    url(r'^edit/(?P<id>\d+)$', edit_bug)
]