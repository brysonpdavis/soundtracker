from django.db import models
from django_enumfield import enum

# Create your models here.

class Status(enum.Enum):
    STARTED = 0
    IN_PROGRESS = 1
    FAILED = 2
    CANCELLED = 3
    SUCCEEDED = 4

 
class Transaction(models.Model):
    video_url = models.URLField(max_length=120)
    status = enum.EnumField(Status, default=Status.STARTED)
