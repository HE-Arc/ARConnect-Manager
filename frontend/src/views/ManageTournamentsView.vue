<script setup>
import { ref, onMounted } from 'vue';
import { TournamentService } from '@/domain/TournamentService';
import { useRouter } from 'vue-router';
import { TournamentStatus } from '../domain/TournamentStatus';

const router = useRouter();
const tournaments = ref([]);
const loading = ref(false);


function deleteTournament(id,name) {
    let text = prompt("Êtes-vous sûr de vouloir supprimer le tournoi ?\nSi oui, tapez \"" + name + "\" pour confirmer");

    if(text ==name){
        
        TournamentService.deleteTournament(id).then((successful) => {
            if (!successful) return;
            tournaments.value = tournaments.value.filter((tournament) => tournament.id != id);
            });
    }
   
}

function editTournament(id) {
    router.push({ name: "editTournament", params: { tournamentId: id } })
}

function addTournament() {
    router.push({ name: "addTournament" })
}

function nextTournamentStatus(tournament) {
    if (tournament.status.id == TournamentStatus.Completed.id) return;
    loading.value = true; 
    TournamentService.nextTournamentStatus(tournament).then((newStatus) => {
        const index = tournaments.value.indexOf(tournament);
        tournaments.value[index].status = newStatus;
        loading.value = false; 
    }).catch(() => {
        loading.value = false; 
    });
}

onMounted(async () => {
    tournaments.value = await TournamentService.getAllTournaments();
});

</script>

<template>
    <div class="grid-container">
        <h1>
            Gérer les tournois
            <span @click="addTournament" class="material-symbols-outlined"
            title="Cliquez pour ajouter un tournoi">
                add
            </span>
        </h1>

        <div class="container">
            <div class="tournament-headers">
                <div>Nom</div>
                <div>Description</div>
                <div>Status</div>
                <div></div>
            </div>
            <div v-for="(tournament, index) in tournaments" class="tournament-item">
                <div>{{ tournament.name }}</div>
                <div>{{ tournament.description }}</div>
                <div>
                    {{ (tournament.status) }}
                </div>
                <div>
                    <template v-if="tournament.playerIds && tournament.playerIds.length >= 2">
                        <span @click="nextTournamentStatus(tournament)" class="material-symbols-outlined"
                            :class="{ 'disabled': tournament.status.id == TournamentStatus.Completed.id || tournament.loading }"
                            title="Cliquez pour passer au prochain statut">next_plan</span>
                    </template>
                    <template v-else>
                        <span class="material-symbols-outlined" 
                        title="Pas assez de joueurs">
                            cancel
                        </span>
                    </template>
                    <span @click="deleteTournament(tournament.id, tournament.name)" class="material-symbols-outlined"
                        title="Cliquez pour supprimer le tournoi">
                        delete
                    </span>
                    <span @click="editTournament(tournament.id)" class="material-symbols-outlined"
                        title="Cliquez pour modifier le tournoi">
                        edit
                    </span>
                    <div v-if="loading" class="loading-spinner"></div>

                </div>
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

    span {
        cursor: pointer;
        margin-left: 16px;
    }

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
            grid-column: span 7;
        }

        & div:nth-child(3) {
            grid-column: span 1;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: left;
            gap: 8px;

            span {
                cursor: pointer;
            }
        }

        & div:nth-child(4) {
            grid-column: span 1;
            display: flex;
            justify-content: space-around;
            align-items: center;
            -webkit-user-select: none;
            /* Safari */
            -ms-user-select: none;
            /* IE 10 and IE 11 */
            user-select: none;
            /* Standard syntax */

            span:hover {
                cursor: pointer;
            }

            span.disabled:hover {
                cursor: not-allowed;
            }

        }

        hr {
            grid-column: span 12;
            width: 100%;
            color: $surface;
        }

        &:last-child {
            hr {
                display: none;
            }
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

.loading-spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #09f;
    border-radius: 50%;
    width: 20%;
    height: 100%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

.disabled {
    pointer-events: none; 
    opacity: 0.5;
}

</style>