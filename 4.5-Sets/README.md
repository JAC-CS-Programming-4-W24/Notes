# Sets

> The defining feature of sets is that its elements are UNIQUE.

In mathematics, a set is defined as **a collection of distinct, well-defined objects forming a group**. There can be any number of items, be it a collection of whole numbers, months of a year, types of birds, and so on. Each item in the set is known as an element of the set.

In other words a *set* is a collection of **distinct** elements.

```text
{2, 3, 5, 7} 
{'a', 'b', 'c'} 
{"aardvark", "aardwolf", "albatross"}
```

## Sets in Computer Science

In computer program, sets are represented by a collection of elements.   For each `element`, there must be some identifying feature that distinguishes one `element` from another, which ensures that each element in the set is *unique*.

In this discussion, the elements in our sets will be `objects` that have a property `id` which is unique to each object.

### Operations

#### Contains

The fundamental operation *contains* (a.k.a.: member, usually denoted by $\in$) on a set is to tell
if an element is contained within it:

$$
a \in {a, b, c}
c \not\in {a, b}
$$

#### Contains all

Determine if every element of a set $A$ is also in a second set $B$, that is, $A$ is entirely in $B$
(a.k.a. subset). This is usually written as $A \subseteq B$. For example:

$$
\{a, c\} \subseteq \{a, b, c, d\}  \hspace{1cm}  \{b, d\} \not\subseteq \{a, b, c\}
$$

A more formal definition of subset is: 

​	for all $x$, if $x \in A$ then $x \in B$.

#### Add

Sets are built using an operation for adding an element to an existing set. If we have a set
$\{a,b\}$, then $\textbf{add}(c)$ would yield $\{a,b,c\}$. Add should behave like the traditional
set *union* operation $\cup$, in that adding a duplicate to a set would leave the set unchanged. Ex:

$$
\{a,b,c\} \cup \{d\}  = \{a,b,c,d\} \hspace{1cm} \{a,b,c\} \cup \{b\} = \{a,b,c\}
$$

#### Remove

An element can be removed from a sorted set using the remove operation. If we have a set
$\{a,b,c\}$, then $\textbf{remove}(c)$ would yield $\{a, b\}$. Remove should behave like the
traditional set *difference* operation $-$, in that removing an element not in the original set
results in the set unchanged. Ex:

$$
\{ a, b, c \} - \{ d \} = \{ a, b, c \} \hspace{1cm} \{ a, b, c \} - \{ b \} = \{ a, c \}
$$

#### Size

Number of elements of the set (a.k.a. cardinality). This is usually written as $|A|$.

$$
A= \{ a, b, c \} \hspace{1cm} |A| = 3
$$

#### Empty

Determine if the set is empty ($\{\}$) or full. 

### Set API ###

This specification uses a type parameter `T`.


| `contains`   |                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| Description  | Determine if the set contains a specific element.                                                                     |
| Signature    | `__contains__(element: T) -> bool`                                                                                    |
| Precondition | There must be an agreed upon method to determine the uniqueness of each element.                                      |
| Mutator      | No.                                                                                                                   |
| Returns      | If the element is found in the set that equals `element`, then returns `True`, otherwise, the method returns `False`. |

| `contains_all` |                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determine if the set contains all the elements of the provided set, or, that the provided set is a subset of the current set.       |
| Signature      | `contains_all(other: Set[T]) -> bool`                                                                                               |
| Precondition   | There must be an agreed upon method to determine the uniqueness of each element.                                                    |
| Mutator        | No.                                                                                                                                 |
| Returns        | Returns `True` if all the elements of `rhs` are in the current set, `False` otherwise. If the provided set is empty, return `True`. |

| `add`        |                                                                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description  | Add an element into the set. If there is no element in the set that equals `element`, then the element is inserted into the set, otherwise the set is unchanged. |
| Signature    | `add(element: T) -> bool`                                                                                                                                       |
| Precondition | There must be an agreed upon method to determine the uniqueness of each element.                                                                                 |
| Mutator      | Yes.                                                                                                                                                             |
| Returns      | The method returns `True` if the element is added to the set, and `False` otherwise.                                                                             |
|              |                                                                                                                                                                  |

| `remove`     |                                                              |
| ------------ | ------------------------------------------------------------ |
| Description  | Remove an element from the set. If there is an element in the set equal to `element`, then it is removed from the set. Otherwise, the set is unchanged. |
| Signature    | `remove(element: T)`                                         |
| Precondition | The element to be removed must exist in the set.             |
| Mutator      | No.                                                          |
| Returns      |                                                              |
| Raises       | `TypeError` if element is not in set                         |

| `length`     |                                              |
|--------------|----------------------------------------------|
| Description  | Determine the number of elements in the set. |
| Signature    | `__len__() -> int`                           |
| Precondition | None.                                        |
| Mutator      | No.                                          |
| Returns      | Returns the number of elements in the set.   |

| `is_empty`   |                                                        |
| ------------ | ------------------------------------------------------ |
| Description  | Determine if the set is empty.                         |
| Signature    | `is_empty() -> bool`                                   |
| Precondition | None.                                                  |
| Mutator      | No.                                                    |
| Returns      | Returns `True` if the set is empty, `False` otherwise. |

| `is_full`    |                                                                                          |
|--------------|------------------------------------------------------------------------------------------|
| Description  | Determines if the set is full (i.e. there is no more space to store additional elements) |
| Signature    | `is_full() -> bool`                                                                      |
| Precondition | None.                                                                                    |
| Mutator      | No.                                                                                      |
| Returns      | Returns `True` if the set is full, `False` otherwise.                                    |

| `__str__()`    |                                                                        |
|----------------|------------------------------------------------------------------------|
| Signature      | `__str__()`                                                            |
| Description    | Get a string representation of the set.                                |
| Pre-conditions | None.                                                                  |
| Returns        | Returns a string representation of the set, consisting of:             |
|                | -   a `{`,                                                             |
|                | -   the string representations of the elements, comma-separated, and |
|                | -   a `}`.                                                             |

[Exercise](https://github.com/JAC-CS-Programming-4-W24/Exercise-04.5-UsingSets/blob/main/main.py)