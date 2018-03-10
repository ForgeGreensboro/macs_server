from django.db import models
from .TimeStampedModel import TimeStampedModel

class Location(TimeStampedModel):
    description = models.TextField()

    def __str__(self):
    	return self.description
