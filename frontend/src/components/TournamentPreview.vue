<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps(['tournament'])
const tournament = props.tournament;

function navigateToTournamentDetails() {
    router.push({ name: "tournamentDetails", params: { tournamentId: tournament.id } })
}
</script>


<template class="test">
    <div class="tournament-container" @click="navigateToTournamentDetails">
        <p>{{ tournament.name }}</p>
    </div>

</template>


<style lang="scss" scoped>
.tournament-container {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 1em;
    background-image: url("@/assets/images/arconnect_background.png");
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
</style>