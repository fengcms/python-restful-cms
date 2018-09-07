module.exports = {
  baseUrl: '/manage/',
  devServer: {
    proxy: {
      '/api/v1/be': {
        target: 'http://localhost:9000', // 你接口的域名
        secure: false,
        changeOrigin: false
      },
      '/api/v1/fe': {
        target: 'http://localhost:9000', // 你接口的域名
        secure: false,
        changeOrigin: false
      }
    }
  }
}
