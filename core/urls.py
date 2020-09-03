from django.contrib import admin
from django.urls import path, include
from rooms import views as room_views

app_name = "core"

urlpatterns = [path("", room_views.all_rooms, name="home")]

