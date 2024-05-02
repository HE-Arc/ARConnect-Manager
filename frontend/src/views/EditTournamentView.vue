<script setup>
import { useRouter, useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { TournamentService } from '@/domain/TournamentService';
import { Tournament } from '@/domain/Tournament';
import { TournamentStatus } from '@/domain/TournamentStatus';

const router = useRouter();
const form = ref(null)
const route = useRoute();
const tournamentId = route.params.tournamentId;


const matches = ref(null);
const name = ref(null);
const description = ref(null);

onMounted(async () => {
    const tournament = await TournamentService.getTournamentById(tournamentId);
    name.value = tournament.name;
    description.value = tournament.description;
    matches.value = await TournamentService.getMatchesByTournamentId(tournamentId);
});

const editTournament = () => {
    if (!form.value.reportValidity()) return;

    const newTournament = new Tournament(
        tournamentId,
        name.value,
        description.value
    );

    TournamentService.updateTournament(newTournament).then((successful) => {
        if (successful) router.push({ name: "manageTournaments" });
    })
};

const sendMatchResult = (match) => {
    if (match.state != 'open') return;
    if (!document.getElementById('form-' + match.id).reportValidity()) return;
    const score1 = document.getElementById(match.id + '-' + match.player1Id).value;
    const score2 = document.getElementById(match.id + '-' + match.player2Id).value;
    TournamentService.sendMatchResult(
        tournamentId,
        match.id,
        match.player1Id,
        match.player2Id,
        parseInt(score1),
        parseInt(score2),
    ).then((successful) => {
        if (!successful) return;
        match.state = 'complete';
        match.scores = score1 + '-' + score2
    });


};

</script>

<template>
    <div class="grid-container">
        <div>
            <h1>Modifier un tournoi</h1>
            <form ref="form">
                <label for="name">Nom du tournoi :</label>
                <input id="name" type="text" name="name" placeholder="Free For All" v-model="name" required>

                <label for="description">Description :</label>
                <textarea id="description" placeholder="60 joueurs, 5 jeux, un seul vainqueur..." name="description"
                    v-model="description" required></textarea>
            </form>
            <button class="btn-primary" @click="editTournament">Modifier</button>
        </div>
        <hr>
        <div>
            <h1>Matchs</h1>
            <div v-for="match in matches" class="match-container">
                <form :id="'form-' + match.id">
                    <label :for="match.id + '-' + match.player1Id">Score de {{ match.player1Name }} :</label>
                    <input :id="match.id + '-' + match.player1Id" type="number" :name="match.id + '-' + match.player1Id"
                        placeholder="0" required :disabled="match.state != 'open'"
                        :value="match.scores === '' ? null : match.scores.split('-')[0]">


                    <label :for="match.id + '-' + match.player2Id">Score de {{ match.player2Name }} :</label>
                    <input :id="match.id + '-' + match.player2Id" type="number" :name="match.id + '-' + match.player2Id"
                        placeholder="0" required :disabled="match.state != 'open'"
                        :value="match.scores === '' ? null : match.scores.split('-')[1]">
                </form>
                <button class="btn-primary" @click="sendMatchResult(match)"
                    :disabled="match.state != 'open'">Envoyer</button>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.grid-container {
    div {
        grid-column: 1 / span 12;
    }

    hr {
        width: 100%;
        grid-column: 1 / span 12;
        margin-top: 32px;
        margin-bottom: 32px;
    }

    .match-container {
        margin-top: 16px;
        grid-column: 1 / span 12;
        align-items: center;
        display: flex;
        gap: 16px;

        form {
            display: flex;
            align-items: center;
            gap: 16px;
            margin: 0;

            input {
                height: 6
            }


        }

    }
}

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