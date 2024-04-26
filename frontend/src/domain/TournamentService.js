import { Tournament } from "./Tournament";
import { TournamentStatus } from "./TournamentStatus";
import axios from 'axios';
import { getCookie } from "./Cookies";

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
    static async addTournament(name, description, status) {
        let data = {
            "name": name,
            "description": description,
            "state": parseInt(status.id),
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
            "state": parseInt(tournament.status.id),
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
        } catch (error) {
            return { success: false, message: "Registration failed" };
    }

    static async unregisterFromTournament(tournamentId) {
        const response = await axios.post(
            `http://localhost:8000/api/tournaments/${tournamentId}/unregister/`,
            null
        ) 
        return { success: response.status >= 200 && response.status < 300, message: "Unregistration successful" };
        } catch (error) {
            return { success: false, message: "Unregistration failed" };
    }
}