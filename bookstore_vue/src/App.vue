<template>
  <div id="wrapper">
    <nav class="navbar is-primary">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Virtual Library</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/latest-books" class="navbar-item">Latest Books</router-link>
          <router-link to="/genre-list" class="navbar-item">All Books</router-link>
          <router-link to="/favorites" class="navbar-item">Favorites</router-link>

          <div class="navbar-item">
            <div class="buttons">
              
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/profile" class="button is-light">Profile</router-link>
              </template>
              <template v-else>
                <router-link to="/login" class="button is-light">Log In</router-link>
              </template>
              
              <router-link to="/cart" class="button is-danger">
                <span>Cart ({{cartTotalLength}})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  <section class="section">
    <router-view/>
  </section>
<!--  <footer class="footer">
    <p class="has-text-centered">Team 6 Bookstore</p>
  </footer> -->
  </div>
</template>

<script>
import axios from 'axios'
export default({
  data() {
    return{
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    }
    else{
      axios.defaults.headers.common['Authorization'] = " "
    }
  },
  mounted(){
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0 
      for (let i = 0; i < this.cart.items.length; i++){
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  }

})
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>