<template>
  <div>
    <main-topline :bread="['辅助管理', '作者管理-/auxiliary/author']">
      <el-button type="primary" @click="$router.push('author/add')" icon="el-icon-plus">添加作者</el-button>
      <el-button type="danger" @click="batchDelete()" icon="el-icon-delete">批量删除</el-button>
    </main-topline>
    <!-- 搜索区域 -->
    <main-search :search="search" :field="base.search_field" :goSearch="getData" :goRest="restData"></main-search>
    <!-- 列表区域 -->
    <div class="manage_main_list">
      <el-table :data="dat.list" style="width: 100%" @selection-change="selectData">
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column label="作者姓名" prop="name" width="160"></el-table-column>
        <el-table-column label="手机" prop="mobile" width="120"></el-table-column>
        <el-table-column label="邮箱" prop="email" width="180"></el-table-column>
        <el-table-column label="创作量" prop="hits" width="80" align="center"></el-table-column>
        <el-table-column label="个人网站" prop="website"></el-table-column>
        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" @click="$router.push(`${api}/edit/${scope.row.id}`)" icon="el-icon-edit">编辑</el-button>
            <el-button type="danger" size="mini" @click="deleteItem(scope.row)" icon="el-icon-delete">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
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
        search: { page: 0, 'name-like': '' },
        search_field: [{ field: 'name-like', label: '作者姓名' }]
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
      for (let i of val) {
        this.select_id.push(i.id)
      }
    },
    batchDelete () {
      this.$api.delete(`${this.api}/${this.select_id.join(',')}`, null, r => {
        this.getData()
        this.$message.success('批量删除成功')
      })
    },
    deleteItem (row) {
      this.$api.delete(`${this.api}/${row.id}`, null, r => {
        this.getData()
        this.$message.success('删除成功')
      })
    }
  }
}
</script>
