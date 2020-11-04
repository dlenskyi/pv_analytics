const BundleTracker = require("webpack-bundle-tracker")
const path = require('path')

module.exports = {
  publicPath: '/static/sections_dist/',
  outputDir: '../pv_analytics/static/sections_dist/',
  pages: {
    admin: {
      // entry for the page
      entry: 'src-admin/main.js',
      title: 'user',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      // chunks: ['chunk-vendors', 'chunk-common', 'index']
    },
    anonymous: {
      // entry for the page
      entry: 'src-anonymous/main.js',
      title: 'anonymous',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      // chunks: ['chunk-vendors', 'chunk-common', 'index']
    },
  },

  chainWebpack: config => {

    if (process.env.VUE_APP_SERVER_TYPE === 'DEV') {
      config.optimization
        .splitChunks(false)
    }

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

    config.resolve.alias
      .set('__STATIC__', 'static')
      .set('@base', path.resolve(__dirname, './src-base/'))
      .set('@anonymous', path.resolve(__dirname, './src-anonymous/'))
      .set('@admin', path.resolve(__dirname, './src-admin/'))

    config.devServer
      .public('http://0.0.0.0:8000')
      .host('0.0.0.0')
      .port(8080)
      .hotOnly(true)
      .watchOptions({poll: 1000})
      .https(false)
      .headers({
        'Access-Control-Allow-Origin': ['*']
      })
  }
}
