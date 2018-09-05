<template>
  <el-container class="manage_container">
    <el-header class="manage_header">这里将编写管理后台头部通栏</el-header>
    <el-container>
      <el-aside class="manage_bar">这里将编写管理后台左侧导航栏</el-aside>
      <el-container class="manage_body">
        <div class="manage_main">
          <router-view />
        </div>
      </el-container>
    </el-container>
  </el-container>
</template>
