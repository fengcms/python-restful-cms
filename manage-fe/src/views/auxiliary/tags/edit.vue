<template>
  <div>
    <main-topline :bread="['辅助管理', '关键词管理-/auxiliary/tags', '编辑详情']">
      <el-button type="info" @click="$router.go(-1)" icon="el-icon-arrow-left">返回</el-button>
      <el-button type="primary" icon="el-icon-check" @click="onSubmit()">保存关键词</el-button>
    </main-topline>
    <el-form
      v-loading="loading"
      label-width="100px"
      :model="dat"
      :rules="rules"
      ref="ref"
    >
      <el-form-item label="关键词：" prop="tag">
        <el-input v-model="dat.tag"></el-input>
      </el-form-item>
      <el-form-item label="点击量：" prop="hits">
        <el-input-number v-model="dat.hits" :min="0"></el-input-number>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">保存关键词</el-button>
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
      api: 'tags',
      id: this.$route.params.id,
      rules: rules('tag,contact,mobile,email,website,hits'),
      base: {
        dat: { tag: null, hits: 0, channel_id: 0},
        list_url: '/auxiliary/tags'
      }
    }
  }
}
</script>
