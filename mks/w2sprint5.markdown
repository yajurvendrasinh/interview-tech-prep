### Intro to Client and Server

- [Postman](https://www.getpostman.com/docs) is a great tool for playing around with APIs.

### HTTP requests

- **GET** request: ask for data from server. Client expects to receive data in a **response body** from server.
- **POST** request: change data on server. Server expects to receive data in a **request** body from client.
- **content-type** header informs the client or server how to interpret the request body.

### Status Codes

- 200: Okay
- 400: Client error
- 500: server error

### Client

- Instance of client/server interaction
- Interface (mobile is another client interface)

### REST

- Representational State Transfer.
- It's a stateless, client-server, cacheable protocol.
- You can interact with a server in a lot of different ways.
- Different standards have come and gone (ex. SOAP).
- Right now most folks use REST (a contract for interacting with a web server.)
- The way you interact with a web resource demonstrates the intent you want to have with that resource.
- GET is the most common action (fetch data from server).
- Standardized way everyone has agreed upon to interact with a server in a particular way.
- ex. GET (fetching), POST (creating), PUT (updating), DELETE

### API Keys

- authenticate you.

### Package Managers

- NPM: backend dependencies
- Bower: frontend dependencies

### The JavaScript Event Loop

- [Blog post on event loop](http://blog.carbonfive.com/2013/10/27/the-javascript-event-loop-explained/)

- Java, Ruby, Python have a request/reponse model.
- JavaScript's event driven interaction model is a concurrency model.
- Server-side applications typically are synchronous and linear in following requests and responses.
- When working with user interfaces where there is non-blocking I/O ("mousedown", "click" can be triggered any time), you need a different kind of model.
- The event loop allows us to decouple the caller from the response. This means JS lets you do other things while waiting for your async request to get a response.

### Web workers

- web workers have a copy of what your main thread has (a separate message queue, event loop, and memory space) and they can handle expensive operations which frees the main thread to be able to do other things.

![web-workers](/img/web-workers.png)



