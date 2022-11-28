<template>
    <div class="page-book">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="book.get_image">
                </figure>
                <h1 class="title">{{book.title}}</h1>
                <p>{{book.author}}</p>
                <p>{{book.summary}}</p>
            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
                <p><strong>Price: </strong>${{book.price}}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>
                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
                <div class ="control"> <a class="button is-light">Add to favorites</a></div>
            </div>
        </div>
    </div>
</template>

<script>
import { thisExpression } from '@babel/types'
import axios from 'axios'
import {toast} from 'bulma-toast'

export default ({
    name: 'Book',
    data() {
        return{
            book: {},
            quantity: 1
        }
    },
    mounted(){
        this.getBook()
    },
    methods:{
        async getBook(){
            const genre_slug = this.$route.params.genre_slug
            const book_slug = this.$route.params.book_slug

            await axios
                .get(`/api/v1/books/${genre_slug}/${book_slug}`)
                .then(response => {
                    this.book = response.data
                })
                .catch(error =>{
                    console.log(error)
                })
        },
        addToCart(){
        console.log('addToCart')
            if(isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }
            const item = {
                book: this.book,
                quantity: this.quantity
            }
            this.$store.commit('addToCart', item)

        }
    },
})
</script>