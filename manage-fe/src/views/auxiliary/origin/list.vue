<template>
  <div>
    <main-topline :bread="['辅助管理', '来源管理-/auxiliary/origin']">
      <el-button type="primary" @click="$router.push('origin/add')" icon="el-icon-plus">添加来源</el-button>
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
      api: 'origin',
      base: {
        search: { page: 0, 'name-like': '', 'mobile': '' },
        search_field: [
          { field: 'name-like', label: '来源名称' },
          { field: 'contact-like', label: '联系人' },
          { field: 'mobile', label: '手机' }
        ],
        list_field: [
          { field: 'name', label: '来源名称', width: 180 },
          { field: 'contact', label: '联系人', width: 120 },
          { field: 'mobile', label: '手机', width: 120 },
          { field: 'email', label: '邮箱', width: 180 },
          { field: 'website', label: '来源网站' }
        ],
        list_control: ['edit', 'delete']
      }
    }
  }
}
</script>
<!-- name = Column(String(255), nullable=False)
contact = Column(String(255))
mobile = Column(String(255))
email = Column(String(255))
website = Column(String(255)) -->
