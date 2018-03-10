from rest_framework import serializers

from macs.models import Member, Machine


class MemberSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Member
        fields = ['member_id', 'member_name', 'machines']
