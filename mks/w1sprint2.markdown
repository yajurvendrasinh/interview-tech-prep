### Data Modeling and Classes

There are 4 different instantiation patterns in JavaScript. Here is a good [spreadsheet](http://www.ryanatkinson.io/javascript-instantiation-patterns/) outlining each. I'll walk through all of them.

###The functional pattern

- a simple "maker" pattern
- does not use `new`, `this`, or `prototype` chains
- Generate, assign properties, and define methods within a function.
- There are no methods delegated to fallback object.

```
var House = function(color) {
  
  //Generate Object
  var obj = {} 

  //Assign properties
  obj.color = color;
  obj.door = 'open';

  //Explicitly define methods
  obj.openDoor = function() {
  obj.dorr = 'open;'
  }

 //return Object
  return obj;
}

//instantiate
var house = House('red');
```

- **Pros**: very clear object construction.
- **Cons**: results in duplicate methods.

###The functional-shared pattern

- a simple "maker" pattern with shared methods
- does not use `new` or `prototype` chains

```
var House = function(color) {
  
  //Generate Object
  var obj = {} 

  //Assign properties
  obj.color = color;
  obj.door = 'open';

  //Explicitly define methods
  obj.openDoor = houseMethod;

 //return Object
  return obj;
}

var houseMethod = function() {
  this.door = 'open;'
  }

//instantiate
var house = House('red');
```

- **Pros**: Methods shared between objects
- **Cons**: Setting a pointer to a method is less efficient than delegating a fallback.

###The prototypal pattern

- uses `Object.create`
- does not use `new`

###The pseudoclassical pattern

- creates instances with the keyword new
- does not declare the instance explicitly
- does not return the instance explicitly




