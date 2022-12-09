<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Payment and shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>
                <form
  id="app"
  @submit="checkForm"
  method="post"
>

  <p v-if="errors.length">
    <b>Please correct the following error(s):</b>
    <ul>
      <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
    </ul>
  </p>
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

                <hr>

                <div id="card-element" class="mb-5">
                    <div class="field">
                            <label>Card Number*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="card">
                            </div>
                    </div>
                    <div class="field">
                            <label>CVV*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="cvv">
                            </div>
                    </div>
                    <div class="field">
                            <label>Expiration Date*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="exp">
                            </div>
                    </div>
                </div>

                <hr>
                <p>
    <input
      type="submit"
      value="Pay"
      class="button is-primary"
    >
  </p>

</form>                
            </div>
        </div>
    </div>
</template>

<script>
import router from '@/router';

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            first_name: '',
            last_name: '',
            phone: '',
            email: '',
            state: '',
            city:'',
            address: '',
            zipcode: '',
            card:'',
            cvv:'',
            exp:'',
            errors: []
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        checkForm: function (e) {
            this.errors = [];
            if (this.first_name === '') {
                this.errors.push('Please enter a first name.')
                console.log("first name error")
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
            if (this.card === '') {
                this.errors.push('Please enter your credit cart number.')
            }
            if (this.cvv === '') {
                this.errors.push('Please enter your security code.')
            }
            if (this.exp === '') {
                this.errors.push('Please enter the expiration date of your card.')
            }
            else{
                router.push("/cart/success")
            }

      e.preventDefault();
    }  ,

    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.book.price * curVal.quantity
            }, 0)
        },
        cartTotalLength(){
            return this.cart.items.reduce((acc, curVal)=>{
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc, curVal)=>{
                return acc += curVal.book.price * curVal.quantity
            }, 0)
        },
    }
}
</script>