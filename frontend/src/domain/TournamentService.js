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
                tournamentData.players ?? null,
                tournamentData.challonge_image_url ?? null,
            )
        )
    }

    /**
     * Returns the corresponding tournament by ID.
     * @param {number} id - The ID of the tournament.
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
            response.data.players ?? null,
            response.data.challonge_image_url ?? null,
        );

    }

    /**
     * Deletes a tournament.
     * @param {number} id - The ID of the tournament.
     * @return {boolean} Wether the deletion was successful.
     */
    static async deleteTournament(id) {
        const response = await axios.delete(
            `http://localhost:8000/api/tournaments/${id}`,
        );
        return response.status >= 200 && response.status < 300
    }

    /**
     * Adds a tournament.
     * @param {string} name - The name of the tournament.
     * @param {string} description - The description of the tournament.
     * @param {TournamentStatus} status - The status of the tournament.
     * 
     * @return {boolean} Wether the creation was successful.
     */
    static async addTournament(name, description) {
        let data = {
            "name": name,
            "description": description,
        };

        const response = await axios.post(
            "http://localhost:8000/api/tournaments/",
            data
        )

        return response.status >= 200 && response.status < 300
    }

    /**
     * Updates a tournament.
     * @param {Tournament} tournament - The tournament.
     * 
     * @return {boolean} Wether the update was successful.
     */
    static async updateTournament(tournament) {
        let data = {
            "name": tournament.name,
            "description": tournament.description,
        };

        const response = await axios.put(
            `http://localhost:8000/api/tournaments/${tournament.id}/`,
            data
        )

        return response.status >= 200 && response.status < 300
    }

    static async registerForTournament(tournamentId) {
        const response = await axios.post(
            `http://localhost:8000/api/tournaments/${tournamentId}/register/`,
            null
        )
        return { success: response.status >= 200 && response.status < 300, message: "Registration successful" };
    } catch(error) {
        return { success: false, message: "Registration failed" };
    }

    static async unregisterFromTournament(tournamentId) {
        const response = await axios.post(
            `http://localhost:8000/api/tournaments/${tournamentId}/unregister/`,
            null
        )
        return { success: response.status >= 200 && response.status < 300, message: "Unregistration successful" };
    } catch(error) {
        return { success: false, message: "Unregistration failed" };
    }

    /**
     * Updates a tournament status by entering the next phase.
     * @param {Tournament} tournament - The tournament.
     * 
     * @return {TournamentStatus} The updated tournament status.
     */
    static async nextTournamentStatus(tournament) {
        let endpoint;
        let resultStatus = tournament.status;
        switch (tournament.status.id) {
            case TournamentStatus.Closed.id:
                endpoint = `http://localhost:8000/api/tournaments/${tournament.id}/open_registration/`
                resultStatus = TournamentStatus.Open;
                break;
            case TournamentStatus.Open.id:
                endpoint = `http://localhost:8000/api/tournaments/${tournament.id}/start/`
                 resultStatus = TournamentStatus.Running;
                break;
            case TournamentStatus.Running.id:
                endpoint = `http://localhost:8000/api/tournaments/${tournament.id}/finish/`
                resultStatus = TournamentStatus.Completed;
                break;
            case TournamentStatus.Completed.id:
                throw new Error("Operation not permited. A completed tournament cannot change status.");
            default:
                throw new Error(`Tournament status unkown: ${tournament.status}`);
        }
        const response = await axios.post(endpoint)
        return resultStatus;
    }
}