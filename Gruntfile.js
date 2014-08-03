module.exports = function(grunt) {
	var port = grunt.option('port') || 8000;

	grunt.initConfig({
		connect: {
			server: {
				options: {
					port: port,
					base: '.',
					keepalive: true
				}
			}
		}

	});

	// Dependencies
	grunt.loadNpmTasks('grunt-contrib-connect');

	// Default task
	grunt.registerTask('default', ['serve']);

	// Serve presentation locally
	grunt.registerTask('serve', ['connect']);
};
