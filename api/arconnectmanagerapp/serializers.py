from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TournamentItem

class TournamentItemSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for the TournamentItem model '''
    class Meta:
        model = TournamentItem
        fields = [
            'url', 
            'id', 
            'name',
            'description',
            'state'
        ]
            