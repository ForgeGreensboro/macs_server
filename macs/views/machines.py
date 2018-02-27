from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from macs.models import Machine
from macs.serializers import MachineSerializer
from macs.serializers.data_transfer import PermissionSerializer
from macs.data_transfer import Permission
from macs.models.log import MachineLock, MachineUnlock

class MachineView(viewsets.ViewSet):
    serializer = MachineSerializer


    def retrieve(self, request, pk=None, member_pk=None):
        queryset = Machine.objects.filter(address=pk, members__member_id=member_pk, memberpermission__can_use=1)
        machine = get_object_or_404(queryset)
        perm = Permission(member=machine.members.first().member_name, machine=machine.description, permission=1)
        serializer = PermissionSerializer(perm)
        return Response(serializer.data)

    @detail_route(methods=['POST'])
    def log(self, request, pk=None, member_pk=None):
        queryset = Machine.objects.filter(address=pk, members__member_id=member_pk)
        machine = get(queryset)
        if(request.data['event'] == 1):
            event = MachineUnlock(machine=machine, member=machine.members.first())
        elif(request.data['event'] == 2):
            event = MachineLock(machine=machine)
        else:
            event = InvalidRequest(machine=machine, member=machine.members.first())

        event.save()

        return Response()