<template>
  <div class="manage_main_search">
    <el-form size="small" :inline="true">
      <el-form-item v-for="i in field" :key="i.field" :label="i.label">
        <el-input v-model="search[i.field]"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="goSearch()">查询</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="goRest()">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'main-search',
  props: {
    field: Array,
    search: Object,
    goSearch: {
      type: Function,
      default: () => {}
    },
    goRest: {
      type: Function,
      default: () => {}
    }
  }
}
</script>
