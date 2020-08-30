from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()  # 별점
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.ImageField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __Str__(self):
        return f"{self.review} - {self.room}"
