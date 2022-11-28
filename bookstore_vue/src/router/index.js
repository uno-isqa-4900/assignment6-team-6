import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Book from '../views/Book.vue'
import Genre from '../views/Genre.vue'
import Cart from '../views/Cart.vue'
import GenreList from '../views/GenreList.vue'
import Register from '../views/Register.vue'
import LogIn from '../views/LogIn.vue'
import Profile from '../views/Profile.vue'
import store from '@/store'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'
import Favorites from '../views/Favorites.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/:genre_slug/:book_slug',
    name: 'Book',
    component: Book
  },
  {
    path: '/:genre_slug',
    name: 'Genre',
    component: Genre
  },
  {
    path: '/genre-list',
    name: 'GenreList',
    component: GenreList
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta:{
      requireLogin: true
    }
  },  
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/favorites',
    name: 'Favorites',
    component: Favorites
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
