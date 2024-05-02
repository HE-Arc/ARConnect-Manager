import { TournamentStatus } from "./TournamentStatus";

/** Class representing a tournament. */
export class Tournament {

    /**
     * Create a tournament.
     * @param {number} id - The ID of the tournament.
     * @param {string} name - The name of the tournament.
     * @param {string} description - The description of the tournament.
     * @param {TournamentStatus} status - The status of the tournament.
     * @param {Array} playerIds - The IDs of player that are registered for this tournament.
     * @param {String} challongeImageUrl - The status of the tournament.
     */
    constructor(id, name, description, status, playerIds, challongeImageUrl) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.status = status;
        this.playerIds = playerIds;
        this.challongeImageUrl = challongeImageUrl;
    }
}