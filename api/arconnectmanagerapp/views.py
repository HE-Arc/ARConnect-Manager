from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import TournamentItem
from .serializers import TournamentItemSerializer
from .permissions import TournamentPermission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import action
from rest_framework import status


class TournamentItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tournament items to be viewed or edited.
    """
    queryset = TournamentItem.objects.all()
    serializer_class = TournamentItemSerializer
    permission_classes = [TournamentPermission]
    
    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        tournament = self.get_object()
        if tournament.state != 1:
            return HttpResponse('The tournament is not open to registration modification', status=403)
        
        tournament.players.add(request.user)
        
        return HttpResponse(status=204) #OK NO CONTENT
    
    @action(detail=True, methods=['post'])
    def unregister(self, request, pk=None):
        tournament = self.get_object()
        tournament.players.remove(request.user)
        if tournament.state != 1:
            return HttpResponse('The tournament is not open to registration modification', status=403)
        
        return HttpResponse(status=204) #OK NO CONTENT
    
    

class UserView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user_info = {
            'username': user.username,
            'isAdmin': user.is_staff,
            'tournaments': user.players.all().values_list('pk', flat=True)
        }
            
        content = {'user_info': user_info}
        
        return Response(content)
