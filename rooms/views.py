from django.shortcuts import render
from django.http import HttpResponse  # httpresponse 이용


def all_rooms(request):

    return HttpResponse(content="hello")
