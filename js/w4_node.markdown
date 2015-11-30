### Node.js

The ability to write a full stack application in one language is valuable because you don't have to context switch. Additionally, some features of JS lend themselves very well to writing server side code.

####What is a server

- takes requests from clients, and depending on information that is sent, responds to that information.
- You can have the client and server on different machines, or same machine.
- There is an SSH server (if you have SSH enabled) that is running at all times

####What it is

- Javascript interpreter
- entire ecosystem has been built around it
- basically the v8 engine stripped from chrome
- Event-driven I/O server-side JavaScript environment based on V8
- allows you to run JS outside the browser
- It is NOT a web server. You have to write your own.
- Just a Javascript Runtime.
- Node is the REPL I wanted!
- Allows you to use JavaScript across the stack

####Why is it the new hotness? As opposed to Ruby.

- Classic buzzword response: it's asynchronous, implication being that Ruby/Python is not. But don't say that!
- It's not just because it's asynchronous. You can make Ruby/Python asynchronous. And yet JS/Node.js is still faster. It's because Node.js was built from the ground up to use asynchronous code. Ruby and Python at their base are synchronous. Node.js is written in the opposite perspective (default is written asynchronously. If you want to use synchronous code you have to go out of your way to do so). This means it can be highly performant.

####Installing Node

- You need NPM. Install using Brew: `brew install node`
- Install Node using `n`. `npm install -g n`, `n stable`
- Override Node installed by Brew: `n stable`
- Uninstall the version of node you installed with brew, `brew uninstall node`

#### Set up

- Upon initially cloning/setting up a repo, run `npm install --save`.
- Local installation: `npm install --save underscore`
- Global installation: `npm install -g nodemon`
- To start a server: `node server.js`
- Debugging: [Node inspector](https://github.com/node-inspector/node-inspector), `node-debug server.js`
- Running tests: `npm test`
- Refreshing changes without restarting server: [nodemon](https://github.com/remy/nodemon), `nodemon server.js`

####Pros

In the last 20 years, we've had a stateless-web based on the stateless request/response paradigm. With Node you can write web apps with real-time, two-way connections. Instead of just the client initiating communication, now the server can initiate communication!

- [Benefits of Using Javascript across the Stack](http://www.toptal.com/javascript/guide-to-full-stack-javascript-initjs)
- [Why the hell would you use Node.js](http://www.toptal.com/nodejs/why-the-hell-would-i-use-node-js)

####npm, which contains a node package manager

- [What does npm stand for](https://docs.npmjs.com/misc/faq#if-npm-is-an-acronym-why-is-it-never-capitalized)
- Works like Ruby Gems: you can build your own Modules and your own Node packages. However, with Ruby gems you can get stuck in dependency hell. In Ruby all libraries are installed globally. It doesn't get associated with your specific program. 
- NPM avoids dependency hell! It's the wild west of package managers.
- [Understanding NPM](https://unpm.nodesource.com/)
- NPM is commonly used for managing Node.js modules. It works on the front end when combined with [Browserify](http://browserify.org/).
- The ONLY time you want to install things **globally** with npm is to install command line tools. Otherwise install it locally.
- The difference between the NPM and [Bower](http://bower.io/)(created by Twitter) is that Bower is solely for the front-end. The biggest difference is that NPM does nested dependency tree (size heavy) while Bower requires a flat dependency tree (puts the burden of dependency resolution on the user).
- Some projects use both: they use Bower for front-end packages and NPM for developer tools like Yeoman, Grunt, Gulp, JSHint, CoffeeScript, etc.
- A nested dependency tree means that your dependencies can have its own dependencies which can have their own, and so on. This is really great on the server where you don't have to care much about space and latency.
- NPM aims for stability. Bower aims for minimal resource load. 

####Examples of where you should use Node.js

- A real-time multi-user application (chat client).
- API on top of a DB.
- Concurrent data where your database could become a bottleneck.
- Data streaming (real time video encoding)
- Server-side proxy

####Where you should NOT use Node.js

- Server-side application with relational DB. Use Rails over Node.js + Express when it comes to relational data access.
- Heavy server-side computation processing. Node.js is single threaded and only uses 1 CPU core.




