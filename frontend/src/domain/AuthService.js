import axios from 'axios';
import { ref } from 'vue';

export const authenticated = ref(document.cookie != null);

/** Utility class to manage authentication and make requests to the API.*/
export class AuthService {


    /**
     * Registers a new user.
     * @param {string} email - The email of the user.
     * @param {string} password - The password of the user.
     * @param {string} passwordConfirmation - The password confirmation.
     * 
     * @return {boolean} Wether the operation was successful.
     */
    static async register(email, password, passwordConfirmation) {
        let data = {
            "username": email,
            "password1": password,
            "password2": passwordConfirmation,
        };

        let response = null;
        try {
            response = await axios.post(
                `http://localhost:8000/api/user/register/`,
                data
            );
        } catch (error) {
            alert(error.response.data.password1[0]);
            return false;
        }

        console.log(response);

        return response.status >= 200 && response.status < 300

    }

    /**
     * Logs in the user and saves the authentication token inside browser cookies.
     * @param {string} email - The email of the user.
     * @param {string} password - The password of the user.
     * 
     * @return {string} The authentication token that was saved.
     */
    static async login(email, password) {
        let data = {
            "username": email,
            "password": password,
        };

        const response = await axios.post(
            `http://localhost:8000/api/user/login/`,
            data
        )

        if (response.status < 200 || response.status >= 300) {
            authenticated.value = false;
            return null;
        };

        document.cookie = response.data.key
        authenticated.value = true;

        return response.data.key;

    }

    /**
     * Logs out the user and destroys the authentication token inside browser cookies and inside the API.
     * 
     * @return {string} Wether the operation was successful.
     */
    static async logout() {
        const token = document.cookie;
        const response = await axios.post(
            `http://localhost:8000/api/user/logout/`,
            {
                headers: {
                    "Authorization: Token": token,
                }
            }
        )
        if (response.status >= 200 && response.status < 300) {
            document.cookie = null;
            authenticated.value = false;
            return true;
        }
        return false;


    }



}