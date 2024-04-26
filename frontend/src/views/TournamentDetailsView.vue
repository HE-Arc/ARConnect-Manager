<script setup>
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { TournamentService } from '@/domain/TournamentService';
import { currentUser } from '@/domain/AuthService';

const route = useRoute();
const tournamentId = route.params.tournamentId;
const tournament = ref(null);
const isRegistered = ref(false);

onMounted(async () => {
    tournament.value = await TournamentService.getTournamentById(tournamentId);
    isRegistered.value = currentUser.value.tournamentsId.includes(tournament.value.id);
});

const register = async () => {
    if (isRegistered.value) {
        await unregister();
    } else {
        const registrationResult = await TournamentService.registerForTournament(tournamentId);
        if (registrationResult.success) {
            // Inscription réussie, afficher le message de succès
            alert(registrationResult.message);
            isRegistered.value = true;
        } else {
            // Inscription échouée, afficher le message d'erreur
            alert(registrationResult.message);
        }
    }
};

const unregister = async () => {
    const unregistrationResult = await TournamentService.unregisterFromTournament(tournamentId);
    if (unregistrationResult.success) {
        // Désinscription réussie, afficher le message de succès
        alert(unregistrationResult.message);     
        isRegistered.value = false;   
    } else {
        // Désinscription échouée, afficher le message d'erreur
        alert(unregistrationResult.message);
    }
};

</script>
<template>
    <div v-if="tournament" class="grid-container">
    <h1>{{ tournament.name }}</h1>
    <p>{{ tournament.description }}</p>
    <p>{{ tournament.status }}</p>
    <button v-if="isRegistered" class="btn-primary" @click="register">Se désinscrire</button>
    <button v-else class="btn-primary" @click="register">S'inscrire</button>
</div>

</template>

<style scoped>
.grid-container * {
    grid-column: 1 / span 12;
}
</style>