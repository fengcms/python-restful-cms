<template>
  <div>
    <main-topline :bread="['辅助管理', '来源管理-/auxiliary/origin', '编辑详情']">
      <el-button type="info" @click="$router.go(-1)" icon="el-icon-arrow-left">返回</el-button>
      <el-button type="primary" icon="el-icon-check" @click="onSubmit()">保存来源</el-button>
    </main-topline>
    <el-form
      v-loading="loading"
      label-width="100px"
      :model="dat"
      :rules="rules"
      ref="ref"
    >
      <el-form-item label="来源名称：" prop="name">
        <el-input v-model="dat.name"></el-input>
      </el-form-item>
      <el-form-item label="联系人：" prop="contact">
        <el-input v-model="dat.contact"></el-input>
      </el-form-item>
      <el-form-item label="联系手机：" prop="mobile">
        <el-input v-model="dat.mobile" :maxlength="11"></el-input>
      </el-form-item>
      <el-form-item label="联系邮箱：" prop="email">
        <el-input v-model="dat.email"></el-input>
      </el-form-item>
      <el-form-item label="官方网站：" prop="website">
        <el-input v-model="dat.website"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">保存来源</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import rules from '@/tool/rules'
import mixinEdit from '@/mixin/edit.js'
export default {
  mixins: [mixinEdit],
  data () {
    return {
      api: 'origin',
      id: this.$route.params.id,
      rules: rules('name,contact,mobile,email,website,hits'),
      base: {
        dat: { name: null, contact: null, mobile: null, email: null, website: null},
        list_url: '/auxiliary/origin'
      }
    }
  }
}
</script>
