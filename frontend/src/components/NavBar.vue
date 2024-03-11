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

<style scoped lang="scss">
#home-link img {
  height: 1.2rem;
}

nav {
  display: flex;
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

a {
  text-decoration: none;
  color: white;
  text-transform: uppercase;
}
</style>