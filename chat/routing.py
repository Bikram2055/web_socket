from django.urls import path

from chat.consumer import ChatRoomConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatRoomConsumer.as_asgi()),
]