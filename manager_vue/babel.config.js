module.exports = {
  presets: [
    '@vue/app'
  ],
  dev: {
    proxyTable: {
      '/api' : {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': 'api'
        }
      }
    }
  },
  cssSourceMap: false,
  build: {
    index: path.resolve(__dirname, '../templates/index.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, '../static'),
    assetsSubDirectory: 'build',
    assetsPublicPath: '/static/',
  }
}
