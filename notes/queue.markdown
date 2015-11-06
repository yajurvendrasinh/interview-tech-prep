### Queues

Implementation

```
var Queue = function() {
  this.storage = {};
  this.count = 0;
  this.front = 0;
  this.back = 0;
};

Queue.prototype.enqueue = function(value) {
  this.storage[this.front+this.count] = value;
  this.back++;
  this.count++;
}

Queue.prototype.dequeue = function() {
  if (this.count === 0) {
    return null;
  }
  var result = this.storage[this.front];
  this.front++;
  this.count--;
  return result;
}

Queue.prototype.size = function() {
  return this.count;
}
```

Alternatively you can use a LinkedList to implement a Queue:

```
var Queue = function() {
  var queueInstance = LinkedList();
  queueInstance.count = 0;
  queueInstance.enqueue = queueMethods.enqueue;
  queueInstance.dequeue = queueMethods.dequeue;
  queueInstance.size = queueMethods.size;
  return queueInstance;
}

queueMethods = {
  enqueue : function(value) {
    this.addToTail(value);
    this.count++;
  },
  dequeue : function() {
    var result = this.removeHead();
    this.count--;
    return result;
  },
  size : function() {
    return this.count;
  }
}
```
