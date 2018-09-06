module.exports = {
  devServer: {
    proxy: {
      '/api/v1/be': {
        target: 'http://localhost:3000', // 你接口的域名
        secure: false,
        changeOrigin: false
      }
    }
  }
}
