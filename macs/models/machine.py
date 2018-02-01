from django.db import models

from .location import Location
from .TimeStampedModel import TimeStampedModel

class Machine(TimeStampedModel):
    description = models.TextField()
    address = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
