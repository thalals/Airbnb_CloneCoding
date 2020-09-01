from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# decorator model 바로 위에 써줘야함
@admin.register(models.User)  # admin.ModelAdmin
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("avatar", "gender", "birthdate", "bio", "superhost")},),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
