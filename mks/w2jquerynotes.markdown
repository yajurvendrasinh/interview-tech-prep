### jQuery

- Good to cache your jQuery when possible.

### Debugging

```
$('#main').find('.username').trigger('click');
```

### Event delegation

```
// shorthand for document.ready
$(app.init());

//if you need to rely on this
$(app.init.bind(app));
```

### Ajax

A GET request

```
  var settings = {
  "async": true,
  "crossDomain": true,
  "url": app.server,
  "method": "GET"
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
```

A POST request

```
$.ajax({
  url: app.server,
  type: 'POST',
  data: JSON.stringify(message),
  contentType: 'application/json',
  success: function (data) {
    console.log('Message sent');
  },
  error: function (data) {
    console.error('Failed to send message');
  }
});

```
Another GET request

```
$.ajax({
  url: app.server,
  type: 'GET',
  data: JSON.stringify(message),
  contentType: 'application/json',
  success: function (data) {
    console.log('Message received');
  },
  error: function (data) {
    console.error('Failed to receive message');
  }
});

```

### JQuery vs Backbone

In jQuery we did our best to separate our concerns. Backbone allows us to do much better. The other motivation for using Backbone is that it eliminates the need for adding a lot of boilerplate code. In our jQuery implementation there's a lot of code reuse in our Ajax functions. Wouldn't it be great if we could abstract that out into a function?

### Backbone

- Uses a psuedoclassical instantiation model.
- Has an extend() function that implements subclassing for you.





