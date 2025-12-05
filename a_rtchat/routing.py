from django.urls import path
from .consumers import * 
# So this consumers file is similar to views.py file in normal django app but for a websocket connection.

websocket_urlpatterns = [
    path("ws/chatroom/<chatroom_name>/", ChatroomConsumer.as_asgi()),
]