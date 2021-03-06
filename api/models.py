from django.db import models
from django_enumfiled import enum
from enum import Enum

# Create your models here.

class Status(Enum):
    STARTED = 0
    IN_PROGRESS = 1
    FAILED = 2
    CANCELLED = 3
    SUCCEEDED = 4

 
class Transaction(models.Model):
    video_url = models.UrlField(max_length=120)
    status = enum.EnumField(Status, default=Status.STARTED)
