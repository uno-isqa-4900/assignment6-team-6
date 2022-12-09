<template>
    <tr>
        <td><router-link :to="item.book.get_absolute_url">{{item.book.title}}</router-link></td>
        <td>{{item.book.isbn}}</td>
        <td><button class="delete" @click="removeFromFavorite(item)"></button></td>
    </tr>
</template>
<script>

export default ({
    name: 'FavoriteItem',
    props:{
        initialItem: Object
    },
    data(){
        return {
            item: this.initialItem
        }
    },
    methods:{
        updateFavorite(){
            localStorage.setItem('favorite',JSON.stringify(this.$store.state.favorite))
        },
        removeFromFavorite(item){
            this.$emit('removeFromFavorite',item)
            this.updateFavorite()
        }
    }
})
</script>
