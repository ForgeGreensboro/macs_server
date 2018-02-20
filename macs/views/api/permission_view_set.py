from rest_framework import viewsets
from rest_framework.response import Response
# from django.http import HttpResponse
# from django.views import View
# from rest_framework.renderers import JSONRenderer

import sys

from macs.models import Machine, Member
from macs.serializers.data_transfer import PermissionSerializer
from macs.data_transfer.permission import Permission

class PermissionViewSet(viewsets.ViewSet):
    serializer_class = PermissionSerializer

    def retrieve(self, request, pk=None, pk2=None):
        serializer = PermissionSerializer(
            instance=Permission(), many=False)
        return Response(serializer.data)

# class PermissionViewSet(View):
#     def get(self, request, pk, pk2):
#         return HttpResponse(JSONRenderer.render(PermissionSerializer(Permission()).data), content_type="application/json")
