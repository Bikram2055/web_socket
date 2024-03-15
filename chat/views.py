from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Room, Message



# Create your views here.

class IndexView(View):
    
    template = 'base.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'rooms': Room.objects.all(),})
    

class RoomView(View):
    
    template = 'room.html'
    def get(self, request, *args, **kwargs):
        chat_room, created = Room.objects.get_or_create(name=kwargs["room_name"])
        return render(request, self.template, {'room': chat_room})
