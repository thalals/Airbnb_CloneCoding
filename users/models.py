from django.db import models
from django.contrib.auth.models import AbstractUser

# Abstract 모델은 db에 추가되지 않는다.
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

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(blank=True)  # black 는 db상이 아니라 form에서 사용 값이 없어도 괜찮게
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
        default=GENDER_MALE,  # choices 의 default 값
    )
    bio = models.TextField(default="", blank=True)  # 값을 비워두지 않고 defalut 값생성(defalut="")
    birthdate = models.DateField(null=True)
    language = models.CharField(  # 사용 언어
        choices=LANGUAGE_CHOICES, max_length=2, blank=True
    )
    currency = models.CharField(  # 사용하는 돈 종류
        choices=CURRENCY_CHOICES, max_length=3, blank=True
    )
    superhost = models.BooleanField(default=False)
