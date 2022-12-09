<template>
    <div class="home">
        <div>
        <p class="title mb-6">
          Latest Books
        </p>
    </div>

      <div class="columns is-multiline">   
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
