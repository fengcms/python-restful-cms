import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router/main.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Api from '@/tool/api'
import Coms from '@/coms/coms'

Vue.use(ElementUI)

Vue.prototype.$api = Api

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App, Coms)
}).$mount('#app')
