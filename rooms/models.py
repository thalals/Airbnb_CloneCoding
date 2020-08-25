from django.db import models
from django_countries.fields import CountryField
from core import models as core_models  # 이름 바꿔줌
from users import models as users_models

# Create your models here.
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

    def __str__(self):
        return self.name
