from django.db import models
from .base import Log

class InvalidRequest(Log):
    machine = models.ForeignKey('machine', on_delete=False)
    member = models.ForeignKey('member', on_delete=False)