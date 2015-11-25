### Coffeescript notes

Coffeescript is a Javascript transpiler.

Install

``
npm install -g coffee-script
``

Sublime Package

```
Better Coffeescript
```

Transpile

```
[command] --flag [output directory] --flag --flag --flag [source directory]
coffee --output compiled --map --watch --compile ./
```

Specific Coffeescript shenanigans

ES5 | Coffeescript |
--- | --- |
Selection Sort | O(n) | 
Insertion Sort | O(n)| 
Merge Sort | O(n) |   
Quick Sort | O(n) |  
Binary Search | O(1) |


### ES6 notes

ES6 is a superset of ES5. Currently most JavaScript interpreters support ES5. ECMA refers to the European Computer Manufacturers Association.

Install and Transpile

```
npm install babel -g
babel originalFile.js --out-file compiledFile.js
```

If you've having Babel struggles

```
npm install babel-preset-es2015
babel --presets es2015 original.js --out-file output.js
```

Examples

- [`let` and `const` example](https://babeljs.io/repl/#?experimental=false&evaluate=true&loose=false&spec=false&code=let%20name%20%3D%20%22hello%22%3B%0Aconst%20numbers%20%3D%20%5B1%2C%202%2C%203%5D%3B%0A%0A%2F%2F%20numbers%20%3D%20%5B1%2C%202%5D%3B)
- [Arrow functions example](https://babeljs.io/repl/#?experimental=false&evaluate=true&loose=false&spec=false&code=const%20numbers%20%3D%20%5B1%2C%202%2C%203%2C%204%5D%3B%0A%0Anumbers.map(num%20%3D%3E%20num%20*%202)%3B%0A%2F%2F%20%5B2%2C%204%2C%206%2C%208%5D%0A%0Anumbers.reduce((sum%2C%20num)%20%3D%3E%20sum%20%2B%20num)%3B%0A%2F%2F%2010%0A%0Aconst%20reduceBySum%20%3D%20(sum%2C%20num)%20%3D%3E%20sum%20%2B%20num%3B%0A%0Aconsole.log(%0A%20%20numbers.reduce(reduceBySum)%0A))
- [Interpolation example](https://babeljs.io/repl/#?experimental=false&evaluate=true&loose=false&spec=false&code=%0A%0A%0Aconst%20name%20%3D%20%22Chris%22%3B%0Aconst%20answer%20%3D%2042%3B%0A%20%20%0Aconsole.log(%0A%20%20%60Hello%2C%20%24%7Bname%7D.%20The%20answer%20is%20%24%7Banswer%7D.%60%0A)%3B)
- [Default, Rest, Spread example](http://babeljs.io/repl/#?experimental=false&evaluate=true&loose=false&spec=false&code=%0Aconst%20greet%20%3D%20(name%2C%20greeting%20%3D%20%22Hey%22)%20%3D%3E%20%7B%0A%20%20console.log(%60%24%7Bgreeting%7D%2C%20%24%7Bname%7D%60)%3B%0A%7D%0Agreet(%22Chris%22)%3B%0Agreet(%22Chris%22%2C%20%22Hola%22)%3B%0A%0Aconst%20matchesAll%20%3D%20(pattern%2C%20...tests)%20%3D%3E%20%7B%0A%20%20console.log(pattern%2C%20tests)%3B%0A%7D%0A%0Aconsole.log(matchesAll(%2F%5Cd%2B%2F%2C%20%22231%22%2C%20%22324%22%2C%20%22999%22))%3B)
- [Destructuring example](https://babeljs.io/repl/#?experimental=false&evaluate=true&loose=false&spec=false&code=const%20getPoint%20%3D%20function()%20%7B%0A%20%20return%20%7B%20x%3A%201%2C%20y%3A%202%20%7D%0A%7D%0A%0Aconst%20%7Bx%2C%20y%7D%20%3D%20getPoint()%0A%0Aconsole.log(%60x%20is%20%24%7Bx%7D%2C%20y%20is%20%24%7By%7D!%60)%0A%0Aconst%20%5Ba%2C%20%2C%20b%5D%20%3D%20%5B1%2C2%2C3%5D%3B%0A%0A%0Aconst%20setPoint%20%3D%20(%7Bx%2C%20y%7D)%20%3D%3E%20%7B%0A%20%20console.log(x%2C%20y)%3B%0A%7D%0AsetPoint(%7Bx%3A%201%2C%20y%3A%202%7D)%3B)
- [Real world module example](https://github.com/rackt/redux/blob/adf8b9a3b14ecc65eb1c30bf7b5840aff2797934/examples/real-world/containers/RepoPage.js)


ES6 Conventions:

1. Use `const` by default.
2. Use `let` if you have to rebind a variable.
3. Use `var` to signal untouched legacy code.

### Resources

- Use semicolons in ES6 to avoid having to know [the Rules of ASI](http://bclary.com/2004/11/07/#a-7.9.1)
- [ES6 Coding Style Guide from Mozilla](https://github.com/mozilla/addon-sdk/wiki/Coding-style-guide)
- [Intro to modules](https://babeljs.io/docs/learn-es2015/#modules)
- [what is `strict` mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
- [what is `void 0`](http://stackoverflow.com/questions/7452341/what-does-void-0-mean)





