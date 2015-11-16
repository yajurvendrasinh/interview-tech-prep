### D3 notes

- ['personal' branch I'm working off of](https://github.com/polinadotio/MKS28-visualize-it/tree/personal)

- Data Driven Documents
- You interact with data rather than the DOM
- D3 and jQuery are somewhat related, but D3 keeps track of things that would be really hard to keep track of if you were using jQuery.
- It is not a collection of charts.
- It's a toolset for manipulating the DOM, but more advanced than jQuery.
- Tying data to HTML.
- Decouples process of tying data to HTML
- Being able to reason in isolation. Isolate the manipulation of the data from the visualization of data.
- Humans are bad at multi-tasking.
- Separation of concerns: manipulate data in one place, visualization data in another place

### tl;dr

- select/identify nodes in DOM you will want to update
- bind data to nodes (D3's special sauce that jQuery can't do well)
- add/remove nodes as needed
- drive visualizations via D3 methods

```
  //select nodes
d3.selectAll('div')
  //bind data to nodes
  .data([1,2,3]);
```

### Libraries to explore

- [Working with SVG elts](http://alignedleft.com/tutorials/d3/an-svg-primer)

- [Core](https://github.com/mbostock/d3/wiki/API-Reference#d3-core) Selections, transitions, color.
- [Scales](https://github.com/mbostock/d3/wiki/API-Reference#d3scale-scales) Convert between data and visual encodings.
- [SVG](https://github.com/mbostock/d3/wiki/API-Reference#d3svg-svg) Create scalable vector graphics.
- [Time](https://github.com/mbostock/d3/wiki/API-Reference#d3time-time)
- [Layouts](https://github.com/mbostock/d3/wiki/API-Reference#d3layout-layouts)
- [Geography](https://github.com/mbostock/d3/wiki/API-Reference#d3geo-geography)
- [Geometry](https://github.com/mbostock/d3/wiki/API-Reference#d3geom-geometry)
- [Behaviors](https://github.com/mbostock/d3/wiki/API-Reference#d3behavior-behaviors)

### Resources

- [Intro D3 talk](https://github.com/vicapow/intro-to-d3-talk)
- [D3 book](http://alignedleft.com/tutorials/d3/)
- [Mike Bostock D3 Gallery](http://bost.ocks.org/mike/)
- [D3 viewer for Gists](http://bl.ocks.org/)
- [Prototyping D3 code](http://tributary.io/)

### Similarities between D3 and jQuery

```
$('.foo');
d3.selectAll('.foo');
```

- can select dom elements, manipulate attributes, and style

### Differences

- associate data with 3 divs in jQuery is much harder
- the data binding below is super easy but looks like magic

```
//you have 3 divs
d3.selectAll('div').data(['red', 'green', 'blue'])
  .style('color', function(d){return d})
```

`d` is data[i]. Each element in the data array gets returned and the color it represents gets set.

### What if our document has no divs/appropriate html tag?

```
//I've got more data than divs
d3.selectAll('div').data([18, 4, 7]);
  //lets create some divs
  .enter().append('div');
  //lets manipulate those divs now
```

```
//I've got less data than divs
d3.selectAll('div').data([18,4]);
  //lets delete some divs
  .exit().remove();
```

### General Update Patterns

- [Pattern 1](http://bl.ocks.org/mbostock/3808218)
- Data Join -> Enter -> Update -> Exit












