from django.db import models
from .TimeStampedModel import TimeStampedModel

class Member(TimeStampedModel):
    member_id = models.TextField()
    member_name = models.TextField(default='')
