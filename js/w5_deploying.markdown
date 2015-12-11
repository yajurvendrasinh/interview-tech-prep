### Deployment

####[Gruntfiles](http://gruntjs.com/)

- Grunt [tutorial](https://24ways.org/2013/grunt-is-not-weird-and-hard/)
- `npm install -g grunt-cli`, `npm install grunt --save`
- Concatenating files: `npm install grunt-contrib-concat --save-dev`
- Minifying code: `npm install grunt-contrib-uglify --save-dev`
- Optimizing images: `npm install grunt-contrib-imagemin --save-dev`
- Add a `Gruntfile.js`
- Run `grunt`
- Grunt [tips and tricks](https://ponyfoo.com/articles/grunt-tips-and-tricks)
- [Usage](https://github.com/gruntjs/grunt-contrib-concat#usage-examples) examples

####Example

```
module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            // 2. Configuration for concatinating files goes here.
        }

    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['concat']);
};
```

####Watching files

- `npm install grunt-contrib-watch --save-dev`

```
watch: {
    scripts: {
        files: ['js/*.js'],
        tasks: ['concat', 'uglify'],
        options: {
            spawn: false,
        },
    } 
}
```

####Preprocessing (SASS)

- `npm install grunt-contrib-sass --save-dev`

```
sass: {
    dist: {
        options: {
            style: 'compressed'
        },
        files: {
            'css/build/global.css': 'css/global.scss'
        }
    } 
}
```

