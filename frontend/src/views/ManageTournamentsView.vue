<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { TournamentService } from '../domain/TournamentService';

const router = useRouter();

const tournaments = ref([]);

onMounted(async () => {
    tournaments.value = await TournamentService.getAllTournaments();
});

</script>

<template>
    <div class="grid-container">
        <h1>Gérer les tournois</h1>
        <div class="container">
            <div class="tournament-headers">
                <div>Nom</div>
                <div>Description</div>
                <div>Status</div>
            </div>
            <div v-for="(tournament, index) in tournaments" class="tournament-item">
                <div>{{ tournament.name }}</div>
                <div>{{ tournament.description }}</div>
                <div>{{ (tournament.status) }}</div>
                <hr>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/breakpoints";
@import "@/assets/styles/colors";

h1 {
    grid-column: 1 / span 12;
    grid-row: 1 / span 1;
    margin-bottom: 16px;
}

.container {
    grid-column: 1 / span 12;
    grid-row: 2 / span 1;

    display: grid;
    grid-template-columns: repeat(12, 1fr);

    gap: 8px;

    background-color: $surface;

    padding: 32px;
    border-radius: 16px;

    .tournament-item,
    .tournament-headers {
        grid-column: 1 / span 12;
        display: grid;
        grid-template-columns: repeat(12, 1fr);

        & div:nth-child(1) {
            grid-column: span 3;
        }

        & div:nth-child(2) {
            grid-column: span 8;
        }

        & div:nth-child(3) {
            grid-column: span 1;
        }

        hr {
            grid-column: span 12;
            width: 100%;
            color: $surface;
        }
    }

    .tournament-headers {
        font-size: 1.4rem;
    }
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