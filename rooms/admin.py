from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.House_rules)
class Roomtype(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    # admin 화면에 리스트 보여줌
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guestes",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("instant_book", "city", "country")
    # city로 먼저 검색하고 없으면 username으로 검색
    search_fields = ("=city", "host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
