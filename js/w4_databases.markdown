### Databases

- Applications need to persist data. They need an organized collection of data.
- Database management system <=> Database <=> Set of data that sits on a DMS.

Considerations:

- Ability to Scale
- Relational Data

#### CAP

- Consistency
- Availability
- Partition Tolerance

#### ACID

- Atomicity
- Consistency
- Isolation
- Durability

#### CRUD

- Create
- Read
- Update
- Delete

#### Relational

- RDMS: relational database management systems
- Normalization: not repeating data in certain places
- "Structured Query Language": SQL
- Examples: Oracle, MySQl, Postgres
- SQL ds tend to be harder to use than NoSQL dbs.

#### Getting Started with MySQL

- `mysql.server start`, `mysql -u root`
- Loading in schema: `mysql -u root < server/schema.sql`

#### Not only SQL (NoSQL)

Document Stores

- Examples: MongoDB, CouchDB
- Fast lookups by one index.
- Tree/List like data
- Bad for relational data
- Store arbitrary documents as JSON. Schemaless and do not support complex relationships, but support fast read/write of non-relational data.

Key-Value Stores

- Examples: Redis
- Can handle massive scalability, ie. distributed hash tables.
- Good for simple associative data.
- Distributed data.
- Bad for complex relational data.
- Think of a single specialized key/value table.
- Can support the value as a data structure (hash, list, array)
- Read is very fast and very cacheable

Graph Databases

- Good for highly relational data, complex relationships
- Bad for non-relational data, tree/list structures
- Example: Neo4j
- Large graph. Edges represent relationships.

memcached

- caching results of database reads in memory
- access in RAM/memory > disk


#### ORM

