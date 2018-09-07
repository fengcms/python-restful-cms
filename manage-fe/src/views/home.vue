<template>
  <div class="manage_home">
    这里是管理后台首页内容
    <!-- <input type="file" @change="upload" ref="love">
    <img :src="img" alt="">
    <div :style="`width: 100px;height: 100px;background-image: url(${img});`"></div> -->
  </div>
</template>
<script>
export default {
  data () {
    return {
      img: '',
      img2: ''
    }
  },
  created () {
    this.$api.get('article', null, r => {
      console.log(r)
    })
  },
  methods: {
    upload () {
      this.img = this.getObjectURL(this.$refs.love.files[0])
      console.log(this.getObjectURL(this.$refs.love.files[0]))
    },
    getObjectURL (file) {
      var url = null
      if (window.createObjectURL !== undefined) {
        url = window.createObjectURL(file)
      } else if (window.URL !== undefined) {
        url = window.URL.createObjectURL(file)
      } else if (window.webkitURL !== undefined) {
        url = window.webkitURL.createObjectURL(file)
      }
      return url
    }
  }
}
</script>
