<template>
  <div>
    <main-topline :bread="['辅助管理', '作者管理-/auxiliary/author', '编辑详情']">
      <el-button type="info" @click="$router.go(-1)" icon="el-icon-arrow-left">返回</el-button>
      <el-button type="primary" icon="el-icon-check" @click="onSubmit()">保存作者</el-button>
    </main-topline>
    <el-form
      v-loading="loading"
      label-width="100px"
      :model="dat"
      :rules="rules"
      ref="ref"
    >
      <el-form-item label="作者姓名：" prop="name">
        <el-input v-model="dat.name"></el-input>
      </el-form-item>
      <el-form-item label="作者手机：" prop="mobile">
        <el-input v-model="dat.mobile" :maxlength="11"></el-input>
      </el-form-item>
      <el-form-item label="作者邮箱：" prop="email">
        <el-input v-model="dat.email"></el-input>
      </el-form-item>
      <el-form-item label="作者网站：" prop="website">
        <el-input v-model="dat.website"></el-input>
      </el-form-item>
      <el-form-item label="创作量：" prop="hits">
        <el-input-number v-model="dat.hits" :min="0"></el-input-number>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">保存作者</el-button>
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
      api: 'author',
      id: this.$route.params.id,
      rules: rules('name,mobile,email,website,hits'),
      base: {
        dat: { name: null, mobile: null, email: null, website: null, hits: 0 },
        list_url: '/auxiliary/author'
      }
    }
  }
}
</script>
