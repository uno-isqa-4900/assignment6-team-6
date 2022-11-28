<template>
    <div class="page-register">
        <div class="colums">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Register</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Re-enter Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="primary-button">Register</button>
                        </div>
                    </div>
                    <hr>
                    Already have an account? <router-link to="/log-in">Click here</router-link> to log in.
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default ({
    name: 'Register',
    data(){
        return {
            username:'',
            password:'',
            password2:'',
            errors:[]
        }
    },
    methods:{
        submitForm(){
            this.errors=[]
            if (this.username === ''){
                this.error.push('Please enter a username')
            }
            if (this.password === ''){
                this.error.push('Please enter a password')
            }
            if (this.password2 === ''){
                this.error.push('Passwords do not match')
            }

            if(!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios
                    .post("/api/v1/users/", formData)
                    .then(response =>{
                        toast({
                            message:'You have successfully created an account. Log in to continue.',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover:true,
                            duration:3000,
                            position: 'top-right',
                        })
                        this.$router.push('/login')
                    })
                    .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data){
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data))
                    }
                    else {
                        this.errors.push('Error. Please try again.')
                        console.log(JSON.stringify(error))
                    }
                })
            }
        }
    }
    

})
</script>
