import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home.vue'
import Login from '@/views/login.vue'
import MainFrame from '@/frame/main_frame.vue'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/login', component: Login },
    {
      path: '/',
      component: MainFrame,
      children: [
        { path: '', component: Home }
      ]
    }
  ]
})