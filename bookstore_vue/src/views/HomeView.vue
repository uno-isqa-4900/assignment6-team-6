<template>
  <div class="home">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to the Virtual Library
        </p>
      </div>

      <div class="columns is-multiline">
      <div class="column is-12">
      </div>
      <div class="column is-3">
        <div class="box">
          <h3 class="is-size-4">Latest Books</h3>
          <p class="card-text">Browse most recent books</p>
          <p><a><router-link to="/latest-books">View Details &raquo;</router-link></a></p>
        </div>
      </div>
      <div class="column is-3">
        <div class="box">
          <h3 class="is-size-4">All Books</h3>
          <p class="card-text">List of all books</p>
          <p><a><router-link to="/genre-list">View Details &raquo;</router-link></a></p>
        </div>
      </div>

      <div class="column is-3">
        <div class="box">
          <h3 class="is-size-4">Favorites</h3>
          <p class="card-text">You can favorite books</p>
          <p><a><router-link to="/favorites">View Details &raquo;</router-link></a></p>        </div>
      </div>

      <div class="column is-3">
        <div class="box">
          <h3 class="is-size-4">Profile</h3>
          <p class="card-text">You can log in and out here</p>
          <p><a><router-link to="/profile">View Details &raquo;</router-link></a></p>        </div>
      </div>

      </div>
  </div>

</template>

<script>
import axios from 'axios'
export default {
  name: 'Home',
  data(){
    return {
      latestBooks:[]
    }
  },
  components:{},

  mounted() {
    this.getLatestBooks()
  },
  methods: {
    async getLatestBooks() {
      await axios
        .get('/api/v1/latest-books/')
        .then(response=>{
          this.latestBooks = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    }
  }

}
</script>
