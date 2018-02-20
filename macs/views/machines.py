from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from macs.models import Machine
from macs.serializers import MachineSerializer
from macs.serializers.data_transfer import PermissionSerializer
from macs.data_transfer import Permission

class MachineView(viewsets.ViewSet):
    serializer = MachineSerializer


    def retrieve(self, request, pk=None, member_pk=None):
        queryset = Machine.objects.filter(address=pk, members__member_id=member_pk, memberpermission__can_use=1)
        machine = get_object_or_404(queryset)
        perm = Permission(member=machine.members.first().member_name, machine=machine.description, permission=1)
        serializer = PermissionSerializer(perm)
        return Response(serializer.data)
