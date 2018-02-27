from django.db import models
from .base import Log

class MachineLock(Log):
    machine = models.ForeignKey('machine', on_delete=False)
