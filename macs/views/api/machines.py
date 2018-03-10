from rest_framework import viewsets

from macs.models import Machine
from macs.serializers import MachineSerializer

class MachineViewSet(viewsets.ReadOnlyModelViewSet):
    """Member Views

    [description]

    Extends:
        viewsets.ReadOnlyModelViewSet
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
