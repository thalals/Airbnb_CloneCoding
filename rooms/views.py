from math import ceil  # 올림
from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404  # httpresponse 이용
from django.views.generic import ListView, DetailView  # CBV
from . import models

# fbv
# def all_rooms(request):
#     page = request.GET.get("page")
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10)  # 리스트와, 페이지수
#     # 오류처리
#     try:
#         rooms = paginator.get_page(page)
#         return render(request, "rooms/home.html", {"rooms": rooms})

#     except EmptyPage:
#         return redirect("/")


class HomeView(ListView):

    """ Homeview Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"  # ordering은 필드를 반환해야함
    context_object_name = "rooms"  # cbv가 제공하는 object 이름을 바꿈

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


# fbv
# def room_detail(request, pk):
#     try:
#         room = models.objects.get(pk=pk)
#         render(request, " rooms/detail.html", {"room": room})

#     except models.Room.DoesNotExist:
#         raise Http404()  # templates 폴더안에 404html 있으면 알아서 redirect함


class RoomDetail(DetailView):
    """ RoomDetail Definition """
    model = models.Room  # Detailview를 사용하면 자동적으로 pk를 찾음

