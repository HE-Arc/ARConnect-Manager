<script setup></script>

<template>
  <q-header reveal elevated class="bg-grey-10 text-white" height-hint="98">
    <q-toolbar>
      <q-icon name="coffee" size="xl"></q-icon>
      <q-toolbar-title>ARConnect</q-toolbar-title>
    </q-toolbar>

    <q-tabs align="left">
      <q-route-tab :to="{ name: 'home' }" label="Home" />
      <q-route-tab :to="{ name: 'beverages' }" label="Add beverage" />
      <q-route-tab :to="{ name: 'detailsAndStats' }" label="Details and stats" />
    </q-tabs>
  </q-header>
</template>

<style scoped></style>