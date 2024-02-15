# Traversals

A *traversal* is a sequence of steps visiting each element in the data type.

## Traversal

A *traversal* is a series of operations that enable a visiting of each of the elements in the collection. 

For example the traversal of $\{ "a", "b", "c" \}$ will be: first "a", then "b", then finally "c".


## Iterators and Iterables

Traversals are used to "loop" over the data type. For example, if `my_collection` is a traversable collection of elements then we can write the following:

```python
collection: Iterable = MyCollectionClass()
collection_iter = iter(collection)
while True
	try:
   	s = collection_iter.__next__()
   	print(s)
  except StopIteration:
  	break
  	
# the above is equivalent to:
for s in collection:
	print(s)
	
```

### Iterable API
In python, an iterable is an object which allows the traversal of data.  

For an object to be `iterable`, it must have a method `__iter__` which returns an `iterator`.  In some cases, an `iterable` is also an `iterator`.

## Iterable API

| `__iter__`       |                                                              |
| ------------ | ------------------------------------------------------------ |
| Description  | Initializes, and returns an `iterator` |
| Signature    | `__iter__() -> iterator`                                         |
| Precondition | None |
| Mutator      | No |
| Returns      | an `iterator` object |



## Iterator API

In python, an `iterator` is an object that will traverse a series of elements.  An `iterator` must *also* be `iterable`.


| `__next__`       |                                                              |
| ------------ | ------------------------------------------------------------ |
| Description  | If there is a next element, it is returned.  If there is no more elements to be returned, a `StopIteration` Exception is thrown. |
| Signature    | `next() -> T`                                                |
| Precondition | The traversal has been initialized and no modifications to the collection have been performed since the initialization.  |
| Mutator      | Yes, but only internals which keep track of which element is 'next' |
| Returns      | Return the current element in the traversal |

| `__iter__`       |                                                              |
| ------------ | ------------------------------------------------------------ |
| Description  | Initializes, and returns an `iterator` |
| Signature    | `__iter__() -> iterator`                                         |
| Precondition | None |
| Mutator      | No |
| Returns      | an `iterator` object (typically `self`) |

