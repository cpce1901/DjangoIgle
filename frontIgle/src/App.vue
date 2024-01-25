<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/dash">Dash</RouterLink>
    <RouterLink to="/login">Login</RouterLink>
  </nav>

  <RouterView />
</template>

