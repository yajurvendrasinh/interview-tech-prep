###Why sorting matters

We use computers to organize information for us. How can computers sort them? 

- The order of items makes a big difference (what you order on matters! alpha or most recent?)
- It helps you get to certain pieces of info faster (contacts in phone, emails)
- It helps you answer a superlative (what is the tallest, shortest, etc). If your group is in order, the answer to your question is the first person.

####Bubblesort

- Iterative algorithm
- “smallest values bubble up, one swap between consecutive cards at a time”
- Smallest values bubbling to the top is the longest part.
- The superlative (tallest, highest) item reaches the end of the list quickly. The smallest value can take a long time to get to the front of the list.
- Start with the leftmost element. If element to the right of this element has a smaller value, switch places. If not, do not do anything. Then, move to the next leftmost element. When you get to the end, repeat until no elements switch in an iteration (you’ve sorted the entire list).

####Selection Sort

- Iterative algorithm
- “selects and then swaps”
- involves markers
- put your marker on the left-most card. find the smallest card in the list and swap it with the current left-most card
- two markers. one for the current left-most card. another one to keep track of the smallest card of the remaining cards.

####Insertion Sort

- Iterative algorithm
- “finds and then inserts”
- Inserting is complicated.
- Start with second left most element. Check if all elements before you and stop at the first one that has the higher value. Once you’ve reached them, place the element to the right of it. If there are none with a higher value, place element at the beginning of the list. Repeat with the next left most element. 
- This forms a sublist at the front of the list that is already sorted. When the next element checks this list, it knows it’s already sorted. 
AKA: Insert the element in the correct place in the already sorted sublist, and the sublist will grow.

#### Merge Sort

- Divide and Conquer (Recursive) algorithm
- Merging is complicated (dividing is simple)
- Divide elements in half. Recursively sort each half. Merge the sorted halves together. 
- Merge sort is classic divide and conquer recursive solution.
- Once you’ve recursively sort each half, in order to merge them you know one important thing: of the two sorted sublists you have, the first item in your new merged list is going to be either the first item in your first sorted sublist or the first item in the second sorted sublist. You know this because you’ve already sorted them in ascending order.

Merging:

- 1) compare first elements of both sublists 
- 2) In new merged list, higher value is placed there and removed from its sublist
- 3) repeat until you’ve added all elements to the new merged list

####Quick Sort 

- Divide and Conquer (Recursive) algorithm
- Merging is simple (dividing is complicated)
- 1) Divide: split the list into sublists
- 2) Sort: recursively sort the sublists
- 3) Merge: merge the sorted sublists into a sorted list

####Dividing

- Systematically split the list into two sublists: items that are smaller than the first item and items that are larger than the first item. 
- Markers needed: mark items that have been divided, and a marker to separate the divided items into two groups: one group that is smaller than the first item and one group that is larger than the first item. 
- After you’ve gone through all elements once, move the first item to where the second marker is (separating the two groups) and repeat the process recursively on the two sublists to the left/right of the first item. 


####Why having lots of different kinds matters

- Learn to think of systematic strategies for solving problems. 
- Specific strategies let you be efficient with time and resources. Make sure you’re not repeating work.
- Different strategies work better with different groups of things to sort.
- Different strategies work better for difference scenarios where you want to make different trade-offs.
- Learning more than one way to do something makes you resourceful.
- Learning more than one way to do something is also a good reminder that there are many ways to solve something, and they all come with their strengths and weaknesses. 

Here’s to computers helping us stay organized!

####Interview tips:

- if you think sorting the data will help you but you don’t need to implement a sorting algorithm then and there, or the interviewer says you can just use a built in one, assume it’s O(n log (n)).

