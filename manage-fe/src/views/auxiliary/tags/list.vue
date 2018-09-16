<template>
  <div>
    <main-topline :bread="['辅助管理', '关键词管理-/auxiliary/tags']">
      <el-button type="primary" @click="$router.push('tags/add')" icon="el-icon-plus">添加关键词</el-button>
      <el-button type="danger" @click="batchDelete()" icon="el-icon-delete">批量删除</el-button>
    </main-topline>
    <!-- 搜索区域 -->
    <main-search :search="search" :field="base.search_field" :goSearch="getData" :goRest="restData"></main-search>
    <!-- 列表区域 -->
    <main-list
      v-loading="loading"
      :api="api"
      :field="base.list_field"
      :data="dat.list"
      :getData="getData"
      :control="base.list_control"
      :selection="selectData">
    </main-list>
    <!-- 分页区域 -->
    <pagination :total="dat.total" :change="changePage"></pagination>
  </div>
</template>
<script>
import mixinList from '@/mixin/list.js'
export default {
  mixins: [mixinList],
  data () {
    return {
      api: 'tags',
      base: {
        search: { page: 0, 'tag-like': '' },
        search_field: [
          { field: 'tag-like', label: '关键词' },
        ],
        list_field: [
          { field: 'tag', label: '关键词名称' },
          { field: 'hits', label: '搜索量', width: 80, align: 'center' },
        ],
        list_control: ['edit', 'delete']
      }
    }
  }
}
</script>
