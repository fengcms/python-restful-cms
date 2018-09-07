<template>
  <el-container class="manage_container">
    <el-header class="manage_header">
      <!-- 使用顶部通栏组件 -->
      <TopLine></TopLine>
    </el-header>
    <el-container>
      <el-aside class="manage_bar">这里将编写管理后台左侧导航栏</el-aside>
      <el-container class="manage_body">
        <div class="manage_main">
          <router-view />
        </div>
      </el-container>
    </el-container>
  </el-container>
</template>
<script>
// 引入顶部通栏组件
import TopLine from '@/coms/frame/main_frame/top_line.vue'
export default {
  // 注册组件
  components: { TopLine }
}
</script>
