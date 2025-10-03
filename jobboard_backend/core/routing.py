from django.urls import re_path
from jobs.consumers import JobUpdateConsumer

websocket_urlpatterns = [
    re_path(r'ws/jobs/$', JobUpdateConsumer.as_asgi()),
]
