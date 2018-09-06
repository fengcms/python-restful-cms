<template>
  <div class="manage_home">
    这里是管理后台首页内容
  </div>
</template>
<script>
export default {
  data () {
    return {}
  },
  created () {
    this.$api.get('loves', null, r => {
      console.log(r)
    })
  }
}
</script>
