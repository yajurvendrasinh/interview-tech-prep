### Two day project in Javascript

Ideas

- CSV -> JSON API using Express and Node.js
- Dynamically generate RESTful JSON API from static CSV

Problem:

Relational data is often represented in CSV format. CSVs are simple to create and move around and make them a good candidate for the default data format for bulk relational data. 

However, what if we want to expose our data as an API? JSON is the most popular data transport format. But many systems don't expose a JSON API.

This project uploads CSVs and dynamically generates a JSON API from that CSV.

Research:

- [JSON API mocking](https://github.com/typicode/json-server)
- [Tiny Node API with Express](https://github.com/scotch-io/node-api)
- [Read only API from CSV in Rails](https://github.com/davbre/mira)
- [Designing API in JS Express](http://www.smashingmagazine.com/2012/10/designing-javascript-apis-usability/)
- [REST API Express 4](https://scotch.io/tutorials/build-a-restful-api-using-node-and-express-4)
- [CSV to API](https://github.com/project-open-data/csv-to-api)
- [Javascript API design](http://webstandardssherpa.com/reviews/secrets-of-awesome-javascript-api-design/)

Tools:

- [Express](http://expressjs.com/)
- Node.js
- Postman for API testing

What it does:

- generate API from database
- display some API documentation in the UI
- fancier: upload CSV to database, generate API/docs from database afterwards

- API call -> google spread sheet. JSON to CSV converter.
- Google sheet -> JSON API

- turn your google sheet into an API?





