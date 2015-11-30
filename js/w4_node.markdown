### Node.js

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

####Pros

In the last 20 years, we've had a stateless-web based on the stateless request/response paradigm. With Node you can write web apps with real-time, two-way connections. Instead of just the client initiating communication, now the server can initiate communication!

- [Benefits of Using Javascript across the Stack](http://www.toptal.com/javascript/guide-to-full-stack-javascript-initjs)
- [Why the hell would you use Node.js](http://www.toptal.com/nodejs/why-the-hell-would-i-use-node-js)

####NPM, the Node Package Manager

- works like Ruby Gems
- [Understanding NPM](https://unpm.nodesource.com/)

####Examples of where you should use Node.js

- A real-time multi-user application (chat client).
- API on top of a DB.
- Concurrent data where your database could become a bottleneck.
- Data streaming (real time video encoding)
- Server-side proxy

####Where you should NOT use Node.js

- Server-side application with relational DB. Use Rails over Node.js + Express when it comes to relational data access.
- Heavy server-side computation processing. Node.js is single threaded and only uses 1 CPU core.




