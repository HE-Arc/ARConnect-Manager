<script setup>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { TournamentService } from '@/domain/TournamentService';

const route = useRoute();
const tournamentId = route.params.tournamentId;
const tournament = ref(null);

onMounted(async () => {
    tournament.value = await TournamentService.getTournamentById(tournamentId);
});


</script>


<template>
    <div v-if="tournament" class="grid-container">
        <h1>{{ tournament.name }}</h1>
        <p>{{ tournament.description }}</p>
        <p>{{ tournament.status }}</p>
    </div>
</template>

<style scoped>
.grid-container * {
    grid-column: 1 / span 12;
}
</style>