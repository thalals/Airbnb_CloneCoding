from django.shortcuts import render
from django.http import HttpResponse  # httpresponse 이용
from . import models

def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request,"home.html", {"rooms" : all_rooms})
