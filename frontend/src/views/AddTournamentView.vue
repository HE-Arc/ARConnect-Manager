<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { TournamentService } from '@/domain/TournamentService';
import { TournamentStatus } from '@/domain/TournamentStatus';

const router = useRouter();
const form = ref(null)

const name = ref(null);
const description = ref(null);

const addTournament = () => {
    if (!form.value.reportValidity()) return;
    TournamentService.addTournament(
        name.value,
        description.value,
    ).then(() => {
        router.push({ name: "manageTournaments" })
    })
};
</script>

<template>
    <div class="grid-container">
        <h1>Ajouter un tournoi</h1>
        <form ref="form">
            <label for="name">Nom du tournoi :</label>
            <input id="name" type="text" name="name" placeholder="Free For All" v-model="name" required>

            <label for="description">Description :</label>
            <textarea id="description" placeholder="60 joueurs, 5 jeux, un seul vainqueur..." name="description"
                v-model="description" required></textarea>
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
    }
}

button {
    grid-column: 3 / span 4;
}
</style>