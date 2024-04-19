<script setup>
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { TournamentService } from '@/domain/TournamentService';

const route = useRoute();
const tournamentId = route.params.tournamentId;
const tournament = ref(null);

onMounted(async () => {
    tournament.value = await TournamentService.getTournamentById(tournamentId);
});

const register = async () => {
    const registrationResult = await TournamentService.registerForTournament(tournamentId);
    if (registrationResult.success) {
        // Registration successful, display success message
        alert(registrationResult.message);
    } else {
        // Registration failed, display error message
        alert(registrationResult.message);
    }
};

</script>


<template>
    <div v-if="tournament" class="grid-container">
        <h1>{{ tournament.name }}</h1>
        <p>{{ tournament.description }}</p>
        <p>{{ tournament.status }}</p>
        <button class="btn-primary" @click="register">S'inscrire</button>
    </div>
</template>

<style scoped>
.grid-container * {
    grid-column: 1 / span 12;
}
</style>