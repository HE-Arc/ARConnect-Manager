from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import TournamentItem
from .serializers import TournamentItemSerializer, ScoreSerializer
from .permissions import TournamentPermission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import action
from rest_framework import status

from .api import ChallongeAPI

challongeAPI = ChallongeAPI()

class TournamentItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tournament items to be viewed or edited.
    """
    queryset = TournamentItem.objects.all()
    serializer_class = TournamentItemSerializer
    permission_classes = [TournamentPermission]
    
    #Open the tournament to user registration
    @action(detail=True, methods=['post'])
    def open_registration(self, request, pk=None):
        tournament = self.get_object()
        if tournament.state != 0:
            return HttpResponse('The tournament has already been opened', status=400)
        
        tournament.state = 1
        tournament.save()
        
        return HttpResponse(status=204)
    
    #Register a user to the tournament
    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        tournament = self.get_object()
        if tournament.state != 1:
            return HttpResponse('The tournament is not open to registration modification', status=403)
        
        tournament.players.add(request.user)
        tournament.save()
        
        return HttpResponse(status=204) #OK - NO CONTENT
    
    #Unregister a user from the tournament
    @action(detail=True, methods=['post'])
    def unregister(self, request, pk=None):
        tournament = self.get_object()
        if tournament.state != 1:
            return HttpResponse('The tournament is not open to registration modification', status=403)
        
        tournament.players.remove(request.user)
        tournament.save()
        
        return HttpResponse(status=204) #OK - NO CONTENT
    
    #Start the tournament and create it on Challonge
    @action(detail=True, methods=['post'], url_path='start')
    def api_start(self, request, pk=None):
        tournament = self.get_object()
        
        if tournament.state != 1:
            return HttpResponse('The tournament is not ready or has already been started. Check the tournament state first', status=400)
        
        participants = tournament.players.all().values_list('username', flat=True)
        if len(participants) < 2:
            return HttpResponse('Not enough participants (minimum 2 are required)', status=400)
        
        response = challongeAPI.create_tournament(tournament.name, participants)
        
        tournament.challonge_id = response['id']
        tournament.challonge_image_url = response['image_url']
        tournament.state = 2
        tournament.save()
        
        return HttpResponse(status=201) #OK - CREATED
    
    #Finish the tournament on Challonge
    @action(detail=True, methods=['post'], url_path='finish')
    def api_finish(self, request, pk=None):
        tournament = self.get_object()
        
        if tournament.state != 2:
            return HttpResponse('The tournament has not been started yet or is already finished', status=400)
        
        if challongeAPI.are_matches_finished(tournament.challonge_id) == False:
            return HttpResponse('Not all matches have been played yet. Please submit all scores first', status=400)
        
        if tournament.challonge_id == '':
            return HttpResponse('The tournament has not been started yet or is already finished', status=400)
        
        challongeAPI.finalize_tournament(tournament.challonge_id)
        
        tournament.state = 3
        tournament.save()
        
        return HttpResponse(status=204) #OK - NO CONTENT

    #Get the matches of the tournament on Challonge
    @action(detail=True, methods=['post'], url_path='matches')
    def api_get_matches(self, request, pk=None):
        tournament = self.get_object()
        
        if tournament.challonge_id == '':
            return HttpResponse('The tournament has not been started yet', status=400)
        
        return JsonResponse(challongeAPI.get_matches(tournament.challonge_id), safe=False)
    
    #Submit the scores of a match on Challonge
    @action(detail=True, methods=['post'], url_path='scores')
    def api_submit_scores(self, request, pk=None):
        serializer = ScoreSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        tournament = self.get_object()
        
        matchID = request.data.get('match_id')
        score_p1 = request.data.get('score_p1')
        score_p2 = request.data.get('score_p2')
        p1_id = request.data['player1_id']
        p2_id = request.data['player2_id']
        
        if tournament.challonge_id == '':
            return HttpResponse('The tournament has not been started yet', status=400)
        
        if tournament.state != 2:
            return HttpResponse('The tournament has not been started or is already finished', status=400)
        
        if challongeAPI.is_matchID_valid(tournament.challonge_id, matchID) == False:
            return HttpResponse('The match ID is incorrect', status=400)
        
        if p1_id == p2_id:
            return HttpResponse('Players ID must be different', status=400)
        
        if challongeAPI.are_players_in_match(tournament.challonge_id, matchID, [p1_id, p2_id]) == False:
            return HttpResponse('The specified players ID are incorrect/not in the match', status=400)
        
        match = challongeAPI.match_update_score(tournament.challonge_id, matchID, p1_id, score_p1, p2_id, score_p2)
        
        return JsonResponse(match, safe=False)

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
