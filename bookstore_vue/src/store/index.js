import { createStore } from 'vuex'

export default createStore({
  state: {
    favorite: {
      items: [],
    },
    cart: {
      items: [],
    },
    isAuthenticated:false,
    token: '',
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if(localStorage.getItem('favorite')){
        state.cart = JSON.parse(localStorage.getItem('favorite'))
      }
      else {
        localStorage.setItem('favorite', JSON.stringify(state.favorite))
      }
    },
    addToFavorite(state, item){
      const exists = state.favorite.items.filter(i => i.book.id === item.book.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }
      else {
        state.favorite.items.push(item)
      }
      localStorage.setItem('favorite', JSON.stringify(state.favorite))
    },
    initializeStore(state) {
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }
      else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    addToCart(state, item){
      const exists = state.cart.items.filter(i => i.book.id === item.book.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }
      else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
  },
  actions: {
  },
  modules: {
  }
})

