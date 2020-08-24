from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ Custom user Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    Language_korean = "kr"
    Language_english = "en"
    # tuple
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    LANGUAGE_CHOICES = (
        (Language_korean, "korean"),
        (Language_english, "English"),
    )

    avatar = models.ImageField(
        null=True, blank=True
    )  # black 는 db상이 아니라 form에서 사용 값이 없어도 괜찮게
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        null=True,
        blank=True,
        default=GENDER_MALE,  # choices 의 default 값
    )
    bio = models.TextField(default="", blank=True)  # 값을 비워두지 않고 defalut 값생성(defalut="")
    birthdate = models.DateField(null=True)
    Language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
