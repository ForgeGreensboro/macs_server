from .base import Log
from django.db import models

class MachineUnlock(Log):
    machine = models.ForeignKey('machine', on_delete=False)
    member = models.ForeignKey('member', on_delete=False)