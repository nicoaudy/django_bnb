from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


class Conversation(core_models.TimestampedModel):

    """ conversation model definition """

    participants = models.ManyToManyField(user_models.User, blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimestampedModel):

    """ message model definition """

    message = models.TextField()
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says {self.message}'
