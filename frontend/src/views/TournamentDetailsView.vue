<script setup>
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { TournamentService } from '@/domain/TournamentService';
import { TournamentStatus } from '@/domain/TournamentStatus';

import { currentUser } from '@/domain/AuthService';

const route = useRoute();
const tournamentId = route.params.tournamentId;
const tournament = ref(null);
const isRegistered = ref(false);
const isTournamentOpen = ref(false);

onMounted(async () => {
    tournament.value = await TournamentService.getTournamentById(tournamentId);
    isRegistered.value = currentUser.value.tournamentsId.includes(tournament.value.id);
    isTournamentOpen.value = tournament.value.status.id === TournamentStatus.Open.id;
});

const register = async () => {
    if (isRegistered.value) {
        await unregister();
    } else {
        const registrationResult = await TournamentService.registerForTournament(tournamentId);
        if (registrationResult.success) {
            isRegistered.value = true;
        }
        await TournamentService.registerForTournament(tournamentId);
    }

    location.reload();
};

const unregister = async () => {
    const unregistrationResult = await TournamentService.unregisterFromTournament(tournamentId);
    if (unregistrationResult.success) {
        isRegistered.value = false;
    }
    await TournamentService.unregisterFromTournament(tournamentId);
    location.reload();
};

</script>
<template>
    <div v-if="tournament" class="grid-container">
        <h1>{{ tournament.name }}</h1>
        <p>{{ tournament.description }}</p>
        <p>{{ tournament.status }}</p>
        <p>{{ tournament.playerIds.length }} joueurs</p>


        <div v-if="isTournamentOpen">
            <button v-if="isRegistered" class="btn-primary" @click="register">Se désinscrire</button>
            <button v-else class="btn-primary" @click="register">S'inscrire</button>
        </div>
        <div v-else>
            <button class="btn-primary" disabled>Le tournoi est fermé</button>
        </div>

        <hr>

        <div v-if="tournament.status.id > 1" class="display-tournament">
            <img :src="tournament.challongeImageUrl">
        </div>
    </div>

</template>

<style scoped lang="scss">
@import "@/assets/styles/breakpoints";
@import "@/assets/styles/colors";

.grid-container * {
    grid-column: 1 / span 12;
}

.grid-container {
    div {
        margin-top: 16px;
    }

    hr {
        width: 100%;
        margin-top: 32px;
        margin-bottom: 32px;
    }
}

.btn-primary {
    grid-column: 4 / span 12;

}

.display-tournament {
    background-color: $on-primary;
    padding: 12px 16px;
    border-radius: 8px; 
}
</style>