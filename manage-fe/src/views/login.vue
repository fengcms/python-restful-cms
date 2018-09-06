<template>
  <div class="manage_login">
    这里是管理后台登录页面
  </div>
</template>
<script>
export default {
  data () {
    return {}
  },
  created () {
    this.$api.get('article', { page: 0, pagesize: 5 }, r => {
      console.log(r)
    })
  }
}
</script>
