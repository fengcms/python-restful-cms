<template>
  <section class="manage_login">
    <section class="manage_login_box">
      <header>
        <i class="el-icon-menu"></i> 新闻系统管理后台
      </header>
      <div class="manage_login_form">
        <el-form label-position="left" label-width="55px">
          <el-form-item label="账户：">
            <el-input v-model="dat.account"></el-input>
          </el-form-item>
          <el-form-item label="密码：">
            <el-input v-model="dat.password"></el-input>
          </el-form-item>
        </el-form>
        <el-button type="primary" class="block">登录</el-button>
      </div>
      <footer>
        Copyright &copy; 2018-2020, FungLeo, All Rights Reserved
      </footer>
    </section>
  </section>
</template>
<script>
export default {
  data () {
    return {
      dat: {
        account: '',
        password: ''
      }
    }
  },
  created () {
    // this.$api.get('article', { page: 0, pagesize: 5 }, r => {
    //   console.log(r)
    // })
  }
}
</script>
