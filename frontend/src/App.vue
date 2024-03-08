<script setup>
import NavBar from '@/components/NavBar.vue';
</script>

<template>
  <div id="main">
    <NavBar />
    <router-view />
  </div>
</template>

<style scoped>
div#main {
  background-image: url("@/assets/images/arconnect_foreground.png");
  background-position: 0px 0px;
  height: 100vh;
}
</style>