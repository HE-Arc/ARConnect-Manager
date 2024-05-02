<script setup>
import { ref, resolveDirective } from 'vue';
import { currentUser, AuthService } from '@/domain/AuthService';
import { useRouter } from 'vue-router';

const router = useRouter();

const isActive = ref(false);

const toggleMenu = () => {
  alert("Sorry! The mobile menu hasn't been implemented yet.\nCome back later or use a desktop.")
  isActive.value = !isActive.value;
}

const logout = () => {
  AuthService.logout().then(() => {
    router.push({ name: 'home' });
  })
 
}

</script>

<template>
  <nav reveal elevated class="bg-grey-10 text-white" height-hint="68" :class="{ 'active': !isActive }">
    <div id="navbar-home">
      <router-link id="home-link" :to="{ name: 'home' }"><img src="@/assets/images/logo_white_text.svg"></router-link>
    </div>
    <div id="navbar-links">
      <router-link v-if="currentUser && currentUser.isAdmin" :to="{ name: 'manageTournaments' }">Administration</router-link>
      <router-link :to="{ name: 'tournaments' }">Tournois</router-link>
      <button v-if="currentUser" class="btn-primary" @click="logout">Se déconnecter</button>
      <router-link v-else class="btn-primary" :to="{ name: 'login' }">Se connecter</router-link>
    </div>
    <div id="hamburger-menu" class="material-symbols-outlined hidden" @click="toggleMenu">
      menu
    </div>
  </nav>
</template>

<style scoped lang="scss">
@import "@/assets/styles/breakpoints";

#home-link img {
  height: 1.2rem;
}

nav {
  display: flex;
  padding: 1em 3% 1em 3%;
  justify-content: space-between;
  align-items: center;
}

#navbar-home {
  display: flex;
  justify-content: center;

  a {
    display: flex;
  }

  z-index: 1;
}

#navbar-links {
  display: flex;
  gap: 5%;
  justify-content: end;
  align-items: center;
  flex: 1;
  z-index: 1;
}

a {
  text-decoration: none;
  color: white;
  text-transform: uppercase;
}

#hamburger-menu {
  display: none;
  font-size: 38px;
  z-index: 1;
  user-select: none;

  &:hover {
    cursor: pointer;
  }
}



@media(max-width: $medium-breakpoint) {
  #navbar-links {
    display: none;
  }

  #hamburger-menu {
    display: flex;
    align-items: end;
    justify-self: end;
  }
}
</style>