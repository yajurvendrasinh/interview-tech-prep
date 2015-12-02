### Promises

- Motivation: Continuation passing style is harder to read and more procedural than it should be.

#### Flavors of async programming

- callback-based
- promises-based (also called futures)
- using promises in conjunction with generators or coroutines (`yield`, `async/await`)

####Promises Are

- representations of eventual values
- instead of declaring the order the program should use when executing, you define how each computation depends on each other
- a way to describe dependecies between expressions

####Three main pieces of functionality.

Step 1: Construct a representation of a value. The value must be provided at a later point in time.

```
createPromise();
```

Step 2: Put a value in a Promise, allowing the expressions that depend on that value to be computed.

```
fulfill(promise, value)
```

Step 3: Define a dependency between the expression and the value of the promise. It returns a new promise for the result of the expression, so new expressions can depend on that value.

```
depend(promise, expression)
```

