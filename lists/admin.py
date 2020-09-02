from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin definition """

    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("name",)

    filter_horizonntal = "rooms"

