### Scopes and Closures

Really good resource is Kyle's book on [Scopes and Closures](https://github.com/getify/You-Dont-Know-JS/blob/master/scope%20&%20closures/README.md).

###What is a scope?

- Ability to store values in variables and later retrieve/modify them.
- This is important because it gives programs state.

###The rules of scope help answer these questions:

- Where do those variables "live"?
- Where are they stored?
- How are they accessed?

JavaScript is a compiled language. Steps compiler goes through:

1. tokenizing/lexing
2. Parsing (take stream of tokens and build an AST) (optimizing steps here)
3. code generation: take an AST and turn it into an executable

###Who needs to understand scope:

1. Engine: start to finish compilation and execution.
2. Compiler: parsing and code generation.
3. Collects and has a look-up list of declared identifiers and enforces how these are accessed to currently executing code.

###Dynamic generation: legacy behavior that is deprecated:

- eval()
- setTimeout()
- setInterval()

###Closure: a few definitions

- A Closure is a function is able to remember and access its lexical scope even when that function is executing outside its lexical scope.
- Closures are functions that refer to independent (free) variables. In other words, the function defined in the closure 'remembers' the environment in which it was created.

### Testing knowledge

- [Scope](http://madebyknight.com/javascript-scope/)

### Truthy and Falsy values

The following values are always falsy.

- false
- 0 (zero)
- "" (empty string)
- Null
- undefined
- NaN

Values that are truthy include ALL objects, functions, arrays. Even empty ones!

### Common idiom: casting truthy values to a boolean

```
  _.every = function(collection, iterator) {

    var predicate = iterator;
    if (predicate === undefined) {
      predicate = _.identity;
    }

    return _.reduce(collection, function(result, item) {
      return !!(predicate(item) && result);
    }, true);

  };
```

### `this` keyword

- Kyle's `this` articles [here](https://github.com/getify/You-Dont-Know-JS/blob/master/this%20&%20object%20prototypes/ch1.md) and [here](https://github.com/getify/You-Dont-Know-JS/blob/master/this%20&%20object%20prototypes/ch2.md) are incredibly helpful.

####What `this` is
- A special identifier that is automatically defined in the scope of every function.
- An elegant way of implictly passing along an object reference
- `this` is not an author-time binding but a runtime binding. It is contextual based on the conditions of the function's invocation. It has to do with how the function was called, not where it was called.
- `this` is a binding made for each function invocation, based entirely on its call-site (how the function is called).

####What `this` IS NOT

- It does not let a function get a reference to itself
- `this` DOES NOT refer to a function's lexical scope
- You CANNOT use a `this` reference to look something up in a lexical scope. It is not possible.

#### How do we find the call-site, how the function is called

- The call-site we care about is in the invocation before the currently executing function.
- Inspect the call-site and determine if one of the 4 rules apply.


**Rule #1**: standalone function invocation, `this` is global object

```
function foo() {
    console.log( this.a ); //resolves to global variable a
}

var a = 2;

foo(); // 2
```

- NOTE: If strict mode is in effect, the global object is not eligible for the default binding, so the this is instead set to undefined.

**Rule #2**: When there is a context object for a function reference, the implicit binding rule says that it's that object which should be used for the function call's this binding.

```
function foo() {
    console.log( this.a );
}

var obj = {
    a: 2,
    foo: foo
};

obj.foo(); // 2
```

#### `this`, call(), and apply()

- both invoke the function at that time
- myFunc.call(obj). This bounds `this` to obj when myFunc is called.

Only difference between call() and apply() is that call can look like this:

```
myFunc.call(obj,1,2,3,4) //this = obj
```

Whereas apply can only look like this: 

```
myFunc.apply(obj,[1,2,3,4])
```

### Additional JS I learned

```
//objects (objs, arrays, functions) are never falsy
//even empty ones
//this is a typical way of checking whether you 
//got an object
//Not a good way to check for primitives

var f = function(arg) {
    if (!arg) {
        console.log("no arg");
    } else {
        console.log("got an arg");
    }
}
```

```
//another thing to check is undefined.
//safest thing is to check length of the arguments 
//but undefined works most of the time

var f = function(arg) {
    if (arg === undefined) {
        console.log("no arg");
    } else {
        console.log("got an arg");
    }
}
```
