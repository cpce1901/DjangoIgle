<script setup>

import { reactive } from 'vue'

const user = reactive({
    name: '',
    pass: ''
})

const validar = () => {
    console.log("validando..")
}

</script>

<template class="h-screen">
    <div class="container mx-auto p-10">

        <form method="post" class="flex flex-col" @submit.prevent="validar">

            <div class="flex flex-col mb-5 gap-2">
                <label for="name">Email</label>
                <input type="email" id="name" v-model='user.name'
                    class="px-4 py-1 outline outline-1 outline-gray-200 rounded-sm text-gray-600">
            </div>

            <div class="flex flex-col mb-10 gap-2">
                <label for="pass">Contraseña</label>
                <input type="password" id="pass" v-model="user.pass"
                    class="px-4 py-1 outline outline-1 outline-gray-200 rounded-sm text-gray-600">

            </div>

            <input 
            type="submit" 
            value="Ingresar"
            class="px-4 py-2 bg-indigo-500 rounded-md text-white font-semibold">
        </form>

    </div>
</template>



