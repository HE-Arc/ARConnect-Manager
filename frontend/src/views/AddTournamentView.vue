<script setup>
import { Label } from 'radix-vue'
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

let tournamentName;
let tournamentDescription;
let tournamentState;

const addTournament = () => {
    let data = {
        "name": tournamentName,
        "description": tournamentDescription,
        "state": parseInt(tournamentState)
    };

    axios.post(
        "http://localhost:8000/api/tournaments/ ",
        data
    ).then(() => {
        router.push({ name: "manageTournaments" })
    })
};
</script>

<template>
    <div class="grid-container">
        <h1>Ajouter un tournoi</h1>
        <form>
            <Label for="tournamentName">Nom du tournoi :</Label>
            <input id="firstName" type="text" placeholder="Free For All" v-model="tournamentName" required>

            <Label for="tournamentDescription">Description :</Label>
            <textarea id="tournamentDescription" placeholder="60 joueurs, 5 jeux, un seul vainqueur..."
                v-model="tournamentDescription" required></textarea>

            <Label for="tournamentState">État :</Label>
            <select id="tournamentState" v-model="tournamentState" required>
                <option value="0">Fermé</option>
                <option value="1">Ouvert</option>
                <option value="2">En cours</option>
                <option value="3">Terminé</option>
            </select>

        </form>
        <button class="btn-primary" @click="addTournament">Ajouter</button>
    </div>
</template>

<style lang="scss" scoped>
h1,
form {
    grid-column: 1 / span 12;
}

form {
    margin-top: 32px;
    margin-bottom: 32px;
    display: grid;
    align-items: end;
    grid-template-columns: repeat(12, 1fr);
    gap: 16px;

    label {
        grid-column: 1 / span 2;
        height: 32px;
    }

    input,
    textarea,
    select {
        grid-column: 3 / span 4;
        height: 32px;
    }
}
</style>