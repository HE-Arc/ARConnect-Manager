<script setup>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';

const route = useRoute();
const tournamentId = route.params.tournamentId;

const tournament = ref(null);

const fetchTournament = async () => {
    const res = await axios.get(`http://localhost:8000/api/tournamentitems/${tournamentId}`);
    tournament.value = res.data;
};

onMounted(() => {
    fetchTournament();
});


</script>


<template>
    <div v-if="tournament">
        <h1>{{ tournament.name }}</h1>
    </div>
</template>