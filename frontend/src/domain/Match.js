/** Class representing a match. */
export class Match {

    /**
     * Create a match.
     * @param {number} id - The ID of the tournament.
     * @param {number} round - The number of the round the match is in.
     * @param {string} scores - The current score of the match.
     * @param {string} state - The current state of the match.
     * @param {number} player1Id - The Challonge ID of player 1.
     * @param {number} player2Id - The Challonge ID of player 2.
     * @param {number} winnerId - The Challonge ID of the winning player.
     * @param {number} player1Name - The name player 1.
     * @param {number} player2Name - The name of player 2.
     * 
     */
    constructor(id, round, scores, state, player1Id, player2Id, winnerId, player1Name, player2Name) {
        this.id = id;
        this.round = round;
        this.scores = scores;
        this.state = state;
        this.player1Id = player1Id;
        this.player2Id = player2Id;
        this.winnerId = winnerId;
        this.player1Name = player1Name;
        this.player2Name = player2Name;
    }
}