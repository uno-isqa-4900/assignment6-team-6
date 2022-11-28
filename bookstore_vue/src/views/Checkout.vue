<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Book</th>
                            <th>ISBN</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.book.id"
                        >
                            <td>{{ item.book.name }}</td>
                            <td>{{item.book.isbn}}</td>
                            <td>${{ item.book.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="3">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Payment and shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First Name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>

                        <div class="field">
                            <label>State*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="state">
                            </div>
                        </div>

                        <div class="field">
                            <label>Address*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Last Name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>City*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="city">
                            </div>
                        </div>

                        <div class="field">
                            <label>Zipcode*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>

                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>

                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            phone: '',
            email: '',
            state: '',
            city:'',
            address: '',
            zipcode: '',
            errors: []
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51H1HiuKBJV2qfWbD2gQe6aqanfw6Eyul5PO2KeOuSRlUMuaV4TxEtaQyzr9DbLITSZweL7XjK3p74swcGYrE2qEX00Hz7GmhMI')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })
            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.book.price
        },
        submitForm() {
            this.errors = []
            if (this.first_name === '') {
                this.errors.push('Please enter a first name.')
            }
            if (this.last_name === '') {
                this.errors.push('Please enter a last name.')
            }
            if (this.email === '') {
                this.errors.push('Please enter an email.')
            }
            if (this.phone === '') {
                this.errors.push('Please enter a phone number.')
            }
            if (this.address === '') {
                this.errors.push('Please enter an address.')
            }
            if (this.zipcode === '') {
                this.errors.push('Please enter a zipcode.')
            }
            if (this.state === '') {
                this.errors.push('Please enter a state.')
            }
            if (this.city === '') {
                this.errors.push('Please enter a city.')
            }
            if (!this.errors.length) {
                this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.errors.push('Error with Stripe. Try again')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
       async stripeTokenHandler(token) {
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    book: item.book.id,
                    quantity: item.quantity,
                    price: item.book.price * item.quantity
                }
                items.push(obj)
            }
            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'state': this.state,
                'city': this.city,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id
            }
            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })
             }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.book.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>