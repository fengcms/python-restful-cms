<template>
  <el-container class="manage_container">
    <el-header class="manage_header">
      <!-- 使用顶部通栏组件 -->
      <TopLine></TopLine>
    </el-header>
    <el-container>
      <el-aside class="manage_bar">
        <!-- 使用菜单栏组件 -->
        <Nav></Nav>
      </el-aside>
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
// 引用菜单栏组件
import Nav from '@/coms/frame/main_frame/nav.vue'
export default {
  // 注册组件
  components: { TopLine, Nav },
  created () {
    this.testLogin()
  },
  methods: {
    testLogin () {
      // 通过 site 接口判断是否登录
      this.$api.get('site', null, () => {})
    }
  }
}
</script>
