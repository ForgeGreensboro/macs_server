from macs.models import Machine
from rest_framework import serializers

class MachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Machine
        fields = ('address', 'description', 'location')
