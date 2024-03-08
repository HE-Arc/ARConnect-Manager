<script setup></script>

<template>
  <nav reveal elevated class="bg-grey-10 text-white" height-hint="68">
    <div>
      <router-link id="home-link" :to="{ name: 'home' }"><img src="@/assets/images/logo_white_text.svg"></router-link>
    </div>
    <div>
      <router-link :to="{ name: 'tournaments' }">Tournois</router-link>
      <router-link :to="{ name: 'login' }">Se connecter</router-link>
    </div>
  </nav>
</template>

<style scoped>
#home-link img{
  height: 1rem;
}
nav {
  display: flex;
  background-image: url("@/assets/images/arconnect_foreground.png");
  background-position: 0px 0px;
  padding: 14px 48px 14px 48px;
  justify-content: space-between;
}

q-toolbar-title img {
  height: 1rem;

}

</style>