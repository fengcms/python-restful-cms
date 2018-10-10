<template>
  <el-menu
    default-active="el-icon-tickets"
    :default-openeds="['el-icon-tickets']"
    :unique-opened="true"
    :router="true"
    background-color="#4A5159"
    text-color="#F2F6FC"
    active-text-color="#409EFF"
  >
    <el-submenu v-for="i in nav" :index="i.icon" :key="i.icon">
      <template slot="title">
        <i :class="i.icon"></i>
        <span>{{i.name}}</span>
      </template>
      <el-menu-item v-for="ii in i.children" :index="ii.url" :key="ii.url">
        {{ii.name}}
      </el-menu-item>
    </el-submenu>
  </el-menu>
</template>
<script>
export default {
  data () {
    return {
      nav: [
        {
          name: '文章管理',
          icon: 'el-icon-tickets',
          children: [
            {
              name: '文章列表',
              url: '/article'
            }, {
              name: '添加 html 文章',
              url: '/article/add'
            }, {
              name: '添加 markdown 文章',
              url: '/article/add-md'
            }, {
              name: '栏目管理',
              url: '/article/channel'
            }, {
              name: '回收站',
              url: '/article/trash'
            }
          ]
        }, {
          name: '辅助管理',
          icon: 'el-icon-edit',
          children: [
            {
              name: '作者管理',
              url: '/auxiliary/author'
            }, {
              name: '来源管理',
              url: '/auxiliary/origin'
            }, {
              name: '关键词管理',
              url: '/auxiliary/tags'
            }
          ]
        }, {
          name: '系统管理',
          icon: 'el-icon-setting',
          children: [
            {
              name: '系统设置',
              url: '/system/site'
            }, {
              name: '管理员管理',
              url: '/system/manages'
            }
          ]
        }
      ]
    }
  }
}
</script>
