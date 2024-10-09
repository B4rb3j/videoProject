from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/video/(?P<video_id>\d+)/$', consumers.VideoViewConsumer.as_asgi()),
    re_path(r'ws/comments/(?P<video_id>\d+)/$', consumers.CommentConsumer.as_asgi()),
    re_path(r'ws/rating/(?P<video_id>\d+)/$', consumers.RatingConsumer.as_asgi()),
]

