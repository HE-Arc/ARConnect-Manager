import { Tournament } from "./Tournament";
import { TournamentStatus } from "./TournamentStatus";
import axios from 'axios';

/** Utility class to request the API on tournament items. */
export class TournamentService {

    /**
     * Returns all tournaments.
     * 
     * @return {Tournament[]} The array of tournaments.
     */
    static async getAllTournaments() {
        const response = await axios.get("http://localhost:8000/api/tournaments");
        if (response.status < 200 || response.status > 299) return;
        return response.data.map(
            (tournamentData) => new Tournament(
                tournamentData.id,
                tournamentData.name,
                tournamentData.description,
                TournamentStatus.fromId(tournamentData.state),
            )
        )
    }

    /**
     * Returns all tournaments.
     * 
     * @return {Tournament} The tournament.
     */
    static async getTournamentById(id) {
        const response = await axios.get(`http://localhost:8000/api/tournaments/${id}`);
        if (response.status < 200 || response.status > 299) return;
        return new Tournament(
            response.data.id,
            response.data.name,
            response.data.description,
            TournamentStatus.fromId(response.data.state),
        );

    }



}