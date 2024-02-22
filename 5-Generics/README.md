# 🎭 Generics

> Generic classes and functions are reusable code that still allows the checking of data types.

## 🎯 Objectives

- **Explain** generic types in python.
- **Write** utility functions that use generics to make them type agnostic.

## Motivation

Here is a very general-purpose way to represent data that contains two integers, called a "pair":

```python
class IntPair:

    def __init__(self, first: int, second: int):
        self.first: int = first
        self.second: int = second

    def __str__(self):
        return f"({self.first}, {self.second})"
```

Here are some examples of how we could use this:

```python
point_2d: IntPair = IntPair(3, 4)
student_grade: IntPair = IntPair(123456, 76)
energy_gold: IntPair = IntPair(3, 25)
```

Note: most of the time you will want to represent pairs like these as classes in their own right, but every so often we need to pair data temporarily as part of an algorithm.

It would also be reasonable to have pairs of other things, strings for example:

```python
user_pass: StrPair = StrPair("foo", "abc123")
title_album: StrPair = StrPair("Miles Davis", "Kind of Blue")
```

What does `StrPair` look like? 

```python
class StrPair:

    def __init__(self, first: str, second: str):
        self.first: str = first
        self.second: str = second

    def __str__(self):
        return f"({self.first}, {self.second})"
```

Notice that the only difference in these two versions is the type annotations. Can we combine these into a single class? 

## No typing!

One option in python is to simply remove the types altogether. Something like:

```python
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f"({self.first}, {self.second})"
```

It works, but the downside is the loss of type hints and the consequences we discussed earlier in the course. For example, we can now make pairs of different types of data:

```python
pair: Pair = Pair(1, "abc")  # no error even if first and second are different types
```

This might sound useful in some circumstances, and so there's a data type called `tuple` that does just that. 

By the way, our original "pair" is called *homogeneous* since the two elements have same type. The `tuple` would be called a *heterogeneous* pair. 

## Type variables

There is a way to have both a single class and not lose restriction that the pair elements have same type. We can use a *type variable*. Type variables are variables that are assigned types instead of the usual data values. 

Here is how we create a type variable in python:

```python
T = TypeVar('T')
```

Don't worry about why `TypeVar` has a string argument, just think `T` is a new variable, but unlike the variables we're used to, `T` will store things like `int`, `str`, `TextIO`, etc... Yes, it is usual to name type variables with a single uppercase character. We will mostly use `T` and `S` but every so often we use different letters (ex: `K` and `V` for *key-value* data types).

> We don't assign type to type variables the way we do with normal variables, as you'll see soon enough.

## Generic pairs

Let's use a type parameter to make a generic pair:

```python
T = TypeVar("T")


class Pair(Generic[T]):

    def __init__(self, first: T, second: T):
        self.first: T = first
        self.second: T = second

    def __str__(self):
        return f"({self.first}, {self.second})"
```

There are a few differences:

1. We need to declare a type variable first.
2. We declare that `Pair` is `Generic[T]`, that is has a type variable `T`. Think of *generic* as a *general purpose* version of our class.
3. We use the variable `T` wherever we would have used `int` or `str` in the previous versions. This will be how the type checker will figure out what constrains the creation of pairs.

To use this *generic* pair we need to tell the type checker what flavour of pair it is by providing a type *argument* for `T`. We do this when we declare a variable (or parameter) of our generic data type. The syntax is something you are likely familiar with:


```python
point_2d: Pair[int] = Pair(3, 4)
user_pass: Pair[str] = StrPair("foo", "abc123")
```

The type inside the square brackets `[int]` (or `[str]`) is the type argument that is assigned to the type parameter `T` for that specific pair. 

So what would happen if tried the 

```python
pair1: Pair[int] = Pair(1, "abc")  # error second is a string
pair2: Pair[str] = Pair(1, "abc")  # error first is an int
```

Note: this second line gets a slightly different error message in pycharm, but it's fundamentally a violation of the constraint that the two parameters must be strings.

## ▶️ Exercises

### Generic `Stack` and `Queue`

Modify the `IntStack` class or the `IntQueue` class to a make a generic stack or queue. 

### Generic `Tuple`

Write a generic class with two components that can be of different data types. Hint: a tuple containing a `str` and an `int` would be created with:

```python
t: Tuple[str, int] = Tuple("abc", 123)
```


## Generic functions

## Exercises

### `count()`

Code a *generic* function `count` that takes an list and a value and returns the number of times that value occurs within the list.

Are there any method preconditions?

### `split_at()`

Code a *generic* function `split_at` that take in a list and position `pos` and returns a pair of lists. The first component of the pair is the list values from indices $[0, pos-1]$ and the second component is $[pos, length-1]$.

Are there any method preconditions?

### `zip()`

Code a *generic* function `zip` that takes in two lists and returns a single list with the elements at each indice "paired". For example:

```text
zip([1,2,3,4], [5,6,7,8]) = [(1,5), (2,6), (3,7), (4,8)]
```

Are there any method preconditions?

Here's an example of how `zip` could be used:

```python
for pair in zip(["a", "b", "c", "d"], ["e", "f", "g", "h"]):
    print(pair)
```

> Check out python's built-in function `zip`. It uses iterables (traversals) instead of lists. 


### Exercise: Identifying Type Arguments

Type parameters are "assigned" types when your code is type checked. In the case of methods and functions this is automatic, so it can be good to think a little bit about what `T` might be for some of your code.

What are the types assigned to variables (`?`) in the follow code snippet:

```python
data1: list[?] = "and now for something completely different".split(" ")

print(count(data1, "something"))   # in count: T = ?

data2: Pair[?] = split_at(data1, 3)  # in split_at: T = ?

data3: list[?] = zip([0, 1, 2, 3, 4, 5], data1)  # in zip T = ? 
```

## ⚖️ Generic Interfaces

Remember `Comparable`?

```java
public interface Comparable<T> {
    int compareTo(T rhs);
}
```

Why is there a type variable here?

Think about what happens when we call `compareTo(..)`:

```java
int comparison = bulbasaur.compareTo(charmander);
```

We want to compare our pokemon (`bulbasaur`) to a `rhs` that is also a pokemon (`charmander`).

It really doesn't make much sense to compare pokemon to anything else:

```java
int comparison = bulbasaur.compareTo(scanner);
int comparison = bulbasaur.compareTo(stack);
int comparison = bulbasaur.compareTo(team); // team is Pokemon[]
```

Java's type rules can enforce this by adding a type argument to the `implements` statement:

```java
public class Pokemon implements Comparable<Pokemon> {

    ...

    public int compareTo(Pokemon rhs) {
       ...
    }
}
```

## 🔬 Observations

### Type Erasure

- Type variables are for type-checking only.
- Types are erased after checking so that's why we have the funny cast

| Pros                          | Cons                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| reusable code!                | limited to methods that are available to all objects (without type variable bounds). Ex: .equals(..), .toString(), ... to |
| bad programs don't compile    | might be less efficient for primitives (wrapper classes)                                                                  |
| type checking works perfectly |                                                                                                                           |
| no need to cast return values |                                                                                                                           |
