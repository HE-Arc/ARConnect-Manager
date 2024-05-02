<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { AuthService } from '@/domain/AuthService';

const router = useRouter();
const form = ref(null)

const username = ref(null)
const password = ref(null)
const errorMessage = ref(null)

const login = () => {
    if (!form.value.reportValidity()) return;
    AuthService.login(
        username.value,
        password.value,
    ).then((token) => {
        router.push({ name: "home" })
    }).catch(error => {
        errorMessage.value = "Nom d'utilisateur ou mot de passe incorrect"; // Définition du message d'erreur
    });
};

</script>


<template>
    <div class="flex-container">
        <div class="card">
            <h1>ARConnect</h1>
            <form method="post" ref="form">
                <div class="form-row">
                    <label for="username">Pseudo :</label>
                    <input id="username" type="text" name="username" placeholder="john.doe@example.com"
                        v-model="username" required>
                </div>
                <div class="form-row">
                    <label for="password">Mot de passe :</label>
                    <input id="password" type="password" name="password" v-model="password" required></input>
                </div>
            </form>
            <button class="btn-primary" @click="login">Connexion</button>
            <hr>
            <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
            <p>Pas de compte ? <router-link :to="{ name: 'register' }">S'inscrire</router-link></p>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/breakpoints";
@import "@/assets/styles/colors";

.flex-container {
    align-items: center;
    justify-content: center;
    height: 60%;

    .card {
        padding: 32px;
        display: flex;
        flex-direction: column;
        gap: 16px;

        hr {
            width: 100%
        }

        button {
            width: fit-content;
            align-self: flex-end;
        }

        p {

            align-self: center;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 16px;


            .form-row {
                display: flex;
                gap: 16px;

                input,
                label {
                    flex: 1
                }
            }
        }
    }
    .error-message {
        background-color: $primary;
        color: $on-primary;
        text-align: center;
        padding: 12px 16px;
        border-radius: 8px;
    }
}
</style>