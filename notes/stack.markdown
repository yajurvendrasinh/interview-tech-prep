### Stacks

Implementation

```
var Stack = function() {
  this.storage = {};
  this.count = 0;
};

Stack.prototype.push = function(value) {
  this.storage[this.count] = value;
  this.count++;
};

Stack.prototype.pop = function(value) {
  if (this.count === 0) {
    return null;
  }
  var pop = this.storage[this.count-1];
  delete this.storage[this.count];
  this.count--;
  return pop;
};

Stack.prototype.size = function() {
  return this.count;
};
```

Alternatively you can use a LinkedList to implement a Stack:

```
var Stack = function() {
  var stackInstance = LinkedList();
  stackInstance.count = 0;
  stackInstance.push = stackMethods.push;
  stackInstance.pop = stackMethods.pop;
  stackInstance.size = stackMethods.size;
  return stackInstance;
}

stackMethods = {
  push : function(value) {
    this.addToTail(value);
    this.count++;
  },
  pop : function() {
    //removeTail
    

  },
  size : function() {
    return this.size;
  }
}
```
