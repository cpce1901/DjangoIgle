<script setup>
import router from '@/router/Router';
const handlerClick = () => {

    localStorage.removeItem('token');
    localStorage.removeItem('email');
    localStorage.removeItem('name');
    localStorage.removeItem('last_name');

    router.push('/login')
}

</script>

<template>
    <a 
    class="bg-red-400 px-6 py-3"
    @click="handlerClick"
    >Logout</a>
</template>