# Interview Prep

Overview of what to cover when preparing for a technical interview.

### Data Structures

#### Arrays, Strings, and Lookup Tables

Since they have fast lookup and overwrites, Arrays are the most widely used of all data structures. That makes them a very popular interview question. A Lookup Table is a popular use of an array and a popular choice in Array based interview questions.

Types of problems cover numeric and character arrays (strings), 2D arrays. Some problems will use hashtables. Problems will also cover basic math (prime numbers, matrices, Fibonacci, etc).

Example problems

- Can you efficiently find two elements of an array with a max difference between them? What is the inefficient way to do this?
- Can you compress a string and run length encoding?
- Mutate a string in all the possible ways.
- Can you build a regex matcher?

#### Linked Lists, Stacks, Queues

Linked Lists usually aren't dealt with directly in application programming. However, you can find them in software that handles voice processing/video data. They can make good interview questions. Having a knowledge of Linked Lists also shows that you are familiar with basic memory management and that you can handle an ordered list of values.

Stacks and Queues are a special case of Linked Lists. Go over the basic operation of these structures, and then delve into some frequent applications (for example, traversing trees).

Example problems

- How do you build an LRU cache? (Linked List is the usual way of doing so)
- Can you implement a stack such that getMinimum() is an O(1) operation?

#### Binary Trees

Binary Trees are a popular and intuitive approach to representing hierarchical data. The popular interview variant is Binary Search Trees (BSTs). When data needs to remain sorted, arrays are expensive for insertion and deletion. BSTs are excellent candidates for inserting and deleting data that needs to remain sorted. You should cover various methods for traversing a BST and its applications.

Example problems

- How do you compute the lowest common ancestor of two nodes in a binary search tree?

Less important types of trees

- Red/Black trees
- AVL trees
- B-trees

#### Graphs

Social/interest networks are often represented as graphs on the backend. They can make a popular interview question.

Example problems

- Can you calculate the shortest path between two nodes on a graph?

#### Other useful data structures

Heaps, Tries, Suffix Trees, Interval Trees

### Algorithms

- Analyze complexity of space and time using Big O notation
- Pick algorithms appropriate to a data structure
- Algorithms for sorting, searching, traversing, transforming data structures. 
- Recursive and iterative algorithms.
- Internalize sorting algorithms (QuickSort and MergeSort on small and large data sets).

### Dynamic Programming

This is a good technique to get down. What it boils down to: you take a recursive algorithm, find the overlapping subproblems (repeated calls), and cache those results for future recursive calls.

### Brain Teasers

Fading trend, but may still be out there. Cover the popular ones.

### Concurrency Control

Mutexes, Read-Write lock, Distributed Resource contention problems.

### Large Scale System Design

Building systems that can handle thousands of requests per hour, or store GBs per second, or across geographically spread locations using hundreds of servers in the cloud. Learn to understand and appreciate some of these challenges.

A good source of problems: highscalability.com. 

Example problems

- How do you design a URL shortening service?

### Object Oriented Design

Understand popular design patterns. Learn how to translate real world objects into Classes. 

### Behavioral Questions

Used to get to know you, understand your resume better, and ease you into the interview.

#### Interview preparation grid

For your personal projects/resume experiences be sure you can talk in detail about the following:

- Challenges, Mistakes/Failures, what you enjoyed, leadership, conflicts, and what you'd do differently.
- Know your technical projects. Also think of follow up questions (how would you scale the application?)

#### Ask questions

- Genuine questions: "What brought you to this company? What is the interaction like between teams?"
- Insightful questions: Demonstrate knowledge or understanding of a technology.
- Passion questions: Demonstrate passion for a technology. Show that you're interested in learning and will be a strong contributor to the company.







