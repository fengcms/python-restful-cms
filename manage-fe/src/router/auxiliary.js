import AuthorList from '@/views/auxiliary/author/list.vue'
import AuthorEdit from '@/views/auxiliary/author/edit.vue'

import OriginList from '@/views/auxiliary/origin/list.vue'
import OriginEdit from '@/views/auxiliary/origin/edit.vue'

export default [
  { path: 'author', component: AuthorList },
  { path: 'author/add', component: AuthorEdit },
  { path: 'author/edit/:id', component: AuthorEdit },
  { path: 'origin', component: OriginList },
  { path: 'origin/add', component: OriginEdit },
  { path: 'origin/edit/:id', component: OriginEdit }
]
