import axios from 'axios';
import { ref } from 'vue';
import { setCookie, getCookie, deleteAllCookies } from "./Cookies";
import { User } from './User';

/** Utility class to manage authentication and make requests to the API.*/
export class AuthService {


    /**
     * Registers a new user.
     * @param {string} username - The username of the user.
     * @param {string} password - The password of the user.
     * @param {string} passwordConfirmation - The password confirmation.
     * 
     * @return {boolean} Wether the operation was successful.
     */
    static async register(username, password, passwordConfirmation) {
        const hash = await this.hashString(password);
        const hashConf = await this.hashString(passwordConfirmation);

        let data = {
            "username": username,
            "password1": hash,
            "password2": hashConf,
        };

        let response = null;
        try {
            response = await axios.post(
                `${import.meta.env.VITE_API_URL}/user/register/`,
                data
            );
        } catch (error) {
            alert(error.response.data.password1[0]);
            return false;
        }

        return response.status >= 200 && response.status < 300

    }

    /**
     * Logs in the user and saves the authentication token inside browser cookies.
     * @param {string} username - The username of the user.
     * @param {string} password - The password of the user.
     * 
     * @return {string} The authentication token that was saved.
     */
    static async login(username, password) {
        const hash = await this.hashString(password);

        let data = {
            "username": username,
            "password": hash,
        };



        const response = await axios.post(
            `${import.meta.env.VITE_API_URL}/user/login/`,
            data
        )

        if (response.status < 200 || response.status >= 300) {
            currentUser.value = null;
            return null;
        };

        setCookie("authtoken", response.data.key, 1000000);
        axios.defaults.headers['Authorization'] = `Token ${response.data.key}`;

        const userResponse = await axios.get(`${import.meta.env.VITE_API_URL}/user/`);
        if (userResponse.status < 200 || userResponse.status >= 300) {
            currentUser.value = null;
            return null;
        };

        currentUser.value = new User(userResponse.data.user_info.isAdmin, userResponse.data.user_info.username, userResponse.data.user_info.tournaments);

        return response.data.key;

    }

    /**
     * Logs out the user and destroys the authentication token inside browser cookies and inside the API.
     * 
     * @return {string} Wether the operation was successful.
     */
    static async logout() {
        const response = await axios.post(
            `${import.meta.env.VITE_API_URL}/user/logout/`,
        )
        if (response.status >= 200 && response.status < 300) {
            currentUser.value = null;
            deleteAllCookies();
            axios.defaults.headers['Authorization'] = null;
            return true;
        }
        return false;


    }

    /**
     * Gets the current user using the auth cookie.
     * 
     * If the cookie is not set, does nothing.
     */
    static async getUserFromCookie() {
        const token = getCookie("authtoken");
        if (token == null) return;
        axios.defaults.headers['Authorization'] = `Token ${token}`;
        try {
            const response = await axios.get(`${import.meta.env.VITE_API_URL}/user/`);
            if (response.status < 200 || response.status >= 300) return;
            return new User(response.data.user_info.isAdmin, response.data.user_info.username, response.data.user_info.tournaments);
        } catch {
            return null;
        }
    }


    /**
     * Hashes a string using the SHA-256 algorithm.
     * @param {string} str - The string to be hashed.
     * @returns {Promise<string>} A Promise that resolves with the hexadecimal hash string.
     */
    static async hashString(str) {
        // Convert the string to an array buffer
        const encoder = new TextEncoder();
        const data = encoder.encode(str);

        // Hash the data using SHA-256 algorithm
        const hashBuffer = await crypto.subtle.digest('SHA-256', data);

        // Convert the hash buffer to a hex string
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');

        return hashHex;
    }
}


/**
 * A reactive value (Vue Reference) containing the current user.
 * 
 * This ref can be used in Vue components to modify the UI depending on 
 * the current auth state or permission level.
 */
export const currentUser = ref(await AuthService.getUserFromCookie());