<script setup></script>

<template>
  <nav reveal elevated class="bg-grey-10 text-white" height-hint="68">
    <div id="navbar-home">
      <router-link id="home-link" :to="{ name: 'home' }"><img src="@/assets/images/logo_white_text.svg"></router-link>
    </div>
    <div id="navbar-links">
      <router-link :to="{ name: 'tournaments' }">Tournois</router-link>
      <router-link class="btn-primary" :to="{ name: 'login' }">Se connecter</router-link>
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
  padding: 14px 64px 14px 64px;
  justify-content: space-between;
  align-items: center;
}

div#navbar-links {
  display: flex;
  gap: 64px;
  justify-content: space-around;
  align-items: center;
}

q-toolbar-title img {
  height: 1rem;
}

nav div {
  font-size: 0.8rem;
}

a {
  text-decoration: none;
  font-weight: 800;
  color: white;
  text-transform: uppercase;
}
</style>