from rest_framework import serializers

from macs.models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ['description', 'machines']