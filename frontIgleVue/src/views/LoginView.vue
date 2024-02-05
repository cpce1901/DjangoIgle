<script setup>
import axios from "axios"
import { inject } from "vue";
import { useRouter } from "vue-router";

const toast = inject('toast')
const router = useRouter()

const handlerSubmit = async (formData) => {
    try {
        const url = "http://localhost:8000/login/"
        const {data} = await axios.post(url, formData)
        localStorage.setItem('Token', data.token)
        router.push('dashboard')
            
    } catch (error) {
        toast.open({
            message: error.response.data.error,
            type: 'error',
        })
    }
}

</script>

<template>
    <div class="container mx-auto p-10">

        <FormKit 
            id="loginForm"
            type="form" 
            submit-label="Ingresar"       
            incomplete-message="Debes completar todos los campos..."
            @submit="handlerSubmit"
            >


            <FormKit type="email" label="Email" name="username" placeholder="Ingresa tu correo" validation="required|email"
                validation-visibility="blur" :validation-messages="{
                    required: 'Campo requerido',
                    email: 'El email no es valido'
                }" />



            <FormKit type="password" label="Password" name="password" placeholder="Ingresa tu contraseña"
                validation-visibility="blur" validation="required" :validation-messages="{
                    required: 'Campo requerido',
                }" />


        </FormKit>
    </div>
</template>



