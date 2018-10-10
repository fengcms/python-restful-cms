<template>
  <div>
    <main-topline :bread="['系统管理', '管理员管理-/system/manages', '编辑详情']">
      <el-button type="info" @click="$router.go(-1)" icon="el-icon-arrow-left">返回</el-button>
      <el-button type="primary" icon="el-icon-check" @click="onSubmit()">保存管理员</el-button>
    </main-topline>
    <el-form
      v-loading="loading"
      label-width="120px"
      :model="dat"
      :rules="rules"
      ref="ref"
    >
      <el-form-item label="登录账户：" prop="account">
        <el-input v-model="dat.account"></el-input>
      </el-form-item>
      <template v-if="id">
        <el-form-item label="原密码：" prop="old_password">
          <el-input v-model="dat.old_password"></el-input>
        </el-form-item>
        <el-form-item label="新密码：" prop="new_password">
          <el-input v-model="dat.new_password"></el-input>
        </el-form-item>
        <el-form-item label="确认密码：" prop="re_password">
          <el-input v-model="dat.re_password"></el-input>
        </el-form-item>
      </template>
      <template v-else>
        <el-form-item label="登录密码：" prop="password">
          <el-input v-model="dat.password"></el-input>
        </el-form-item>
      </template>
      <el-form-item label="管理员姓名：" prop="name">
        <el-input v-model="dat.name"></el-input>
      </el-form-item>
      <el-form-item label="管理员手机：" prop="mobile">
        <el-input v-model="dat.mobile" :maxlength="11"></el-input>
      </el-form-item>
      <el-form-item label="管理员邮箱：" prop="email">
        <el-input v-model="dat.email"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">保存管理员</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import rules from '@/tool/rules'
import mixinEdit from '@/mixin/edit.js'
import Rsa from '@/tool/rsa'
export default {
  mixins: [mixinEdit],
  data () {
    let checkRePassword = (rule, value, callback) => {
      if (value !== this.dat.new_password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      api: 'manages',
      id: this.$route.params.id,
      rules: Object.assign(rules('account,password,old_password,new_password,name,mobile,email', '管理员'), {
        re_password: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          { validator: checkRePassword, trigger: 'blur' }
        ]
      }),
      base: {
        dat: { account: null, name: null, mobile: null, email: null },
        list_url: '/system/manages'
      }
    }
  },
  methods: {
    beforeSubmit () {
      let { ...o } = this.dat
      if (o.password) o.password = Rsa(o.password)
      if (o.old_password) o.old_password = Rsa(o.old_password)
      if (o.new_password) o.new_password = Rsa(o.new_password)
      delete o.re_password
      this.submitDat = o
    }
  }
}
</script>
