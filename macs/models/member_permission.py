from django.db import models

from .TimeStampedModel import TimeStampedModel
from .machine import Machine
from .member import Member


class MemberPermission(TimeStampedModel):
    can_use = models.BooleanField(default=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

