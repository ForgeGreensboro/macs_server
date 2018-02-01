from django.db import models
from .TimeStampedModel import TimeStampedModel

class Location(TimeStampedModel):
    description = models.TextField()
