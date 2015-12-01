### Function Binding

- Set the context on a function, so that when that function is executed, it's executed in the preset context.
- Way to permanently bind a function to a this binding. How do I guarantee that the function I invoke has the `this` binding.
- Bind can also be used to provide additional inputs.

How do we ensure callback function runs in correct context?

```
var alice = {teeth: 'dirty'};
var brushTeeth = function() {
  this.teeth = 'clean';
};

setTimeout(function() {brushTeeth.call(alice)}, 1000);
```

- this anonymous function makes reference to variables in its enclosing scope,
therefore we've created a closure
- when that function is evaluated, we do a lookup on the containing scope and it
evaluates correctly
- you cannot pass expressions into functions, you can also pass values
- if you see an expression passed into a function, it was first be evaluated before it can be passed in.

We want to create a function that achieves this behavior:

```
function() { afunc.call(context, arguments) }
```

The function bind returns a function.

```
var bind = function(func, context) {

  return function() {
    //cannot do func(), that is a free function invocation
    func.apply(context);

  };
}
```

Another way to reimplement bind with dot notation:

```
Function.prototype.bind = function(context) {
  var func = this;

  return function(){
    func.apply(context);

  }
};
```

### Full implementation supporting adding arguments

```
//inputs: function, context, args to prepend to arguments
//output: new function that has a preset context
//such that when the new function is executed
//it's executed in that context
var bind = function(func, context){
  var args = Array.prototype.slice.call(arguments, 2);
  
  return function(){
    var boundArgs = args.concat(Array.prototype.slice.call(arguments));
    return func.apply(context, boundArgs);
  }
};  

Function.prototype.bind = function(context) {
  var args = Array.prototype.slice.call(arguments, 1);
  var func = this; 
  return function(){
    var boundArgs = args.concat(Array.prototype.slice.call(arguments));
    return func.apply(context, boundArgs);
  }
};
```

#### Examples where `bind` is used

- Click handlers
- SetTimeOut
- Event binding with querySelectorAll





