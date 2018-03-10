from rest_framework import viewsets

from macs.models import Location
from macs.serializers import LocationSerializer

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """Member Views

    [description]

    Extends:
        viewsets.ReadOnlyModelViewSet
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer