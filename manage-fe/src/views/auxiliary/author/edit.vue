<template>
  <div>
    <main-topline :bread="['辅助管理', '作者管理-/auxiliary/author', '编辑详情']">
      <el-button type="info" @click="$router.go(-1)" icon="el-icon-arrow-left">返回</el-button>
      <el-button type="primary" icon="el-icon-check" @click="onSubmit()">保存作者</el-button>
    </main-topline>
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
export default {
  data () {
    return {
      api: 'author',
      id: this.$route.params.id,
      dat: {},
      rules: rules('name,mobile,email,website,hits'),
      base: {
        dat: { name: null, mobile: null, email: null, website: null, hits: 0 }
      }
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      if (this.id) {
        this.$api.get(`${this.api}/${this.id}`, null, r => {
          this.dat = r.data
        })
      } else {
        let { ...o } = this.base.dat
        this.dat = o
      }
    },
    onSubmit () {
      // 校验数据是否符合验证规则
      this.$refs['ref'].validate((valid) => {
        // 通过验证
        if (valid) {
          // 提交数据
          if (this.id) {
            // 编辑模式
            this.$api.put(`${this.api}/${this.id}`, this.dat, r => {
              this.$message.success('编辑成功')
              this.$router.push('/auxiliary/author')
            })
          } else {
            // 添加模式
            this.$api.post(this.api, this.dat, r => {
              this.$message.success('添加成功')
              this.$router.push('/auxiliary/author')
            })
          }
        }
      })
    }
  }
}
</script>
