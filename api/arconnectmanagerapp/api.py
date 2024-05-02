import challonge
import environ
import random
import re
from datetime import datetime


class ChallongeAPI():
    def __init__(self):
        env = environ.Env()
        CHALLONGE_API_USERNAME = env('CHALLONGE_API_USERNAME')
        CHALLONGE_API_KEY = env('CHALLONGE_API_KEY')
        self.match_desired_attr = ['id', 'round', 'scores_csv', 'state', 'player1_id', 'player2_id', 'winner_id']

        challonge.set_credentials(CHALLONGE_API_USERNAME, CHALLONGE_API_KEY)
        
    def create_tournament(self, name : str, participants : list):
        unique_url = re.sub(r'[^a-zA-Z0-9_]', '', name) + "_" + str(random.randint(0, 1000)) #Generate an unique URL for the tournament (only letters, numbers and _ are allowed)
        tournament = challonge.tournaments.create(name, unique_url, private=True)
        
        for participant in participants:
            challonge.participants.create(tournament['id'], participant)
        
        challonge.tournaments.start(tournament['id'])
        print(tournament['id'])
        return {"id": tournament['id'], "image_url": tournament['live_image_url']}
    
    def finalize_tournament(self, tournamentID : str):
        return challonge.tournaments.finalize(tournamentID)
    
    def get_matches(self, tournamentID: str):
        filtered_matches = []
        
        matches = challonge.matches.index(tournamentID)
        participants = challonge.participants.index(tournamentID)
        
        for match in matches:
            filtered_matches.append(self.__get_match_filtered_info(match, participants))
        
        return filtered_matches
    
    def match_update_score(self, tournamentID : str, matchID : str, p1_ID : str, score_p1 : int, p2_ID : str, score_p2 : int):
        final_score = str(score_p1) + "-" + str(score_p2)
        
        winner_id = p1_ID
        if score_p2 > score_p1:
            winner_id = p2_ID
        
        challonge.matches.update(tournamentID, matchID, scores_csv=final_score, winner_id=winner_id)
        updated_match = challonge.matches.show(tournamentID, matchID)
        return self.__get_match_filtered_info(updated_match, challonge.participants.index(tournamentID))
    
    def is_matchID_valid(self, tournamentID : str, matchID : str):
        matches = challonge.matches.index(tournamentID)
        for match in matches:
            if str(match['id']) == matchID:
                print("Match found")
                return True
        return False
    
    def are_matches_finished(self, tournamentID : str):
        matches = challonge.matches.index(tournamentID)
        for match in matches:
            if match['state'] != 'complete':
                return False
        return True
    
    def are_players_in_match(self, tournamentID : str, matchID : str, players_ID : list):
        match = challonge.matches.show(tournamentID, matchID)
        return str(match['player1_id']) in players_ID and str(match['player2_id']) in players_ID
    
    #Tools functions
    
    def __get_match_filtered_info(self, match, participants):
        filtered_match = {attr: match[attr] for attr in self.match_desired_attr if attr in match}
        filtered_match['player1_name'] = self.__get_participant_name_from_ID(participants, match['player1_id'])
        filtered_match['player2_name'] = self.__get_participant_name_from_ID(participants, match['player2_id'])
        return filtered_match
    
    def __get_participant_name_from_ID(self, participants, id):
        for participant in participants:
            if participant["id"] == id:
                return participant["name"]
        return "Unknown"