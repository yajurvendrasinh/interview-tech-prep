### Selection Sort

#### About

This is a sorting algorithm that repeatedly selects the next smallest element and swaps it into place.

#### Summary

Break up array into two parts. The first part is already sorted. In the second part, find the index of the smallest element in that array and switch the element with the left-most index of the unsorted part of the array.

1. Find the smallest element. Swap it with the first element.
2. Find the second smallest element. Swap it with the second element.
3. Repeat by finding the n-th smallest element and swap it with the n-th element.

#### Psuedocode

1. Selection sort loops over each index in the array.
2. For that index, it finds the minimum element in the subarray starting at that index. 
3. swaps values with the index of the minimum element in that subarray and the start index of that subarray

#### Implementation

```
var selectionSort = function(array) {
    var index;
    for (var i = 0; i < array.length; i++) {
        index = minIndex(array, i);
        swap(array, i, index);
    }
    return array;
}

var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
}

var minIndex = function(array, startIndex) {
    var minValue = array[startIndex];
    var minIndex = startIndex;
    
    for (var i = minIndex + 1; i < array.length; i++) {
        if (array[i] < minValue) {
            minValue = array[i];
            minIndex = i;
        }
    }
    return minIndex;
}

var array = [1,2,3,4,1,4];

console.log(selectionSort(array)); //[ 1, 1, 2, 3, 4, 4 ]
```

#### Run time discussion

The beef of this algorithm lies in minIndex, finding the index of the minimum value in the unsorted subarray. Doing this n times is O(n^2).

1. The run time for swap. We know that there are n calls to swap, and each call to swap takes constant time.
2. The running time for all the calls to minIndex. MinIndex is called n times and each time it runs is n, then n-1, then n-2...all the way to 1. This arithmetic series (1 + 2 + .. N-1 + N) sums up to (N^2+N)/2. So we know minIndex takes N^2.

Dropping all but the most significant term, we get N^2 as the running time for this algorithm. There is no particularly good or bad case for this algorithm. It will always take N^2 regardless of the input.



