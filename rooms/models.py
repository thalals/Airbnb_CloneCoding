from django.db import models
from django_countries.fields import CountryField
from core import models as core_models  # 이름 바꿔줌


class itemAbstract(core_models.TimeStampedModel):

    """room type Abstract Models"""

    name = models.CharField(max_length=80)

    class meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(itemAbstract):
    """ AmenityType Model Definition  """

    class Meta:
        verbose_name_plural = "Amenties"


class Facility(itemAbstract):
    """ Facility Model Definition  """

    class Meta:
        verbose_name_plural = "Facilities"


class House_rules(itemAbstract):
    """ HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class RoomType(itemAbstract):
    # 각 Room은 여러가지 RoomType을 가질 수 있다. ManyToManyField (N:M)
    """ RoomType Model Definition  """

    class Meta:
        verbose_name = "Room Type"  # verbose_name의 경우 접미사를 두되, 문법에 맞게 대문자 조절이 자동
        # ordering = ["-name"] 순서 정하기 가능


class Photo(core_models.TimeStampedModel):

    """Poto models defination"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE
    )  # 파이선은 수직관계 -> String으로 바꿔줌 찾을수있게

    def __str__(self):
        return self.caption


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
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )  # String으로 해주면 import 안해줘도됨
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenity = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facility = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        "House_rules", related_name="rooms", blank=True
    )

    def __str__(self):
        return self.name

    # overiding
    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews))  # 소수점 반올림
        return 0
