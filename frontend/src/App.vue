<script setup>
import NavBar from '@/components/NavBar.vue';
</script>

<template>
  <q-layout view="hHh Lpr fFf">
    <NavBar />
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style scoped></style>