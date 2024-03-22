<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import TournamentPreview from '../components/TournamentPreview.vue';

const tournaments = ref([]);

const fetchTournaments = async () => {
    const res = await axios.get("https://api-arconnect.k8s.ing.he-arc.ch/api/tournaments");
    tournaments.value = res.data;
};

onMounted(() => {
    fetchTournaments();
});

</script>

<template>
    <div class="grid-container">
        <h1>Tournois</h1>
        <div class="container">
            <TournamentPreview v-for="(tournament, index) in tournaments" :tournament :key="index" class="item" />
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/breakpoints";

h1 {
    grid-column: 1 / span 12;
    grid-row: 1 / span 1;
    margin-bottom: 16px;
}

.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: start;
    gap: 8px;
    grid-column: 1 / span 12;
    grid-row: 2 / span 1;
}

.item {
    width: calc(25% - (3 * 8px / 4));
    min-width: 200px;
    aspect-ratio: 16 / 9;
}

@media(max-width: $medium-breakpoint) {
    .item {
        width: calc(50% - (3 * 8px / 4));
    }
}

@media(max-width: $small-breakpoint) {
    .item {
        width: calc(100% - (3 * 8px / 4));
    }
}
</style>