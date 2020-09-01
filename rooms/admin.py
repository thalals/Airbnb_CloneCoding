from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.House_rules)
class Roomtype(admin.ModelAdmin):
    
    list_display = (
        "name",
        "used",
    )

    def userd_by(self, obj):
        return obj.rooms.count()



@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Basic Info", {"fields": ("name", "country", "city", "price",)}),
        # 필드 나누기
        ("Times", {"fields": ("check_in", "check_out", "instant_book",)}),
        ("spaces", {"fields": ("guestes", "beds", "bedrooms", "baths",)}),
        (
            "More About space",
            {
                "classes": ("collapse",),  # 화면을 접을수있게함
                "fields": ("amenity", "facility", "house_rules",),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

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
        "count_amenity",
        "count_photos",
    )

    # 리스트 정렬
    ordering = ("name", "price", "bedrooms")

    # city 와 country는 항상 맨아래
    list_filter = (
        "instant_book",
        "room_type",
        "amenity",
        "facility",
        "house_rules",
        "city",
        "country",
    )
    # city로 먼저 검색하고 없으면 username으로 검색
    search_fields = ("=city", "host__username")
    # Many to many 에서만 사용
    filter_horizontal = (
        "amenity",
        "facility",
        "house_rules",
    )

    # usr 커스텀마이징
    def count_amenity(self, obj):
        return obj.amentiy.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
