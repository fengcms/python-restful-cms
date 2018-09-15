<template>
  <div>
    <div class="manage_main_topline">
      <div class="manage_main_topline_fixed">
        <!-- 按钮组 -->
        <div class="manage_main_topline_btns">
          <el-button-group>
            <el-button type="primary" @click="$router.push('author/add')" icon="el-icon-plus">添加作者</el-button>
            <el-button type="danger" icon="el-icon-delete">批量删除</el-button>
          </el-button-group>
        </div>
        <!-- 面包屑 -->
        <breadcrumb :bread="['辅助管理', '作者管理-/auxiliary/author']"></breadcrumb>
      </div>
    </div>
    <!-- 搜索区域 -->
    <div class="manage_main_search">
      <el-form size="small" :inline="true">
        <el-form-item label="作者姓名">
          <el-input></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary">查询</el-button>
        </el-form-item>
      </el-form>
    </div>
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
            <el-button type="primary" size="small" icon="el-icon-edit">编辑</el-button>
            <el-button type="danger" size="small" icon="el-icon-delete">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <!-- 分页区域 -->
    <!-- <pagination :total="dat.total"></pagination> -->
  </div>
</template>
<script>
export default {
  data () {
    return {
      dat: { list: [], total: 0 }
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      this.$api.get('author', null, r => {
        this.dat = r.data
        console.log(r)
      })
    },
    selectData (val) {
      console.log(val)
    }
  }
}
</script>
