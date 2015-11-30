### 306 view of web development

#### Web application

- Program that generates dynamic HTML responses to user requests
- You need this to login users, display user generated content, and allow different users to interact with the same data.

#### Database

- Where to store data that powers web application (user data)

Relational databases

- Use SQL: MySQL, MariaDB, PostgreSQL, Oracle, Microsoft SQL
- ORM: Object Relational Mapping. Converts regular code that is written in a programming language to the exact SQL commands that are needed to communicate with the database. A DSL for writing SQL queries. Language specific.
- Data has predefined structure

Non-relational databases

- MongoDB, CouchDB, RavenDB, Redis
- There is currently no standard for how data should be stored in a NoSQL database
- MongoDB is good for ad servers, bad for ecommerce sites
- ~10% of developers work with NoSQL DBs

#### Front end

- web browsers understand 3 languages: HTML, CSS, and JS
- HTML: structure documents in a way a browser understands
- CSS: style documents
- JS: manipulate the DOM without reloading page, runs inside web browser
- Vanilla JS: can modify content on a web page
- JavaScript + jQuery: does the same above, but in a much easier fashion.

Single Page Apps & JavaScript MV* Frameworks

- You want a complex interface without reloading the page
- Examples: Gmail, Twitter stream, FB newsfeed
- >95% of web applications out there are not single page applications.
- Examples of front end frameworks: BackboneJS, AngularJS, EmberJS, ReactJS
- Writing a complicated single page application without a framework helps you understand what problem(s) the above are trying to solve.

#### Back end

- Ruby works, good intro programming language as well
- Node.js works. It's easier to learn JS once you become competent in other programming languages first (anonymous functions, prototypal inheritance, callbacks).

#### Web frameworks

- Ruby on Rails: opinionated, there is a "correct" way to do something, convention over configuration
- ExpressJS: runs on NodeJS, not opinionated. That means it doesn't make your life easier if you do something "the right way".
- [NodeJS vs RoR](http://willnathan.com/nodejs-vs-ruby-on-rails)

### Conclusion

NodeJS is a great technology for a narrow band of problems.  100% JavaScript is generally overrated though.  Rails gives you more of a full package, and makes things easier to do once you learn it.

For most web applications the right tool for the job is Ruby on Rails paired with a SQL database with some JavaScript & jQuery on the front-end.  Using these tools will generally allow you to make progress on your application much quicker and be less error prone than the Full-Stack JavaScript approach.

### Teaching how to problem solve on your own

- Tutorial phase: domain specific knowledge. Once you can do the strokes, the broad tasks start to become more apparent. Overtime you'll recognize patterns and it'll come together.

####Most important skills in this phase:

- be extremely detail oriented.
- understanding how to debug error messages: learn how to read error message and understand what error you are resolving.
- Learning to code, you will never know everything you need to solve all of your problems.

####Next phase: inflection point

- You will phase off of using tutorials and start solving problems where someone else hasn’t lined up solutions for you. 
- During this phase you will be coding slower than the previous phase. Feelings of insecurity and doubt will emerge. 
- This phase is about learning procedural knowledge. This is about teaching yourself what you do not know.
- When you get here you will still be in the deep end, but you'll be comfortable knowing that's where you should be.

#### Mastery

- Web development inflection point: capable of building any database driven application.Also known as **Mastering CRUD**.
- Algorithm and Data Structure inflection point: mastered the programming fundamentals and in depth knowledge of solving complex coding challenges.

Once you pass these you will have mastered the ability to manipulate data and understand the performance implications of your design decisions.

**Most technical interviews will start with the assumption that you’ve passed the web development inflection point, since it’s easier to do, and focus their questions to see a candidate’s skill in algorithms and data structures.**

#### Holding the keys to the kingdom

- Understanding the complex algorithmic challenges that need to be built in the context of web applications.
- Domain specific knowledge no longer matters: everything has become "figure-out-able"
- Ask yourself: have I done that before? If you've used an API before, look back at your code and use it again. <--- I like this approach to trying to learn how to do a bunch of things that may later come in handy and referencing old code that you should have written well enough to read 6 months later.



