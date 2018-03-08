from django.db import models

from .location import Location
from .TimeStampedModel import TimeStampedModel
from macs.models.member import Member

class Machine(TimeStampedModel):
    description = models.TextField()
    address = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, through='MemberPermission',
        related_name='machines')

    def __str__(self):
    	return "%s in %s at address %s" %(self.description, self.location.description, self.address)
