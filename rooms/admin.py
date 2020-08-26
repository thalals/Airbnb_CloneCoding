from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.House_rules)
class Roomtype(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
