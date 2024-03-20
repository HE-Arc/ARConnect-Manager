<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import TournamentPreview from '../components/TournamentPreview.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const tournaments = ref([]);

const fetchTournaments = async () => {
    const res = await axios.get("http://localhost:8000/api/tournaments");
    tournaments.value = res.data;
};

function navigateToTournamentDetails() {
    router.push({ name: "addTournament" })
}

onMounted(() => {
    fetchTournaments();
});

</script>

<template>
    <div class="grid-container">
        <h1>Gérer les tournois</h1>
        <div class="container">
            <TournamentPreview v-for="(tournament, index) in tournaments" :tournament :key="index" class="item" />
            <div class="item" id="add-button" @click="navigateToTournamentDetails">
                <span class="material-symbols-outlined">
                    add
                </span>
            </div>
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

#add-button {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 1em;
    background-color: #090909;
    text-align: center;
    transition: all 0.25s ease-out;

    &:hover {
        scale: 105%;
        cursor: pointer;
        box-shadow: rgba($color: #000000, $alpha: 0.2) 0px 0px 10px 10px;
    }

    p {
        margin: 16px;
    }

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