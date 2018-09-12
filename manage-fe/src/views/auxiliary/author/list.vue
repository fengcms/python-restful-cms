<template>
  <div>
    <div class="manage_main_topline">
      <div class="manage_main_topline_fixed">
        <!-- 按钮组 -->
        <div class="manage_main_topline_btns">
          <el-button-group>
            <el-button type="primary" icon="el-icon-arrow-left">返回</el-button>
            <el-button type="primary" icon="el-icon-delete">删除</el-button>
          </el-button-group>
        </div>
        <!-- 面包屑 -->
        <Breadcrumb :bread="['辅助管理', '作者管理-/auxiliary/author']"></Breadcrumb>
      </div>
    </div>
    <!-- 搜索区域 -->
    <div class="manage_main_search">
      <el-form size="small" :inline="true">
        <el-form-item label="姓名">
          <el-input></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary">查询</el-button>
        </el-form-item>
      </el-form>
    </div>
    <!-- 列表区域 -->
    <div class="manage_main_list">
      <el-table :data=[] style="width: 100%">
        <el-table-column label="姓名" width="180"></el-table-column>
        <el-table-column label="地址"></el-table-column>
      </el-table>
    </div>
    <!-- 分页区域 -->
    <Pagination :total="50"></Pagination>
  </div>
</template>
<script>
export default {
}
</script>
