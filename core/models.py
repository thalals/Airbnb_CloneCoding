from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    # 이 모델을 db에 추가하지 않기위해 추상모델로 만듬
    class Meta:
        abstract = True