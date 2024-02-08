# 🚏 Queues

> The word 'queue' in the UK refers to what Americans and Canadians call a 'line'.

## 🎯 Objectives

- **Explain** the queue data structure.
- **Design** a queue data structure.
- **Solve** a problem using a queue.
- **Implement** a queue data structure in Python.

## ↪️ First in, First out

The illustration below shows people waiting for a bus.  In an orderly world, the first person at the bus stop will be the first person to board the bus, and the last person at the bus stop will be the last person to board the bus.

[![Bus Stop](./images/1-Bus-Stop.gif "The word 'queue' in the UK refers to what we call a 'line'.")](https://dribbble.com/shots/6290600-We-are-heroes)

A queue is a *collection* of data, just like a stack, only with a different set of rules. And like a stack, we refer to individual data items in the collection as *elements*.

A queue is a **FIFO** collection: the *first* element added to the queue is the *first* element to leave.

**Let's draw a queue like this:**

![Queue diagram](images/queue.svg)

- **front:** the element at the first position in the queue.
- **rear:** the element in the last position in the queue.
- **empty:** when there are no elements in the queue.
- **capacity:** the maximum number of elements in the queue.

## 📐 Queue Design

For every operation we design we will consider:

1. A description of what the operation accomplishes.
2. What the operation is called, what are it's inputs and outputs. This is called the *signature*.
3. What are the operation's *preconditions*, that is, what condition is required to be met in order to call the method.
4. What are the operation's *postconditions*, that is, what are the expected changes  the object when the operation is called.

### ▶️ Exercise 4.1 - Queue Design

Again, lets only consider a collection `int` for now to keep it simple.

A *enqueue* operation adds an element to the rear of the queue.

![Enqueue](images/enqueue.svg)

A *dequeue* operation removes an element from the front of the queue.

![Dequeue](images/dequeue.svg)

What is a possible problem: queue *underflow*.

![Queue underflow](images/dequeue_underflow.svg)

What is a possible problem: queue *overflow*.

![Queue overflow](images/enqueue_overflow.svg)



## Queue API

<!-- tabs:start -->

### **enqueue**

| Signature    | `enqueue(element: int)`                      |
|--------------|----------------------------------------------|
| Description  | Add an element to the **rear** of the queue. |
| Precondition | Queue is not full.                           |
| Mutator      | Yes.                                         |
| Returns      | None.                                        |

### **dequeue**

| Signature    | `dequeue() -> int`                                  |
|--------------|-----------------------------------------------------|
| Description  | Remove the element from the **front** of the queue. |
| Precondition | Queue is not empty.                                 |
| Mutator      | Yes.                                                |
| Returns      | The front element (**removed**) from the queue.     |

### **front**

| Signature    | `front() -> int`                                    |
|--------------|-----------------------------------------------------|
| Description  | Get the **front** element of the queue.             |
| Precondition | Queue is not empty.                                 |
| Mutator      | No.                                                 |
| Returns      | The front element (**not removed**) from the queue. |

### **is_empty**

| Signature    | `is_empty() -> bool`                             |
|--------------|--------------------------------------------------|
| Description  | Check if the queue is empty.                     |
| Precondition | None.                                            |
| Mutator      | No.                                              |
| Returns      | `true` if the queue is empty, `false` otherwise. |

### **is_full**

| Signature    | `is_full() -> bool`                             |
|--------------|-------------------------------------------------|
| Description  | Check if the queue is full.                     |
| Precondition | None.                                           |
| Mutator      | No.                                             |
| Returns      | `true` if the queue is full, `false` otherwise. |

<!-- tabs:end -->

> "Queue exists" precondition: the existence of the object is required for all operations so we will omit it as a precondition. It will be considered incorrect on test.

## Implementing a Queue using an Array

### Flat Array

In this method, the `head` of the queue will *always* be at the zeroth index of the array. The last item in the queue will be at the `R`th element of the array.

As items are added to the queue, the value of `R` increases by 1.

As items are 'dequeued' from the queue, the value of R is decreased by 1, and the items are all shifted so that the `head` of the queue remains at the zeroth index of the array

![Flat Array](./images/Queue_to_Array.svg)

**Class Discussion**

Do you see any issues with this method of implementation?



### ▶️ Exercise 4.2 - Queue Implementation

Please click [here](./4-Queues/Exercises/4.2_Queue_Array/) to do the exercise.

### Floating Array

The flat array requires a lot of overhead, as we constantly have to move items in the array every time we dequeue an element.

So, lets try it without shifting the elements.  This would require keeping track, not only of the last element, but also of the first element.

![Floating Array](./images/Floating_Array.svg)

**Class Discussion:**

Do you see any issues with this method of implementation?

### ⭕️ Circular Array

The floating array never recuperates the available memory at the beginning of the array once it is no longer used.  So how can we use this memory space?

Imagine that the array is circular (it's not, but lets pretend).

> An array is never really circular. We will code our use of array indices to treat the boundary between the `0` index array and the `capacity - 1`.

![Circular Array](./images/circular2.svg)



Now what?  Lets `enqueue` and `dequeue` like what was done in the "floating array", until we get near the end of available space.

![Almost Full Circular Array](./images/circular3.svg)



Until this point, `R` has been increasing by `1` every time something is added to the queue.  `R` is currently equal to `7`, so `R+1` would be equal to `8`, which exceeds the size of our array.  *However*, what is `8 % 8`?  Zero!  Right where we want it to be.

What if we wanted to add two items?

`R=7`, `(R+1)%8 = 0`, `(R+2)%8 = 1`

The beginning of a pattern is starting to emerge.

![Modular circular](./images/modular.svg)

### ％ Modulus

A standard way to implement the circular array is to use the modulus operation `%`. To see this, take a look at this sequence of expressions using the `%` operator, imagining that we have an array of length 4:

```text
0 % 4 = 0
1 % 4 = 1
2 % 4 = 2
3 % 4 = 3
4 % 4 = 0
5 % 4 = 1
6 % 4 = 2
... and so on ...
```

What we see is that any positive number `x` could be "flattened" into an array position between `0` and `length - 1`. We can now use this for our `enqueue()` and `dequeue()` methods!

Thus, if we have an array of size `N`, and our `rear` item is at position `n` in the array, a `enqueue` operation would place the new item into the array at position `(n+1) % N`.  

### ▶️ Exercise 4.3 - Circular Queue

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E4.3-Circular-Queue) to do the exercise.



Here is an example of a a flat array implementation in purple and a circular array implementation in blue and green:

![Circular Queue](./images/Circular-Queue.mp4 ':include :type=video controls width=100%')

## 📚 References

- [Application Programming Interface](https://en.wikipedia.org/wiki/API)

# Copyright Notice

All notes in this package are copyrighted under the Creative Commons License CC BY-NC

This license enables reusers to distribute, remix, adapt, and build upon 
the material in any medium or format for noncommercial purposes only, and only 
so long as attribution is given to the creator. 

CC BY-NC includes the following elements:

 BY: credit must be given to the creator.
 NC: Only noncommercial uses of the work are permitted.

Notes originated from Ian Clement, and modified by Vikram Singh.  
They have been subsequently modified by Ian Clement and Sandy Bultena.

All rights reserved (c) 2024
