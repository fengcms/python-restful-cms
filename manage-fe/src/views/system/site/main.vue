<template>
  <div>
    <main-topline :bread="['系统管理', '系统设置']">
      <el-button type="primary" icon="el-icon-check" @click="onSubmit()">保存系统设置</el-button>
    </main-topline>
    <el-form
      label-width="100px"
      :model="dat"
      :rules="rules"
      ref="ref"
      v-loading="loading">
      <el-form-item label="网站名称" prop="name">
        <el-input v-model="dat.name"></el-input>
      </el-form-item>
      <el-form-item label="网站标题" prop="title">
        <el-input v-model="dat.title"></el-input>
      </el-form-item>
      <el-form-item label="网站关键词" prop="keywords">
        <el-input v-model="dat.keywords"></el-input>
      </el-form-item>
      <el-form-item label="网站描述" prop="description">
        <el-input type="textarea" autosize v-model="dat.description"></el-input>
      </el-form-item>
      <el-form-item label="网站LOGO" prop="logo">
        <el-input v-model="dat.logo"></el-input>
      </el-form-item>
      <el-form-item label="网站版权" prop="copyright">
        <el-input type="textarea" autosize v-model="dat.copyright"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data () {
    return {
      dat: {},
      rules: {
        name: [
          { required: true, message: '请输入网站名称', trigger: 'blur' },
          { max: 100, message: '网站名称过长', trigger: 'blur' }
        ],
        title: [
          { required: true, message: '请输入网站标题', trigger: 'blur' },
          { max: 200, message: '网站标题过长', trigger: 'blur' }
        ],
        keywords: [
          { required: true, message: '请输入网站关键词', trigger: 'blur' },
          { max: 255, message: '网站关键词过长', trigger: 'blur' }
        ],
        description: [
          { required: true, message: '请输入网站描述', trigger: 'blur' },
          { max: 255, message: '网站描述过长', trigger: 'blur' }
        ],
        logo: [
        ],
        copyright: [
          { required: true, message: '请输入版权', trigger: 'blur' },
          { max: 100, message: '网站名称过长', trigger: 'blur' }
        ]
      },
      base: {
        dat: {
          name: null,
          title: null,
          keywords: null,
          description: null,
          logo: null,
          copyright: null
        }
      },
      loading: true
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      this.loading = true
      this.$api.get('site', null, r => {
        this.loading = false
        this.dat = r.data
      }, e => {
        let { ...o } = this.base.dat
        this.dat = o
        this.loading = false
      })
    },
    onSubmit () {
      if (this.loading) {
        this.$message.warning('数据正在加载中，请稍后操作！')
        return
      }
      // 校验数据是否符合验证规则
      this.$refs['ref'].validate((valid) => {
        // 通过验证
        if (valid) {
          this.$api.post('site', this.dat, r => {
            this.$message.success('网站信息保存成功')
          })
        }
      })
    }
  }
}
</script>
