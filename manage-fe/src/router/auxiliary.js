import AuthorList from '@/views/auxiliary/author/list.vue'
import AuthorEdit from '@/views/auxiliary/author/edit.vue'

export default [
  { path: 'author', component: AuthorList },
  { path: 'author/add', component: AuthorEdit },
  { path: 'author/edit/:id', component: AuthorEdit }
]
