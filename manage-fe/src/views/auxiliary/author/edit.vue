<template>
  <div>
    <div class="manage_main_topline">
      <div class="manage_main_topline_fixed">
        <!-- 按钮组 -->
        <div class="manage_main_topline_btns">
          <el-button-group>
            <el-button type="info" @click="$router.go(-1)" icon="el-icon-arrow-left">返回</el-button>
            <el-button type="primary" icon="el-icon-check" @click="onSubmit()">保存作者</el-button>
          </el-button-group>
        </div>
        <!-- 面包屑 -->
        <breadcrumb :bread="['辅助管理', '作者管理-/auxiliary/author', '编辑作者']"></breadcrumb>
      </div>
    </div>
    <el-form
      label-width="100px"
      :model="dat"
      :rules="rules"
      ref="ref"
    >
      <el-form-item label="作者姓名：" prop="name">
        <el-input v-model="dat.name"></el-input>
      </el-form-item>
      <el-form-item label="作者手机：" prop="mobile">
        <el-input v-model="dat.mobile"></el-input>
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
export default {
  data () {
    return {
      dat: { name: null, mobile: null, email: null, website: null, hits: 0 },
      rules: rules('name,mobile,email,website,hits')
    }
  },
  methods: {
    onSubmit () {
      // 校验数据是否符合验证规则
      this.$refs['ref'].validate((valid) => {
        // 通过验证
        if (valid) {
          // 提交数据
          this.$api.post('author', this.dat, r => {
            this.$message.success('添加成功')
            this.$route.push('../')
          }, e => {
            this.$message.error(e.data)
          })
        }
      })
    }
  }
}
</script>
