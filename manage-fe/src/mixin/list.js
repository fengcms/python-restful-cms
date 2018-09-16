export default {
  data () {
    return {
      dat: { list: [], total: 0 },
      search: {},
      select_id: []
    }
  },
  created () {
    this.restData()
  },
  methods: {
    getData () {
      this.$api.get(this.api, this.search, r => {
        this.dat = r.data
      })
    },
    restData () {
      let { ...o } = this.base.search
      this.search = o
      this.getData()
    },
    changePage (page) {
      this.search.page = page - 1
      this.getData()
    },
    selectData (val) {
      this.select_id = []
      for (let i of val) this.select_id.push(i.id)
    },
    batchDelete () {
      this.$api.delete(`${this.api}/${this.select_id.join(',')}`, null, r => {
        this.getData()
        this.$message.success('批量删除成功')
      })
    }
  }
}
