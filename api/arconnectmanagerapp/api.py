import challonge
import environ
import random
import re
from datetime import datetime

#This class interacts with the Challonge API to create and manage tournaments
class ChallongeAPI():
    def __init__(self):
        env = environ.Env()
        CHALLONGE_API_USERNAME = env('CHALLONGE_API_USERNAME')
        CHALLONGE_API_KEY = env('CHALLONGE_API_KEY')
        self.match_desired_attr = ['id', 'round', 'scores_csv', 'state', 'player1_id', 'player2_id', 'winner_id'] #Filter the attributes wanted in the match object

        challonge.set_credentials(CHALLONGE_API_USERNAME, CHALLONGE_API_KEY)
        
    def create_tournament(self, name : str, participants : list):
        """_summary_ : Create a tournament with the given name and participants
        _param_ : name : str : The name of the tournament
        _param_ : participants : list : The list of participants
        """
        unique_url = re.sub(r'[^a-zA-Z0-9_]', '', name) + "_" + str(random.randint(0, 1000)) #Generate an unique URL for the tournament (only letters, numbers and _ are allowed)
        tournament = challonge.tournaments.create(name, unique_url, private=True)
        
        for participant in participants:
            challonge.participants.create(tournament['id'], participant)
        
        challonge.tournaments.start(tournament['id'])
        print(tournament['id'])
        return {"id": tournament['id'], "image_url": tournament['live_image_url']}
    
    def finalize_tournament(self, tournamentID : str):
        """_summary_ : Finalize the tournament with the given ID
        Args:
            tournamentID (str): the ID of the tournament to finalize

        """
        return challonge.tournaments.finalize(tournamentID)
    
    def get_matches(self, tournamentID: str):
        """_summary_ : Get the list of matches in the tournament with the given ID

        Args:
            tournamentID (str): the ID of the tournament to get the matches from

        Returns:
            list: the list of matches in the tournament
        """
        filtered_matches = []
        
        matches = challonge.matches.index(tournamentID)
        participants = challonge.participants.index(tournamentID)
        
        for match in matches:
            filtered_matches.append(self.__get_match_filtered_info(match, participants))
        
        return filtered_matches
    
    def match_update_score(self, tournamentID : str, matchID : str, p1_ID : str, score_p1 : int, p2_ID : str, score_p2 : int):
        """_summary_ : Update the score of the match with the given ID

        Args:
            tournamentID (str): the ID of the tournament
            matchID (str): the ID of the match to update
            p1_ID (str): the challonge ID of the first player
            score_p1 (int): the score of the first player
            p2_ID (str): the challonge ID of the second player
            score_p2 (int): the score of the second player
        """
        final_score = str(score_p1) + "-" + str(score_p2)
        
        winner_id = p1_ID
        if score_p2 > score_p1:
            winner_id = p2_ID
        
        challonge.matches.update(tournamentID, matchID, scores_csv=final_score, winner_id=winner_id)
        updated_match = challonge.matches.show(tournamentID, matchID)
        return self.__get_match_filtered_info(updated_match, challonge.participants.index(tournamentID))
    
    def is_matchID_valid(self, tournamentID : str, matchID : str):
        """_summary_ : Check if the match with the given ID exists and is valid

        Args:
            tournamentID (str): the ID of the tournament
            matchID (str): the ID of the match to check

        Returns:
            boolean: true if the match exists and is valid, false otherwise
        """
        matches = challonge.matches.index(tournamentID)
        for match in matches:
            if str(match['id']) == matchID:
                print("Match found")
                return True
        return False
    
    def are_matches_finished(self, tournamentID : str):
        """_summary_ : Check if all the matches in the tournament are finished

        Args:
            tournamentID (str): the ID of the tournament

        Returns:
            boolean: true if all the matches are finished, false otherwise
        """
        matches = challonge.matches.index(tournamentID)
        for match in matches:
            if match['state'] != 'complete':
                return False
        return True
    
    def are_players_in_match(self, tournamentID : str, matchID : str, players_ID : list):
        """_summary_ : Check if the players with the given ID are in the match

        Args:
            tournamentID (str): the ID of the tournament
            matchID (str): the ID of the match
            players_ID (list): the list of players ID to check

        Returns:
            boolean: true if the players are in the match, false otherwise
        """
        match = challonge.matches.show(tournamentID, matchID)
        return str(match['player1_id']) in players_ID and str(match['player2_id']) in players_ID
    
    #Tools functions
    
    def __get_match_filtered_info(self, match, participants):
        """_summary_ : Get the filtered information of the match

        Args:
            match : the match object
            participants : the list of participants in the tournament

        Returns:
            dict : the filtered information of the match
        """
        filtered_match = {attr: match[attr] for attr in self.match_desired_attr if attr in match}
        filtered_match['player1_name'] = self.__get_participant_name_from_ID(participants, match['player1_id'])
        filtered_match['player2_name'] = self.__get_participant_name_from_ID(participants, match['player2_id'])
        return filtered_match
    
    def __get_participant_name_from_ID(self, participants, id):
        """_summary_ : Get the name of the participant with the given ID

        Args:
            participants : the list of all participants in the tournament
            id : the ID of the participant to get the name from

        Returns:
            string: the name of the participant
        """
        for participant in participants:
            if participant["id"] == id:
                return participant["name"]
        return "Unknown"