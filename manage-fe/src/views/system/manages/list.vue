<template>
  <div>
    <main-topline :bread="['辅助管理', '管理员管理-/system/manages']">
      <el-button type="primary" @click="$router.push('manages/add')" icon="el-icon-plus">添加管理员</el-button>
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
      api: 'manages',
      base: {
        search: { page: 0, 'name-like': '', 'mobile': '' },
        search_field: [
          { field: 'name-like', label: '作者姓名' },
          { field: 'mobile', label: '手机' }
        ],
        list_field: [
          { field: 'account', label: '登录账号', width: 160 },
          { field: 'name', label: '姓名', width: 160 },
          { field: 'mobile', label: '手机', width: 120 },
          { field: 'email', label: '邮箱' }
        ],
        list_control: ['edit', 'delete']
      }
    }
  }
}
</script>
