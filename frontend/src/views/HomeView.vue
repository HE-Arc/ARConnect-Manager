<template>
    <div class="grid-container">
        <h1>Osez, Pensez, Jouez</h1>
        <p id="description">
            Rejoignez des dizaines de membres de la HE-Arc
            dans un évènement dédié aux jeux-vidéos,
            à la compétition et à la communauté !
        </p>
        <router-link :to="{ name: 'tournaments' }" class="btn-primary">Découvrir</router-link>
    </div>
</template>


<style scoped lang="scss">
h1 {
    margin-top: 25vh;
    font-size: 3rem;
    grid-column: 3 / span 6;

}

p#description {
    grid-column: 3 / span 4;
}

a.btn-primary {
    grid-column-start: 3;
}
</style>