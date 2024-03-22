<script setup>
import { Label } from 'radix-vue'
import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const router = useRouter();
const form = ref(null)

let name;
let description;
let state;

const addTournament = () => {
    if (!form.value.reportValidity()) return;
    let data = {
        "name": name,
        "description": description,
        "state": parseInt(state)
    };

    axios.post(
        "https://api-arconnect.k8s.ing.he-arc.ch/api/tournaments/ ",
        data
    ).then(() => {
        router.push({ name: "manageTournaments" })
    })
};
</script>

<template>
    <div class="grid-container">
        <h1>Ajouter un tournoi</h1>
        <form ref="form">
            <Label for="name">Nom du tournoi :</Label>
            <input id="name" type="text" name="name" placeholder="Free For All" v-model="name" required>

            <Label for="description">Description :</Label>
            <textarea id="description" placeholder="60 joueurs, 5 jeux, un seul vainqueur..." name="description"
                v-model="description" required></textarea>

            <Label for="state">État :</Label>
            <select id="state" v-model="state" required name="state">
                <option value="0">Fermé</option>
                <option value="1">Ouvert</option>
                <option value="2">En cours</option>
                <option value="3">Terminé</option>
            </select>
        </form>
        <button class="btn-primary" @click="addTournament">Ajouter</button>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/breakpoints";

h1,
form {
    grid-column: 1 / span 12;
}

form {
    margin-top: 32px;
    margin-bottom: 32px;
    display: grid;
    align-items: end;
    grid-template-columns: repeat(12, 1fr);
    gap: 16px;

    label {
        grid-column: 1 / span 2;
        height: 32px;
    }

    input,
    textarea,
    select {
        grid-column: 3 / span 4;
        height: 32px;
    }
}

button {
    grid-column: 3 / span 4;
    height: 32px;
}

@media(max-width: $medium-breakpoint) {

    form {
        label {
            grid-column: 1 / span 4;
        }

        input,
        textarea,
        select {
            grid-column: 5 / span 8;
            height: 32px;
        }
    }

    button {
        grid-column: 5 / span 8;
        height: 32px;
    }
}

@media(max-width: $small-breakpoint) {

    form {
        label {
            grid-column: 1 / span 12;
        }

        input,
        textarea,
        select {
            grid-column: 1 / span 12;
            height: 32px;
        }
    }

    button {
        grid-column: 1 / span 12;
        height: 32px;
    }
}
</style>