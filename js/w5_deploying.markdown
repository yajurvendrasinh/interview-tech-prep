### Deployment

#### Heroku and Node.js setup

- [How Heroku Works](https://devcenter.heroku.com/articles/how-heroku-works)
- Setup: `heroku login`
- Prepare the app: `git clone`
- Deploy: `heroku create`, `git push heroku master`
- View logs: `heroku logs --tail`
- Define a Procfile. This is in the root of your application and explicitly declares what command(s) should be executed to start the app.

Here is declaring index.js as the web process to be executed. You can declare additional processes.

```
web: node index.js
```

- Check how many dynos are running: `heroku ps`
- Declare app dependecies in `package.json`, `npm install` to run locally
- Run application locally: `heroku local web`
- Propagate local changes: `git commit` `git push heroku master`
- Provision addons: `heroku addons:create papertrail` `heroku addons` ` heroku addons:open papertrail`
- Console: `heroku run node` `heroku run bash`
- Setting up [configuration vars](https://devcenter.heroku.com/articles/getting-started-with-nodejs#define-config-vars)
- Add db: `heroku addons:create heroku-postgresql:hobby-dev`
- Connect to remote db: `heroku pg:psql`

####[Gruntfiles](http://gruntjs.com/)

Goal:

- Run `grunt deploy` to build and host app locally
- Run `grunt deploy --prod` to push to Heroku

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

