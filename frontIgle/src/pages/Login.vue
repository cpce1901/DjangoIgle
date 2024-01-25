<script setup>

import router from '@/router/Router';
import { reactive } from 'vue'


const user = reactive({
    name: '',
    pass: ''
})

const handlerSubmit = async () => {
    const url = 'http://localhost:8000/login/'

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify({
                'username': user.name,
                'password': user.pass
            })
        })
        const data = await response.json()

        if (response.status == 200 || response.status == 201) {

            localStorage.setItem('token', JSON.stringify(data.token));
            localStorage.setItem('email', JSON.stringify(data.user.email));
            localStorage.setItem('name', JSON.stringify(data.user.name));
            localStorage.setItem('last_name', JSON.stringify(data.user.last_name));

            router.push('/')
        }

    } catch (error) {
        console.error(error)
    }

}

</script>

<template class="h-screen">
    <div class="container mx-auto p-10">

        <form method="post" class="flex flex-col" @submit.prevent="handlerSubmit">

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

            <input type="submit" value="Ingresar" class="px-4 py-2 bg-indigo-500 rounded-md text-white font-semibold">
        </form>

    </div>
</template>



