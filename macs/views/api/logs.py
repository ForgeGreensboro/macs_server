from rest_framework.decorators import detail_route
from rest_framework.response import Response

from rest_framework import viewsets

from macs.models.log import MachineLock, MachineUnlock, InvalidRequest, Log
from macs.models import Machine, Member

class LogViewSet(viewsets.ViewSet):
    """Log Views

    [description]

    Extends:
        viewsets.ViewSet
    """

    def list(self, request):
        pass

    def create(self, request):
        pk = request.data['machine']
        event = request.data['event']
        queryset = Machine.objects.filter(address=pk)
        machine = queryset.first()

        if 'member' in request.data:
            member_pk = request.data['member']
            querySetM = Member.objects.filter(member_id=member_pk)
            member = querySetM.first()
            if(request.data['event'] == '1'):
                event = MachineUnlock(machine=machine, member=member)
            elif(request.data['event'] == '3'):
                event = InvalidRequest(machine=machine, member=member)
        else:
            event = MachineLock(machine=machine)

        event.save()

        return Response()

    def retrieve(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass