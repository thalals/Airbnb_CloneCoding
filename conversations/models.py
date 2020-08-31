from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)  # String 형변환


class Message(core_models.TimeStampedModel):

    messgae = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # conversation 을 지우면 Messge도 삭제
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
