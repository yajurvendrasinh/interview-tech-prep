### Insertion Sort

#### About

Insertion sort repeatedly inserts an element in the sorted subarray to its left.

#### Summary

The main step when inserting a value into a sorted subarray is making space in the array to put the current value.

To insert the next element, we repeatedly compare it with elements to its left, going right to left.
Each time we find that the key is less than an element to its left, we slide that element one position to the right, since we know that the key will have to go to that element's left.

We need to do two things here: have a slide operation that slides the value to the right. And have a variable that stores the current key.

Cases: 

1. When the element being inserted is less than all of the elements in the sorted subarray.

Every element in the subarray to the left of the key slides one position to the right, and we have to stop once we've run off the left end of the array.

2. When the element being inserted is greated than all of the elements in the sorted subarray.
No elements slide over and the key drops into the position that it started in.

#### Psuedocode

Iterate over array. Insert elements at index 1 to index n-1
into sorted subarray at 0 to n-2.

#### Implementation

```
var insertionSort = function(array) {
    //insert elements at index 1 to index n-1
    //into sorted subarray at 0 to n-2
    for (var i = 1; i < array.length; i++) {
        insert(array, i-1, array[i]);
    }
    return array;
}

//assumes array[0] - array[beginIndex] are 
//already sorted
//after this function is called, value is inserted
//and array[0] = array[beginIndex+1] become sorted

//insert function
var insert = function(array, rightMostIndex, value) {
    
    var key = value;
    //start from right to left
    for (var i = rightMostIndex; i >= 0; i--) {
        //if key is less than elt to its left
        //elt to its left slides one to the right
        
        if (array[i] > key) {
            array[i+1] = array[i];
        }
        
        //if key is greater than elt to its left
        //key ends up in current position
        if (array[i] <= key) {
            array[i+1] = key;
            break;
        }
        
        //if we're at the beginning of the array
        //array[0] becomes key
        if (i === 0) {
            array[i] = key;
        }
    }
    return array;
}

var array = [3, 5, 7, 11, 13, 2, 9, 6];
var array1 = [22, 11, 99, 88, 9, 7, 42];

//console.log(insert(array, 4, 2));
//[2, 3, 5, 7, 11, 13, 9, 6]

console.log(insertionSort(array1));
//[7, 9, 11, 22, 42, 88, 99]
```

#### Run time discussion

The main part of this algorithm is insert(), it correctly inserts a given value into an array.
It calls insert() on elements 1...n-1.

If we're inserting into a subarray with k elements, all k might have to slide over by one position. That would mean a time of O(n^2). Can it take less than n^2? Unlike selection sort, which always takes n^2, insertion sort can take less than n^2.

Worst case: O(n^2)
Best case: O(n)
Average case/random array: O(n^2)
"Almost sorted case": O(n)



