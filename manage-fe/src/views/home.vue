<template>
  <div class="manage_home">
    <div class="manage_home_count">
      <div class="manage_home_count_item" v-for="i in count" :key="i.name">
        <em>{{i.total}}</em>
        <span>{{i.name}}</span>
      </div>
    </div>
    <div class="manage_home_list">
      <div class="manage_home_list_item">
        <h3>文章点击排行榜</h3>
        <ol>
          <li v-for="i in hotArticle" :key="i.title">{{i.title}}</li>
        </ol>
      </div>
      <div class="manage_home_list_item">
        <h3>作者创作排行榜</h3>
        <ol>
          <li v-for="i in hotAuthor" :key="i.name">{{i.name}}</li>
        </ol>
      </div>
      <div class="manage_home_list_item">
        <h3>热门关键词排行榜</h3>
        <ol>
          <li v-for="i in hotTags" :key="i.tag">{{i.tag}}</li>
        </ol>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      count: [{ name: '文章数量统计', total: 1000 }],
      hotArticle: [{ title: '文章标题' }],
      hotAuthor: [{ name: '作者姓名' }],
      hotTags: [{ tag: '关键词' }]
    }
  },
  created () {
  },
  methods: {
  }
}
</script>
