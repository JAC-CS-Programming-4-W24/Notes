# 🥞 Stacks

## 🎯 Objectives

- **Explain** the stack data structure.
- **Design** a stack data structure.
- **Solve** a problem using a stack.
- **Implement** a stack data structure in Java.

## ↪️ Last in, First out


A stack is a *collection* of data. We refer to individual data items in the collection as *elements*.

A stack is a **LIFO** collection: the *last* element added to the stack is the *first* element to leave.

Let's draw a stack like this:

![Stack diagram](./images/stack1.svg)



- **bottom:** the element at the "lowest" possible position in the stack.
- **empty:** where there are no elements in the stack.
- **top:** the element at the "highest" possible position in the stack.
- **capacity:** the maximum number of elements in the stack.

## 📐 Stack Design

For every operation we design we will consider:

1. A description of what the operation accomplishes.
2. What the operation is called, what are it's inputs and outputs. This is called the *signature*.
3. What are the operation's *preconditions*, that is, what condition is required to be met in order to call the method.
4. What are the operation's *postconditions*, that is, what are the expected changes  the object when the operation is called.

### ▶️ Exercise 3.1 - Stack Design

#### Normal Operations
Let's start by designing a stack that holds `int` values, only for now.

A *push* operation adds an element to the top of the stack.

A *pop* operation removes an element from the top of the stack.

![Push and pop](./images/stack2.svg)

#### Errors

![Stack underflow and overflow](./images/stack3.svg)

<!-- tabs:start -->

### **push**

| Signature    | `void push(int element)`                |
| ------------ | --------------------------------------- |
| Description  | Add an element to the top of the stack. |
| Precondition | Stack is not full.                      |
| Mutator      | Yes.                                    |
| Returns      | None.                                   |

### **pop**

| Signature    | `int pop()`                                      |
| ------------ | ------------------------------------------------ |
| Description  | Remove an element from the stack.                |
| Precondition | Stack is not empty.                              |
| Mutator      | Yes.                                             |
| Returns      | The element (removed) from the top of the stack. |

### **top**

| Signature    | `int top()`                                          |
| ------------ | ---------------------------------------------------- |
| Description  | Get the top element of the stack.                    |
| Precondition | Stack is not empty.                                  |
| Mutator      | No.                                                  |
| Returns      | The element (not removed) from the top of the stack. |

### **isEmpty**

| Signature    | `boolean isEmpty()`                              |
| ------------ | ------------------------------------------------ |
| Description  | Check if the stack is empty.                     |
| Precondition | None.                                            |
| Mutator      | No.                                              |
| Returns      | `true` if the stack is empty, `false` otherwise. |

### **isFull**

| Signature    | `boolean isFull()`                              |
| ------------ | ----------------------------------------------- |
| Description  | Check if the stack is full.                     |
| Precondition | None.                                           |
| Mutator      | No.                                             |
| Returns      | `true` if the stack is full, `false` otherwise. |

<!-- tabs:end -->

> "Stack exists" precondition: the existence of the object is required for all operations so we will omit it as a precondition. It will be considered incorrect on test.

- Alternate design: `size()` and `getCapacity()`.

## 🍔 APIs (Application Programming Interface)

You've probably heard the term "API" get thrown around in computer science. What does it mean exactly?

One analogy could be ordering from a menu:

The restaurant's menu is like its API. The menu is there to tell you what you're allowed to order at the restaurant. You can **only** order things that are listed on the menu, and **nothing else**.

API = [Application Programming Interface](https://en.wikipedia.org/wiki/API)

> In contrast to a user interface, which connects a computer to a person, an application programming interface connects computers or pieces of software to each other.
> 

## Example: Performing Math on a Computer

Python allows us to easily see what its code is compiled to (byte-code).  The byte code is then executed by the python interpretor.  This is the same as Java, which compiles to byte code, which in turn is executed by the Java Virtual Machine (JVM).

Python code:
```python
import dis

def foo(x: int, y: int) -> int:
     return 3 * (x / 5) + (y - 3)
  
print(dis.dis(foo))
```

What python code gets compiled to:
```text
              2 LOAD_CONST               1 (3)
              4 LOAD_FAST                0 (x)
              6 LOAD_CONST               2 (5)
              8 BINARY_OP               11 (/)
             12 BINARY_OP                5 (*)
             16 LOAD_FAST                1 (y)
             18 LOAD_CONST               1 (3)
             20 BINARY_OP               10 (-)
             24 BINARY_OP                0 (+)
             28 RETURN_VALUE
```

What do these instructions do? 

|Instruction |Description |
|------------|------------|
|`LOAD_CONST`| pushes a value onto a stack|
|`LOAD_FAST`| gets the value of the variable|
|`BINARY_OP`| pop two items off of the stack, perfom the operation, and push the result back onto the stack|
|`RETURN_VALUE`| pops an item off of the stack, and returns that value to the calling program|

![load and x/5](./images/stack4.svg)

![load and 3*x/5](./images/stack5.svg)

![load and 3*x/5](./images/stack6.svg)


## ▶️ Exercise 3.2 - Paired Brackets

Using just the Stack API, (pseudo) code a method `hasPairedBrackets` that uses a stack to determine if brackets `( )`, `{ }`, `[ ]` and `< >` are properly *paired*: each opened bracket is closed but only after subsequent opened brackets are closed.

Good: `()`, `([])`, `<[]()>`, `((()))`, etc.
Bad: `(`, `(]`, `{[}]`, `<<>`, `<>>`, etc.

If we ignore non-bracket characters, these would also be accepted:

Good: `<html>`, `(a[bc]?)`, `(you (should learn (lisp)))`, etc.

## ▶️ Exercise 3.3 - Stack Implementation

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E3.3-Stacks) to do the exercise.

## 📚 References

- [Application Programming Interface](https://en.wikipedia.org/wiki/API)
