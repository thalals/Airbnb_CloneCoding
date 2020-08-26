from django.contrib import admin
from . import models


@admin.register(models.RoomType)
class Roomtype(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
