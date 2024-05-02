/** Class representing a User. */
export class User {

    /**
     * Creates a user.
     * @param {bool} isAdmin - Wether the user is an administrator.
     * @param {string} username - The username of the user.
     * @param {Array} tournamentsId - The tournaments the user is participating in.
     */
    constructor(isAdmin, username, tournamentsId) {
        this.isAdmin = isAdmin;
        this.username = username;
        this.tournamentsId = tournamentsId;
    }
}