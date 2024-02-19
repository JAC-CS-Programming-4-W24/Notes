# Traversals

A *traversal* is a sequence of steps visiting each element in the data type.

## Traversal

A *traversal* is a series of operations that enable a visiting of each of the elements in the collection. 

For example the traversal of $\{ "a", "b", "c" \}$ will be: first "a", then "b", then finally "c".


## Iterators and Iterables

Traversals are used to "loop" over the data type. For example, if `my_collection` is a traversable collection of elements then we can write the following:

```python
from typing import Iterable, Iterator

collection: Iterable = MyCollectionClass()
collection_iter: Iterator = iter(collection)
while True:
    try:
        s = collection_iter.__next__()
        print(s)
    except StopIteration:
        break

# the above is equivalent to:
for s in collection:
    print(s)
```


## Iterator API

In python, an `iterator` is an object that will traverse a series of elements.  An `iterator` must *also* be `iterable`.

| `__iter__`   |                                                                     |
|--------------|---------------------------------------------------------------------|
| Description  | Initializes, and returns an `Iterator`                              |
| Signature    | `__iter__() -> Iterator[T]`                                         |
| Precondition | None                                                                |
| Mutator      | Yes, but only internals which keep track of which element is 'next' |
| Returns      | an `Iterator` object                                                |


| `__next__`   |                                                                                                                                  |
|--------------|----------------------------------------------------------------------------------------------------------------------------------|
| Description  | If there is a next element, it is returned.  If there is no more elements to be returned, a `StopIteration` Exception is thrown. |
| Signature    | `next() -> T`                                                                                                                    |
| Precondition | The traversal has been initialized and no modifications to the collection have been performed since the initialization.          |
| Mutator      | Yes, but only internals which keep track of which element is 'next'                                                              |
| Returns      | Return the current element in the traversal                                                                                      |


## Range

```python
from typing import Iterator

class Range:
    """A range of integers from low (inclusive) to high (exclusive)."""

    def __init__(self, low: int, high: int):
        self.low: int = low
        self.high: int = high
        self._cursor: int

    def __iter__(self) -> Iterator[int]:
        self._cursor = self.low
        return self

    def __next__(self) -> int:
        if self._cursor == self.high:
            raise StopIteration
        tmp: int = self._cursor
        self._cursor += 1
        return tmp

    def __str__(self):
        return f"[{self.low}, {self.high}]"

```

What does this output:

```python
range = Range(1, 10)
sum: int = 0
for i in range:
    sum += i
```

under the hood

```python
range = Range(1, 10)
sum: int = 0 
try:
    it = iter(range)
    while True:
        i = next(it)
        sum += i
except StopIteration:
    pass

```

under the hood

```python
range = Range(1, 10)
sum: int = 0 
try:
    it = range.__iter__()
    while True:
        i = it.__next__()
        sum += i
except StopIteration:
    pass

```

