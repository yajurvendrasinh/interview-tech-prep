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


