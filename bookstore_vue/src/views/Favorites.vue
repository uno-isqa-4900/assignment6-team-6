<template>
    <div>
        <div>
        <p class="title mb-6">
          Favorites
        </p>
    </div>
        <div class="columns is-multiline">

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="favoriteTotalLength">
                <thead>
                    <tr>
                        <th>Book</th>
                        <th>ISBN</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <FavoriteItem 
                        v-for="item in favorite.items"
                        v-bind:key="item.book.id"
                        v-bind:initialItem="item"
                        v-on:removeFromFavorite="removeFromFavorite"/>       
                </tbody>
            </table>
            <p v-else>No Favorites</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import FavoriteItem from '@/components/FavoriteItem.vue'

export default ({
    name: "Favorite",
    components: {
        FavoriteItem
    },
    data(){
        return{
            favorite:{
                items:[]
            }
        }
    },
    mounted() {
        this.favorite = this.$store.state.favorite
    },
    computed:{
        favoriteTotalLength(){
            return this.favorite.items.reduce((acc, curVal)=>{
                return acc += curVal.quantity
            }, 0)
        },
        favoriteTotalPrice(){
            return this.favorite.items.reduce((acc, curVal)=>{
                return acc += curVal.book.price * curVal.quantity
            }, 0)
        },
    
    },
    methods:{
        removeFromFavorite(item){
            this.favorite.items = this.favorite.items.filter(i=>i.book.id !== item.book.id)
        }
    }
})
</script>
