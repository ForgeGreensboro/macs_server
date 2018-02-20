from rest_framework import serializers

class BaseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=256)
    timestamp = serializers.DateTimeField()
