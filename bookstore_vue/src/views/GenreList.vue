<template>
    <div>
    <div>
        <p class="title mb-6">
          Choose a genre
        </p>
    </div>
        <div
        v-for="genre in genreList"
        v-bind:key="genre.name">
        <div class="box">
            <router-link v-bind:to="genre.get_absolute_url" class="primary-button">{{genre.name}}</router-link>

        </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios'
export default {
  name: 'Genres',
  data(){
    return {
      genreList:[]
    }
  },
  components:{},

  mounted() {
    this.getGenreList()
  },
  methods: {
    async getGenreList() {
      await axios
        .get('/api/v1/genre-list')
        .then(response=>{
          this.genreList = response.data
        })
        .catch(error =>{
          console.log(error)
        })

    }
  }

}
</script>

