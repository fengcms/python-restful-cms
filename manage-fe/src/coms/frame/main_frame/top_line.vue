<template>
  <div class="manage_header_topline">
    <h1 class="manage_header_logo">
      <i class="el-icon-menu"></i> 新闻系统管理后台
    </h1>
    <div class="manage_header_link">
      <span @click="clearCache()">清除缓存</span>
      <router-link to="/system/change_password">修改密码</router-link>
      <span @click="logout()">退出登录</span>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    clearCache () {
      // 致敬 alert('缓存清除成功！')
      this.$message({
        message: '缓存清除成功',
        type: 'success',
        duration: 1000
      })
    },
    logout () {
      // 调用退出接口
      this.$api.get('logout', null, r => {
        this.$router.push('/login')
      }, e => {
        this.$message.error(e.data)
      })
    }
  }
}
</script>
