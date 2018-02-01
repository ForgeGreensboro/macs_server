from django.db import models
from .TimeStampedModel import TimeStampedModel
from .machine import Machine

class Member(TimeStampedModel):
    member_id = models.TextField()
    member_name = models.TextField(default='')
    machines = models.ManyToManyField(Machine, through='MemberPermission')