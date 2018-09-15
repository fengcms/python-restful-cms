<template>
  <div class="manage_main_list">
    <el-table :data="data" style="width: 100%" @selection-change="selection">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column
        v-for="i in field" :key="i.field"
        :label="i.label"
        :prop="i.field"
        :align="i.align ? i.align : 'left'"
        :width="i.width ? i.width : 'auto'"
      >
      </el-table-column>
      <el-table-column label="操作" width="180">
        <template slot-scope="scope">
          <el-button type="primary" size="mini"
            v-if="control.indexOf('edit') !== -1"
            @click="$router.push(`${api}/edit/${scope.row.id}`)"
            icon="el-icon-edit"
          >编辑</el-button>
          <el-button type="danger" size="mini"
            v-if="control.indexOf('delete') !== -1"
            @click="deleteItem(scope.row)"
            icon="el-icon-delete"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'main-list',
  props: {
    api: String,
    field: Array,
    data: Array,
    control: Array,
    selection: {
      type: Function,
      default: () => {}
    },
    getData: {
      type: Function,
      default: () => {}
    }
  },
  methods: {
    deleteItem (row) {
      this.$api.delete(`${this.api}/${row.id}`, null, r => {
        this.getData()
        this.$message.success('删除成功')
      })
    }
  }
}
</script>
