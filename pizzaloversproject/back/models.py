import uuid

from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError


class PizzaLover(models.Model):
    numberOfVotes = models.IntegerField(default=0)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def vote(self):
        if self.numberOfVotes is None:
            self.numberOfVotes = 1
        else:
            self.numberOfVotes = self.numberOfVotes + 1
        self.save()


def validate_message_content(content):
    if content is None or content == "" or content.isspace():
        raise ValidationError(
            'Content is empty/invalid',
            code='invalid',
            params={'content': content},
        )


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        null=False,
        default=uuid.uuid4,
        editable=False
    )
    content = models.TextField()
