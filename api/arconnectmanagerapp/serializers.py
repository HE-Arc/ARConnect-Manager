from rest_framework import serializers
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from .models import TournamentItem

class TournamentItemSerializer(serializers.ModelSerializer):
    ''' Serializer for the TournamentItem model '''
    class Meta:
        model = TournamentItem
        fields = [
            'url', 
            'id', 
            'name', 
            'description', 
            'state',
            'challonge_image_url',
            'players',
        ]
        read_only_fields = ['url', 'id', 'state', 'challonge_image_url', 'players']
        
class ScoreSerializer(serializers.Serializer):
    ''' Serializer for the score submission '''
    match_id = serializers.CharField()
    player1_id = serializers.CharField()
    player2_id = serializers.CharField()
    score_p1 = serializers.IntegerField(validators=[MinValueValidator(0)])
    score_p2 = serializers.IntegerField(validators=[MinValueValidator(0)])