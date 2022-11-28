<template>
    <div class="page-genre">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ genre.name }}</h2>
            </div>

            <div
            class="column is-3"
            v-for="book in genre.books"
            v-bind:key="book.id"
          >
            <div class="box">
              <figure class="image mb-4">
                <img :src="book.get_image">
              </figure>
              <h3 class="is-size-4">{{book.title}}</h3>
              <p class="is-size-6 has-text-grey">${{book.price}}</p>

              <router-link v-bind:to="book.get_absolute_url" class="primary-button">View Details</router-link>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Genre',
    data() {
        return {
            genre: {
                books: []
            }
        }
    },
    mounted() {
        this.getGenre()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'genre') {
                this.getGenre()
            }
        }
   },
    methods: {
        async getGenre() {
            const genreSlug = this.$route.params.genre_slug

            axios
                .get(`/api/v1/books/${genreSlug}/`)
                .then(response => {
                    this.genre = response.data
                })
                .catch(error =>{
                    console.log(error)

                    toast({
                        message:'Error. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right'
                    })
                })
        }
    }
}
</script>
