### Binary Search

#### About

Binary search is an efficient algorithm for finding an item from an ordered list of items.

#### Summary of algorithm

Binary search repeatedly divides an ordered list in half until it finds the item.

#### Psuedocode

- Inputs: an array or sorted ints, an int to find
- Output: index in array where int to find is

Step 1. let min = 1 and max = n (size of input array)

Step 2. let guess = (take the average of min and max and round down)

Step 3. array[guess] is the number to find, return

Step 4. if array[guess] is too low, set min to be array[guess+1]

Step 5. if array[guess] is too high, set max to be array[guess-1]

Step 6. Go back to step 2 and continue guessing.

#### Implementation

```
var binarySearch = function(array, targetValue) {
    var min = 0;
    var max = array.length-1;
    var guess;
    while (min <= max) {
        guess = Math.floor((min + max)/2);
        if (array[guess] === targetValue) {
            return guess;
        } else if (array[guess] < targetValue) {
            min = guess+1;
        } else {
            max = guess-1;
        }
    }
    return -1;
}

var arr = [1,2,3,4,5,6,7,8,9,10];
var target = 7;

binarySearch(arr, 7); //6
```

#### Run time discussion

Every time we double the size of the input array we need to make one more guess. We expect the number of guesses in the worst case to be the number of times we repeatedly halve n until we get the value, plus 1.

The worst case running time for binary search is O(log n). The number of guesses to make is at most log(n) + 1. 






