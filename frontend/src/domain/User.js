/** Class representing a User. */
export class User {

    /**
     * Creates a user.
     * @param {bool} isAdmin - Wether the user is an administrator.
     * @param {string} username - The username of the user.
     */
    constructor(isAdmin, username) {
        this.isAdmin = isAdmin;
        this.username = username;
    }
}