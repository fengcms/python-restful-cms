<template>
  <div>
    <main-topline :bread="['辅助管理', '作者管理-/auxiliary/author']">
      <el-button type="primary" @click="$router.push('author/add')" icon="el-icon-plus">添加作者</el-button>
      <el-button type="danger" @click="batchDelete()" icon="el-icon-delete">批量删除</el-button>
    </main-topline>
    <!-- 搜索区域 -->
    <main-search :search="search" :field="base.search_field" :goSearch="getData" :goRest="restData"></main-search>
    <!-- 列表区域 -->
    <main-list
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
export default {
  data () {
    return {
      api: 'author',
      dat: { list: [], total: 0 },
      search: {},
      base: {
        search: { page: 0, 'name-like': '', 'mobile': '' },
        search_field: [
          { field: 'name-like', label: '作者姓名' },
          { field: 'mobile', label: '手机' }
        ],
        list_field: [
          { field: 'name', label: '作者姓名', width: 160 },
          { field: 'mobile', label: '手机', width: 120 },
          { field: 'email', label: '邮箱', width: 180 },
          { field: 'hits', label: '创作量', width: 80, align: 'center' },
          { field: 'website', label: '个人网站' }
        ],
        list_control: ['edit', 'delete']
      },
      select_id: []
    }
  },
  created () {
    this.restData()
  },
  methods: {
    getData () {
      this.$api.get(this.api, this.search, r => {
        this.dat = r.data
      })
    },
    restData () {
      let { ...o } = this.base.search
      this.search = o
      this.getData()
    },
    changePage (page) {
      this.search.page = page - 1
      this.getData()
    },
    selectData (val) {
      this.select_id = []
      for (let i of val) this.select_id.push(i.id)
    },
    batchDelete () {
      this.$api.delete(`${this.api}/${this.select_id.join(',')}`, null, r => {
        this.getData()
        this.$message.success('批量删除成功')
      })
    }
  }
}
</script>
