<template>
  <div class="manage_home">
    <div class="manage_home_count" v-loading="count_loading">
      <div class="manage_home_count_item" v-for="i in count" :key="i.type">
        <em>{{i.total}}</em>
        <span>{{i.type}}</span>
      </div>
    </div>
    <div class="manage_home_list">
      <div class="manage_home_list_item">
        <h3>文章点击排行榜</h3>
        <ol v-loading="hot_article_loading">
          <template v-if="!hot_article_loading && hot_article.length !== 0">
            <li v-for="i in hot_article" :key="i.id">{{i.title}}</li>
          </template>
          <template v-else>暂无文章</template>
        </ol>
      </div>
      <div class="manage_home_list_item">
        <h3>作者创作排行榜</h3>
        <ol v-loading="hot_author_loading">
          <template v-if="!hot_author_loading && hot_author.length !== 0">
            <li v-for="i in hot_author" :key="i.id">{{i.name}}</li>
          </template>
          <template v-else>暂无作者</template>
        </ol>
      </div>
      <div class="manage_home_list_item">
        <h3>热门关键词排行榜</h3>
        <ol v-loading="hot_tags_loading">
          <template v-if="!hot_tags_loading && hot_tags.length !== 0">
            <li v-for="i in hot_tags" :key="i.id">{{i.tag}}</li>
          </template>
          <template v-else>暂无作者</template>
        </ol>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      count: [],
      count_loading: true,
      hot_article: [],
      hot_article_loading: true,
      hot_author: [],
      hot_author_loading: true,
      hot_tags: [],
      hot_tags_loading: true
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      // 获取统计数据
      this.$api.get('count', null, r => {
        this.count = r.data
        this.count_loading = false
      })
      // 获取文章点击排行
      this.$api.get('article', { sort: 'hits' }, r => {
        this.hot_article = r.data.list
        this.hot_article_loading = false
      })
      // 获取作者创作排行榜
      this.$api.get('author', { sort: 'hits' }, r => {
        this.hot_author = r.data.list
        this.hot_author_loading = false
      })
      // 获取作者创作排行榜
      this.$api.get('tags', { sort: 'hits' }, r => {
        this.hot_tags = r.data.list
        this.hot_tags_loading = false
      })
    }
  }
}
</script>
