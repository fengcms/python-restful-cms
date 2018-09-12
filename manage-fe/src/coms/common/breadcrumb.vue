<template>
  <div class="manage_main_topline_breadcrumb">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <template v-for="i in bread">
        <el-breadcrumb-item
          v-if="i.indexOf('-') === -1"
          :key="i"
        >
          {{i}}
        </el-breadcrumb-item>
        <el-breadcrumb-item
          v-else
          :key="i"
          :to="{ path: i.split('-')[1] }"
        >
          {{i.split('-')[0]}}
        </el-breadcrumb-item>
      </template>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  props: {
    bread: Array
  }
}
</script>
