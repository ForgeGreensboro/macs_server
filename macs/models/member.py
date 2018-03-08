from django.db import models
from .TimeStampedModel import TimeStampedModel

class Member(TimeStampedModel):
    member_id = models.TextField()
    member_name = models.TextField(default='')

    def __str__(self):
    	return "%s with card id: %s" % (self.member_name, self.member_id)
