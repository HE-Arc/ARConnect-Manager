<script setup>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { stateToString } from '@/domain/TournamentStatus'

const route = useRoute();
const tournamentId = route.params.tournamentId;

const tournament = ref(null);

const fetchTournament = async () => {
    const res = await axios.get(`https://api-arconnect.k8s.ing.he-arc.ch/api/tournaments/${tournamentId}`);
    tournament.value = res.data;
};

onMounted(() => {
    fetchTournament();
});


</script>


<template>
    <div v-if="tournament" class="grid-container">
        <h1>{{ tournament.name }}</h1>
        <p>{{ tournament.description }}</p>
        <p>{{ stateToString(tournament.state) }}</p>
    </div>
</template>

<style scoped>
.grid-container * {
    grid-column: 1 / span 12;
}
</style>