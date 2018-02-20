from rest_framework.decorators import detail_route
from rest_framework.response import Response

from rest_framework import viewsets

from macs.models import Member
from macs.serializers import MemberSerializer

class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    """Member Views

    [description]

    Extends:
        viewsets.ReadOnlyModelViewSet
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

