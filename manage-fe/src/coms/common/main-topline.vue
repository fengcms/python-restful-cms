<template>
  <div class="manage_main_topline">
    <div class="manage_main_topline_fixed">
      <!-- 按钮组 -->
      <div class="manage_main_topline_btns">
        <el-button-group>
          <slot></slot>
        </el-button-group>
      </div>
      <!-- 面包屑 -->
      <breadcrumb :bread="bread"></breadcrumb>
    </div>
  </div>
</template>

<script>
export default {
  name: 'main-topline',
  props: {
    bread: Array
  }
}
</script>
