var Encore = require('@symfony/webpack-encore');
var BundleTracker = require('webpack-bundle-tracker');

Encore
    .setOutputPath('build/')
    .setPublicPath('/static/')
    .addEntry('app', './assets/js/app.js')
    .enableSassLoader()
    .autoProvidejQuery()
    .enableSourceMaps(!Encore.isProduction())
    .cleanupOutputBeforeBuild()
    .enableBuildNotifications()
    .setManifestKeyPrefix('static/')
    .addPlugin(new BundleTracker({filename: './webpack-stats.json'}))
;

module.exports = Encore.getWebpackConfig();