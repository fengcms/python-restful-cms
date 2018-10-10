export default {
  data () {
    return {
      dat: {},
      submitDat: {},
      loading: true
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      this.loading = true
      if (this.id) {
        this.$api.get(`${this.api}/${this.id}`, null, r => {
          this.dat = r.data
          this.loading = false
        })
      } else {
        let { ...o } = this.base.dat
        this.dat = o
        this.loading = false
      }
    },
    beforeSubmit () {
      let { ...o } = this.dat
      this.submitDat = o
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
          this.beforeSubmit()
          // 提交数据
          if (this.id) {
            // 编辑模式
            this.$api.put(`${this.api}/${this.id}`, this.submitDat, r => {
              this.$message.success('编辑成功')
              this.$router.push(this.base.list_url)
            })
          } else {
            // 添加模式
            this.$api.post(this.api, this.submitDat, r => {
              this.$message.success('添加成功')
              this.$router.push(this.base.list_url)
            })
          }
        }
      })
    }
  }
}
