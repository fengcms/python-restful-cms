import Vue from 'vue'

// 引入我们的自定义组件
import breadcrumb from './common/breadcrumb.vue'
import mainTopline from './common/main-topline.vue'
import mainSearch from './common/main-search.vue'
import mainList from './common/main-list.vue'
import pagination from './common/pagination.vue'

// 将我们的自定义组件构建成数组
const coms = [
  breadcrumb, mainTopline, mainSearch, mainList, pagination
]

// 循环注册组件
coms.forEach(com => {
  Vue.component(com.name, com)
})

// 导出组件
export default {
  breadcrumb,
  pagination,
  mainTopline,
  mainSearch,
  mainList
}
