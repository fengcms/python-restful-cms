<template>
  <div class="manage_main_pagination">
    <el-pagination
      background
      layout="prev, pager, next"
      @current-change="change"
      :total="total">
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: 'pagination',
  props: {
    total: Number,
    change: {
      type: Function,
      default: () => {}
    }
  }
}
</script>
