<template>
    <tr>
        <td><router-link :to="item.book.get_absolute_url">{{item.book.title}}</router-link></td>
        <td>{{item.book.isbn}}</td>
        <td>${{item.book.price}}</td>
        <td> {{item.quantity}}
            <a @click="decreaseQuant(item)">-</a>
            <a @click="increaseQuant(item)">+</a>
        </td>
        <td>${{getItemTotal(item).toFixed(2)}}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>
<script>

export default ({
    name: 'CartItem',
    props:{
        initialItem: Object
    },
    data(){
        return {
            item: this.initialItem
        }
    },
    methods:{
        getItemTotal(item) {
            return item.quantity * item.book.price
        },
        increaseQuant(item){
            item.quantity +=1
            this.updateCart()
        },
        decreaseQuant(item){
            item.quantity -=1
            if(item.quantity === 0){
                this.$emit('removeFromCart', item)
            }
            this.updateCart()
        },
        updateCart(){
            localStorage.setItem('cart',JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item){
            this.$emit('removeFromCart',item)
            this.updateCart()
        }
    }
})
</script>
