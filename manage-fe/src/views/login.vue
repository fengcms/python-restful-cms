<template>
  <section class="manage_login">
    <section class="manage_login_box">
      <header>
        <i class="el-icon-menu"></i> 新闻系统管理后台
      </header>
      <div class="manage_login_form">
        <el-form
          label-position="left"
          label-width="70px"
          :model="dat"
          :rules="rules"
          ref="dat"
        >
          <el-form-item label="账户：" prop="account">
            <el-input v-model="dat.account"></el-input>
          </el-form-item>
          <el-form-item label="密码：" prop="password">
            <el-input type="password" v-model="dat.password"></el-input>
          </el-form-item>
        </el-form>
        <el-button type="primary" @click="onSubmit()" class="block">登录</el-button>
      </div>
      <footer>
        Copyright &copy; 2018-2020, FungLeo, All Rights Reserved
      </footer>
    </section>
  </section>
</template>
<script>
// 引入 rsa 加密工具
import Rsa from '@/tool/rsa.js'
export default {
  data () {
    return {
      // 表单数据
      dat: {
        account: '',
        password: ''
      },
      // 验证规则数据
      rules: {
        account: [
          { required: true, message: '请输入管理员账户', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入管理员密码', trigger: 'blur' },
          { min: 6, max: 16, message: '密码长度为 6-16 之间', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onSubmit () {
      // 校验数据是否符合验证规则
      this.$refs['dat'].validate((valid) => {
        // 通过验证
        if (valid) {
          // 将密码加密
          let { account, password } = this.dat
          let postData = {
            account: account,
            password: Rsa(password)
          }
          // 提交数据
          this.$api.post('login', postData, r => {
            this.$router.push('/')
          }, e => {
            this.$message.error(e.data)
          })
        }
      })
    }
  }
}
</script>
