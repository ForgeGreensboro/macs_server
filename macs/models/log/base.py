from django.db import models
from polymorphic.models import PolymorphicModel

class Log(PolymorphicModel):
    timestamp = models.DateField(auto_now_add = True)
    class Meta:
        abstract = True


