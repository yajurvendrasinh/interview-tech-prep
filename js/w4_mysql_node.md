### Getting Started with MySQL

- Starting: `mysql.server start`
- Stopping: `mysql.server stop`
- Root use: `mysql -u root`
- Loading in schema: `mysql -u root < server/schema.sql`
- Set root use pw: `mysqladmin -u root password YOUR_PASSWORD`

####Resetting Password

- [Article Resource](http://innovativethought.net/2007/05/17/resetting-your-forgotten-mysql-password/)
- Stop: `mysql.server stop`
- Safe restart and skip access tables: `mysqld_safe --skip-grant-tables`
- In another tab: `mysql mysql`
- `UPDATE user SET Password=PASSWORD('YOUR_PASSWORD') WHERE Host='localhost' AND User='root';`

####General Use

- `show databases;`
- `create database DB_NAME;`
- `use DB_NAME;`
- `show tables;`
- `drop database DB_NAME;`

####Create table

```
CREATE TABLE Persons
(
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
);
```

Or load a file:

```
mysql -u root -p DB_NAME < collection.sql
```

Insert into table

```
mysql> insert into Persons (PersonID, LastName, FirstName, Address, City)
    -> values (1, 'Soshnin', 'Polina', '550 Church St.', 'San Francisco');
```

Load SQL to insert:

```
mysql -u root album < insert.sql
```

Load CSV:

```
BULK
INSERT CSVTest
FROM 'c:\csvtest.txt'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
```

Exploring a table:

```
describe database_name.table_name;
select * from table_name limit 1;
```

#### Schema

- [SQL designer](http://ondras.zarovi.cz/sql/demo/)

Turning some JSON into a schema:

```
var data = {
  'results': [
      {
      "createdAt": "2015-12-01T18:53:52.413Z",
      "objectId": "F8baj0FytS",
      "roomname": "lobby",
      "text": "Where is Rachel!",
      "updatedAt": "2015-12-01T18:53:52.413Z",
      "username": "SuperMan"
    },
    {
      "createdAt": "2015-12-01T18:51:09.090Z",
      "objectId": "YxFS3622N7",
      "roomname": "NEWROOM",
      "text": "Batman",
      "updatedAt": "2015-12-01T18:51:09.090Z",
      "username": "fawn"
    },
    {
      "createdAt": "2015-12-01T04:02:57.076Z",
      "objectId": "3Wju8ywLZm",
      "roomname": "lobby",
      "text": "akjdhfkasd",
      "updatedAt": "2015-12-01T04:02:57.076Z",
      "username": "benji"
    }
  ]
};
```

- We have Rooms, Users, and Messages.
- Multiple users for one room.
- Multiple messages for one user.

![sql_schema](/img/sql_schema.jpg)

Loading in File

```
mysql -u root chatter_box < tables.sql
```

Creating Tables

```
CREATE TABLE message (
  id INTEGER,
  user_id INTEGER,
  text VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE user (
  id INTEGER,
  room_id INTEGER,
  username VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE room (
  id INTEGER,
  name VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  PRIMARY KEY (`id`)
);
```

Adding foreign keys

```
ALTER TABLE `message` ADD FOREIGN KEY (user_id) REFERENCES `user` (`id`);
ALTER TABLE `user` ADD FOREIGN KEY (room_id) REFERENCES `room` (`id`);
```

### Node.js and MySQL

- Install: `npm install mysql --save`
- ORM it up with sequelize: `npm install --save sequelize`




