from math import ceil  # 올림
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse  # httpresponse 이용
from . import models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)  # 리스트와, 페이지수
    # 오류처리
    try:
        rooms = paginator.get_page(page)
        return render(request, "rooms/home.html", {"rooms": rooms})

    except EmptyPage:
        return redirect("/")
