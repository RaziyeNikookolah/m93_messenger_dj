from django.db import models
from core.models import BaseModel, User


# Create your models here.
class Message(BaseModel):
    class STATUS(models.IntegerChoices):
        SENT = 1, 'SENT'
        RECEIVED = 2, 'RECEIVED'
        DRAFT = 3, 'DRAFT'

    chat = models.ForeignKey(
        'Chat', on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="messages")
    text = models.CharField(max_length=250)
    status = models.PositiveSmallIntegerField(
        choices=STATUS.choices, default=STATUS.DRAFT)


class Chat(BaseModel):
    topic = models.CharField(max_length=250)
    user = models.ManyToManyField(User, related_name="user_chats")
