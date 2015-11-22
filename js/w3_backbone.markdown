## Backbone

### Prerequisites

Familiarity with JavaScript, including:

- Closures.
- How the keyword `this` works.
- Prototypical inheritance.
- Psuedoclassical classing.

Comfortable with [Underscore.js](http://underscorejs.org/). Especially its method signatures on collections.

Comfortable with jQuery, Ajax, HTML, CSS. See below for an example.

### Intro

You are a budding web developer. You know how to wield jQuery, Ajax calls, HTML, CSS, and you understand the ins and outs of the major parts of the JavaScript language. What are you missing out on?

Well, the great thing about jQuery is that you can do a lot in a few lines of code. The following code:

- Listens for page events
- Listens for user events
- Listens for network IO
- Parses GET response
- Does HTML templating

```
$(document).ready(function() {
    $('#new-status form').submit(function(e) {
        e.preventDefault();

        $.ajax({
            url: '/status',
            type: 'POST',
            dataType: 'json',
            data: { text: $('#new-status').find('textarea').val() },
            success: function(data) {
                $('#statuses').append('<li>' + data.text + '</li>');
                $('#new-status').find('textarea').val('');
            }
        });
    });
});
```
What are the problems with the above code? 

- Well, in its current state it's nearly impossible to test.
- If we followed the single responsibility principle, then it would make it easier to test and reuse. Currently it doesn't do that.
- We want to decouple the DOM and Ajax.

### Goals of Backbone

- Strive towards separation of concerns, single responsibility, and the ability to reason in isolation.

### Basics

Model

- `Backbone.Model`
- property access on models via getters and setters

Collection

- `Backbone.Collection`
- Array-like model
- lacks getters and setters

View (Presenter)

- `Backbone.View`
- projection of model or collection
- a Glorified DOM node
- model can have 0 to many views
- handles user input (there's no controller)

Subclassing

- extend();
- extend's params hash has: initialize property, defaults property, and others

Special Input Parameters

- Defining a Collection: model
- Defining a View: events, render, template
- Instantiating View: model, el, $el

### Resources

- [Backbone, the Primer](https://github.com/jashkenas/backbone/wiki/Backbone,-The-Primer)
- [Step by Step jQuery to Backbone](https://github.com/kjbekkelund/writings/blob/master/published/understanding-backbone.md/)
- [The BackboneJS way of thinking](http://learn.eastros.com/2013/04/20/the-backbonejs-way-of-thinking/)
- [Book: Developing Backbone Applications](http://addyosmani.github.io/backbone-fundamentals/)
- [Backbone Cheat Sheet](http://www.igloolab.com/downloads/backbone-cheatsheet.pdf)
- [Backbone Patterns](http://ricostacruz.com/backbone-patterns/)
- [What is a model?](https://cdnjs.com/libraries/backbone.js/tutorials/what-is-a-model/)
- [What is a view?](https://cdnjs.com/libraries/backbone.js/tutorials/what-is-a-view/)
- [What is a collection?](https://cdnjs.com/libraries/backbone.js/tutorials/what-is-a-collection/)
- [How do JS timers work?](http://ejohn.org/blog/how-javascript-timers-work/)
