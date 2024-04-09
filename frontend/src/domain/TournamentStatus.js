/** Class representing a tournament status. */
export class TournamentStatus {

    static Closed = new TournamentStatus(0)
    static Open = new TournamentStatus(1)
    static Running = new TournamentStatus(2)
    static Completed = new TournamentStatus(3)

    /**
     * Create a tournament status.
     * @param {number} id - An integer representing the ID of the status.
     */
    constructor(id) {
        this.id = id;
    }

    /**
     * Returns the corresponding tournament status based on an ID.
     * @param {number} id - An integer representing the ID of the status.
     */
    static fromId(id) {
        switch (id) {
            case 0:
            case "0":
                return this.Closed;
            case 1:
            case "1":
                return this.Open;
            case 2:
            case "2":
                return this.Running;
            case 3:
            case "3":
                return this.Completed;
        }
    }

    toString() {
        switch (this.id) {
            case 0:
                return "Fermé";
            case 1:
                return "Ouvert";
            case 2:
                return "En cours";
            case 3:
                return "Terminé";
            default:
                return "Status du tournoi";
        }
    }
}