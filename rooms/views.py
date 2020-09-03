from math import ceil   #올림
from django.shortcuts import render
from django.http import HttpResponse  # httpresponse 이용
from . import models


def all_rooms(request):
    page = int(request.GET.get("page",1))
    page = int(page or 1)   #기본값 주기
    page_size = 10
    limit = page_size*page
    offset = limit-page_size
    all_rooms = models.Room.objects.all()[offset:limit]  # [start:finish] 제한하여 필터링
    
    page_count = ceil(models.Room.objects.count()/page_count)   #올림
    
    return render(request, "rooms/home.html", {"rooms": all_rooms, "page" : page, "page_count" : (page_count), "page_range" : range(1,page_count)})
