from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):

    messgae = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="conversations", on_delete=models.CASCADE
    )
    # conversation 을 지우면 Messge도 삭제
    conversation = models.ForeignKey(
        "Conversation", related_name="conversations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
