# Exercise 4.2 - 🚏 Queue Array

## 🎯 Objectives
Implement an array-based queue data structure in python..

## 🔍 Context
How should we use an array to store a queue? The simplest thing to do is base ourselves on the stack array implementation: store the elements in the lower portion of the array. Here we can put the front at position 0 and the rear in the highest index position:

For example, the queue

Queue

would be stored in an array:

Queue array

🚦 Let's Go
Let's set this up:

Create a class called IntQueue.
Add the necessary fields to store queue.
Create two constructors: one where the queue capacity is provided and one where it is not, relying on a default QUEUE_CAPACITY.
Implement the methods of the Queue API: enqueue(..), dequeue(), front(), isEmpty() and isFull().
Throw exception QueueOverflowException and QueueUnderflowException when the caller has not met the operation preconditions.
Pass the unit tests in the class TestQueue.
👑 Bonus - Queueable Interface
Create a Queueable interface which includes the necessary methods for a queue.
Have your IntQueue implement the Queueable interface and override all the interface's methods.
You can have the interface just use ints, but for an extra challenge, can you make it use generics instead?
No worries if you can't do this last part because we'll be learning generics later in the semester!
🔬 Observations
Which operation is more efficient and why?
What is the impact here?
Comic