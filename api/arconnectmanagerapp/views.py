from django.shortcuts import render
from rest_framework import viewsets
from .models import TournamentItem
from .serializers import TournamentItemSerializer

# Create your views here.

class TournamentItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tournament items to be viewed or edited.
    """
    queryset = TournamentItem.objects.all()
    serializer_class = TournamentItemSerializer