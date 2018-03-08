var Encore = require('@symfony/webpack-encore');

Encore
	.setOutputPath('static/build/')
	.setPublicPath('/static/build')
	.addEntry('app', './assets/js/app.js')
	.enableSassLoader()
	.autoProvidejQuery()
	.enableSourceMaps(!Encore.isProduction())
	.cleanupOutputBeforeBuild()
	.enableBuildNotifications()
	;

module.exports = Encore.getWebpackConfig();
