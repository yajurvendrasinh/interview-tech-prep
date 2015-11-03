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
