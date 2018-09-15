<template>
  <div class="manage_main_pagination">
    <el-pagination
      background
      layout="prev, pager, next"
      :total="total">
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: 'pagination',
  props: {
    total: Number
  }
}
</script>
