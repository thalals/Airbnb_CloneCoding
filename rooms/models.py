from django.db import models
from django_countries.fields import CountryField
from core import models as core_models  # 이름 바꿔줌
from users import models as users_models


class itemAbstract(core_models.TimeStampedModel):

    """room type Abstract Models"""

    name = models.CharField(max_length=80)

    class meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(itemAbstract):
    pass


class Room(core_models.TimeStampedModel):

    """ Room models defination"""

    name = models.CharField(max_length=150)
    description = models.TextField()
    country = CountryField()  # 외부 패키지
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guestes = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    room_type = models.ManyToManyField()

    def __str__(self):
        return self.name
