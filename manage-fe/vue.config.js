module.exports = {
  // baseUrl: '/manage/',
  devServer: {
    proxy: {
      '/api/v1/be': {
        target: 'http://0.0.0.0:9000', // 你接口的域名
        secure: false,
        changeOrigin: false
      },
      '/api/v1/fe': {
        target: 'http://0.0.0.0:9000', // 你接口的域名
        secure: false,
        changeOrigin: false
      }
    }
  }
}
