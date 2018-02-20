from rest_framework import serializers
from . import BaseSerializer

from macs.data_transfer import Permission

class PermissionSerializer(BaseSerializer):
    machine = serializers.CharField(max_length=250)
    member = serializers.CharField(max_length=250)
    permission = serializers.BooleanField()
