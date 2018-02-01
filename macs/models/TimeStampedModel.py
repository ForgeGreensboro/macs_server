from django.db import models
from safedelete.models import SafeDeleteModel
from django.utils import timezone


class TimeStampedModel(SafeDeleteModel):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True