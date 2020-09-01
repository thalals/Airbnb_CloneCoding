from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="users", on_delete=models.CASCADE
    )
    room = models.ManyToManyField("rooms.Room", related_name="rooms", blank=True)
    # related_name 은 이 객체를 어떤이름으로 찾을것인지에 관한것
    def __str__(self):
        return self.name
