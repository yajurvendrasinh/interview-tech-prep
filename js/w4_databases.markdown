### Databases

- Applications need to persist data. They need an organized collection of data.
- Database management system <=> Database <=> Set of data that sits on a DMS.

Considerations:

- Ability to Scale
- Relational Data

#### CAP Theorem

- Theorem states it's impossible for a distributed system to have all 3 properties.
- Consistency: all see same data at the same time
- Availability: each client can always read and write
- Partition Tolerance: systems works depsite network issues

#### ACID Consistency Model

Transactions uphold the following 4 properties in order to be processed reliably.

- Atomicity: all or nothing (start transaction or rollback). If one part of the transaction fails, all of the transaction fails and db is left unchanged. This makes databases more complicated, and potentially less performant.
- Consistency: only valid data is saved. All transactions must be valid according to predefined rules.
- Isolation: transactions do not affect each other
- Durability: written data will not be lost in the event of a failure.

#### BASE Consistency Model

Some DBs give up ACID requirements for immediate consistency, data freshness, and accuracy in order to scale and be resilient.

- Basic Availability: database works most of the time
- Soft-state: Stores don't have to be write-consistent, different replicas don't have to be mutually consistent.
- Eventual consistency: Store exhibit consistency later (ex. lazily at read time).

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
- Scale better vertically: throw hardware at it but same machine.

#### Not only SQL (NoSQL)

- Scale better horizontally: throw more machines at it.

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

- Object relational model
- DSL for manipulating data as Javascript's (or another languages) objects.


