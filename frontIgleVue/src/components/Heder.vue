<script setup>
import { RouterLink } from 'vue-router';

</script>

<template>
    <header class="container-fluid py-10 bg-indigo-500 px-20">
        <nav class="flex justify-between">

            <div>
                <RouterLink to="/" class="text-white font-bold uppercase">Public Home</RouterLink>
            </div>
            <div>
                <RouterLink to="/login" class="py-4 px-8 bg-pink-600 rounded-md text-white font-bold uppercase">Login</RouterLink>
            </div>

        </nav>

    </header>
</template>