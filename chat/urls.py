from django.urls import path
from . import views
from .consumer import ChatRoomConsumer

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("chat/<str:room_name>/", views.RoomView.as_view(), name="room"),
]
