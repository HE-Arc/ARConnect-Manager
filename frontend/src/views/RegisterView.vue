<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { AuthService } from '@/domain/AuthService';

const router = useRouter();
const form = ref(null)

const username = ref(null);
const password = ref(null);
const passwordConfirmation = ref(null);

const register = async () => {
    if (!form.value.reportValidity()) return;
    const successful = await AuthService.register(
        username.value,
        password.value,
        passwordConfirmation.value
    );

    if (!successful) return;
    const token = await AuthService.login(username.value, password.value);

    if (token == null) return;
    router.push({ name: "home" })
};

</script>


<template>
    <div class="flex-container">
        <div class="card">
            <h1>ARConnect</h1>
            <form method="post" ref="form">
                <div class="form-row">
                    <label for="username">Pseudo :</label>
                    <input id="username" type="text" name="username"
                        v-model="username" required>
                </div>
                <div class="form-row">
                    <label for="password">Mot de passe :</label>
                    <input id="password" type="password" name="password" v-model="password" required></input>
                </div>

                <div class="form-row">
                    <label for="password-confirmation">Confirmation :</label>
                    <input id="password-confirmation" type="password" name="password-confirmation"
                        v-model="passwordConfirmation" required></input>
                </div>
            </form>
            <button class="btn-primary" @click="register">Créer un compte</button>
            <hr>
            <p>Déjà inscrit ? <router-link :to="{ name: 'login' }">Se connecter</router-link></p>
        </div>
    </div>
</template>

<style lang="scss" scoped>
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
}
</style>