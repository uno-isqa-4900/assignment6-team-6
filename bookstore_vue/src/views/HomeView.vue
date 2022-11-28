<template>
  <div class="home">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to the Bookstore
        </p>
      </div>

      <div class="columns is-multiline">
      <div class="column is-12">
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
      
<!-- 
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Books</h2>
      </div>
    
      <div
        class="column is-3"
        v-for="book in latestBooks"
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

                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">My Lists</h5>
                        <p class="card-text">Track your progress here</p>
                        <p><a class="btn btn-primary" href="{% url 'mylists' %}"
                              role="button">View details &raquo;</a></p>
                    </div>
                </div>
            </div>-->
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
