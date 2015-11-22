### Inheritance Patterns

- [Example](https://github.com/lazd/PseudoClass/blob/master/source/Class.js) of inheritance patterns in action from Larry Davis' Psuedoclass.
- Subclassing: inherit behavior from Parent class and add specialized functionality.
- Class inheritance is a tree structure here: you can only have one parent. Most languages allow only one.

### Polymorphism


### Functional subclassing

- In functional instantiation, there is no way to derive an orignal function once you create a property no the subclass that masks the original function name.

```
var Car = function(loc) {
  var obj = {loc: loc};
  obj.move = function() {
    obj.loc++;
  }
  return obj;
}

var Van = function(loc) {
  var obj = Car(loc);
  obj.grab = function() {..}
  return obj;
}
```

### Psuedoclassical subclassing

- [Object.create](http://dailyjs.com/2012/06/03/js101-object-create/)
- 
- Browsers are optimized for psuedoclassical instantiation.
- In psuedoclassical instantiation, we're talking about separate objects that through a language feature have an association (the prototype chain). Because of that, you have a reference in the original one.

```
var Car = function(loc) {
  this.loc = loc;
};

Car.prototype.move = function() {
  this.loc++;
}

var Van = function(loc) {
  Car.call(this, loc);
}

//this line of code sets up the prototype delegations 
//just like `new` does, but without running the 
//constructor in the process
//one side effect is we overwrite Van.prototype
//which means we lose the Van.prototype.constructor
reference
Van.prototype = Object.create(Car.prototype);

//here we put the Van.prototype.constructor
//back so we have access to it later
Van.prototype.constructor = Van;
Van.prototype.grab = function() {..}
```

- Object.create(obj.prototype) sets up prototype delegations just like `new` does, but without running the constructor in the process.



