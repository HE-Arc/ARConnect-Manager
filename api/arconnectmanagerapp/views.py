from django.shortcuts import render
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


class TournamentItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tournament items to be viewed or edited.
    """
    queryset = TournamentItem.objects.all()
    serializer_class = TournamentItemSerializer
    permission_classes = [TournamentPermission]
    

class UserView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user_info = {
            'username': user.username,
            'isAdmin': user.is_staff,
        }
            
        content = {'user_info': user_info}
        
        return Response(content)