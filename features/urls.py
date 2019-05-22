from django.conf.urls import url, include
from .views import all_features, upvote_feature, add_feature

urlpatterns = [
     url(r'^$', all_features, name='features'),
     url(r'^upvote/(?P<id>\d+)$', upvote_feature, name='upvote_feature' ),
     url(r'^add$', add_feature)
]