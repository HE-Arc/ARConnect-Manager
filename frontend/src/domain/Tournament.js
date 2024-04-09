import { TournamentStatus } from "./TournamentStatus";

/** Class representing a tournament. */
export class Tournament {

    /**
     * Create a point.
     * @param {number} id - The ID of the tournament.
     * @param {string} name - The name of the tournament.
     * @param {string} description - The description of the tournament.
     * @param {TournamentStatus} status - The status of the tournament.
     */
    constructor(id, name, description, status) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.status = status;
    }
}