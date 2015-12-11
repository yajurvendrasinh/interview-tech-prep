### Criticisms of Angular

- http://www.leanpanda.com/blog/2015/09/20/our-criticisms-of-angularjs/

####Dynamic Scoping

- Cannot reason about scope by reading source code
- scoping depends on state of program, leading to interesting shenanigans

####Dirty Checking and Performance

- Angular implements data-bindings, connecting fragments of the DOM to JS variables.
- Angular, not knowing which and how many variables have been changed, is forced to perform a dirty check of every binding on the page. If changes are present, associated change-listeners are triggered, which may themselves cause changes to the scope!
- Conclusion: limit data bindings present in application to 2000.
- This was a [conscious choice](http://stackoverflow.com/questions/9682092/angularjs-how-does-databinding-work/9693933#9693933) made by the Angular team.

####Dependency Injection

- Argues that Angular's third model of dependency injection is inferior to previous two models.

#### Complexity

- Argues that Angular has way too many different types of [service](https://docs.angularjs.org/guide/providers) objects. There are providers, values, factories, services, constants...

#### Server side rendering 

- Login of application lives in the HTML itself. By design it's not possible for an Angular application to work serverside.

