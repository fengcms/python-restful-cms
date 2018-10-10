import SiteMain from '@/views/system/site/main.vue'
import ManagesList from '@/views/system/manages/list.vue'
import ManagesEdit from '@/views/system/manages/edit.vue'

export default [
  { path: 'site', component: SiteMain },
  { path: 'manages', component: ManagesList },
  { path: 'manages/add', component: ManagesEdit },
  { path: 'manages/edit/:id', component: ManagesEdit }
]
