### Time and Space Complexity of Data Structures

### Linked Lists

- `.head` property, a `Node` instance of LinkedList
- `.tail` property, a `Node` instance of LinkedList
- `.addToTail` method, adds value to end of list
- `.removeHead` method, removes first node and returns value
- `.contains` methods, returns boolean if value is in LinkedList

### Trees

- cool visualization on balancing an AVL tree: http://www.qmatica.com/DataStructures/Trees/AVL/AVLTree.html

- `.children` property, an array containing a number of subtrees
- `.addChild` method, given a value adds it as target of a node and adds node as a child in the tree
- `.contains` method, takes a value and return a boolean if found in tree

### Graphs

- This is an undirected graph.
- `.addNode` method, adds a new node to the graph.
- `.contains` method, given a node, return true if it is found in the graph
- `.removeNode` method, removes node from graph if present. All edges connected to the node are removed.
- `.addEdge` method, creates an edge between two nodes if they are present in the graph.
- `.hasEdge` method, returns a boolean if two nodes are connected by an edge.

