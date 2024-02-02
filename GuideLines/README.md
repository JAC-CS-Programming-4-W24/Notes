# Style CheckList (Python)

> Style checklist for C4P6: Programming IV

### Magic Numbers

Don't!

BAD

```python
classroom_too_small: bool = students > 30	
```

GOOD

```python
MAX_CLASSROOM_SIZE = 30
# ... some intervening code
classroom_too_small: bool = students > MAX_CLASSROOM_SIZE
```



### Naming Conventions

Overriding Principle: Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

Use meaningful names for variables/class/functions.  Do not use ong vague identifiers such as `subscript`.

Variables, and function names must use `snake_case`

```python
count: int
def parenthes_counter()
age_employee: int
count_students: int
```

Classes use PascalCase

```python
class Quest
class QuestPool
```

Globals are all uppercase, if multi-word, separate words with an underscore `_`

```python
DEFAULT_FILE_NAME: str = "input_file.txt"
PI: float = math.pi
MAX_SIZE: int = 30
PI_SQUARED: float = math.pi * math.pi
```

### Spacing

Use blank lines to logically group your program statements.  Comment your code block accordingly

```python
# read the data set from the supplied file
file = open("data.txt","r")
xs: list[int] = list(map(int,file.readline().split()))

# calculate the sum of the squares of the set
sum: int = 0
for x in xs:
  sum += x*x

# give info to user
print(sum) 	
```

### Documentation

#### Comments: 

Think of your code as a long long essay.  If there are no chapters or sub-chapters, then the code can be difficult to read.  Each block of code should have its own comment, describing what is the *purpose* of the code (not just a description of what the code does).

Bad Example:
```python
    file = open("day_13_input.txt", 'r')
    ans1 = 0
    ans2 = 0
    for para in read_paragraph(file):
        h_old, v_old = (-1, -1)
        lines = [l for l in para if len(l) != 0]
        if len(lines) > 0:
            ht, vt = find_mirror(lines)
            for h in ht:
                ans1 += (h + 1) * 100
                h_old = h
            for v in vt:
                ans1 += (v + 1)
                v_old = v
```

Better Example:
```python

		# open the input file for reading and set initial conditions
    file = open("day_13_input.txt", 'r')
    ans1 = 0
    ans2 = 0
    
    # read each paragraph, which defines the pattern that needes processing
    for para in read_paragraph(file):
    		
    		# set the initial horizontal and vertical symmetry lines
        h_old, v_old = (-1, -1)
        
        # create a list of non-empty lines from the paragraph (paragraphs always
        # include all of the last blank lines (sigh))
        lines = [l for l in para if len(l) != 0]
        
        # find all the possible symmetry lines and update the required answer as required
        if len(lines) > 0:
            ht, vt = find_mirror(lines)
            for h in ht:
                ans1 += (h + 1) * 100
                h_old = h										# saved for later use 
            for v in vt:
                ans1 += (v + 1)
                v_old = v										# saved for later use
```
> Aside.  I (Sandy) had to re-read the AoC question and review my code before I could figure out what my code was doing, so that I could add the comments.  Hence, this is why I should have had comments in the first place.

#### Class and function documentation
Use `docstring` to describe all classes and functions.

Give a very brief description of what the class/function does, not how the class/function works.

```python
class Array(Generic[T]):
    """Mimics a classic array with generic type [T]"""
```
```python
def binary_search(arr: Array[Comparable], low: int, high: int, value: Comparable) -> Optional[int]:
    """
    does a binary search for value in arr.
    :param arr: a sorted! array of type Array
    :param low: the lowest index to search from
    :param high: the highest index to search to
    :param value: the value that you are looking for
    :return: the index of the value in the array, if it exists,
            otherwise, None
    """
```

### Python Classes

#### Fields

Do NOT declare fields or properties (they are the same thing in python) outside of the constructor

BAD

```python
class Point:
  x: int = 0		# these are class variables!
  y: int = 0		# these are class variables!
  
  def __init__(self, a: int)
  	self.a: int = a
    
  def foo(self, b: int)
  	self.b: int = b  	# python allows this but you are not
                      # allowed to do this in this course!
```

GOOD

```python
class Point:
  x: int = 0		# these are class variables!
  y: int = 0		# these are class variables!
  
  def __init__(self, a: int)
  	self.a: int = a
    self.b: Optional[int] = None
    
  def foo(self, b: int)
  	self.b = b  	# OK
```

#### Private vs Public vs VERY Private

In python, there is no such thing as private vs public, however, there is an understanding that all methods, variables that start with an underscore (`_`) are private, and should not be used outside of the class.

For really private methods (typically reserved for built-in python methods), you can specify a double underscore (*dunder*)

**Python programmers are expected to be polite, and not use any private methods!**

Really bad python coding:

```python
class Foo:
    def __init__(self, b: int):
        self._a = "keep out"
        self.b = b

    def _private_method(self):
        print("Again, keep out!")

    def __forbidden__(self):
        print("You are crossing the line, buddy!")

x = Foo(3)
# --- it will run, but just don't do this -----
print(x._a)			
x._private_method()
x.__forbidden__()
```

### Type Hinting

Python is dynamically typed, which means that type is assigned to variables as the code is executed.  This can be very powerful at times, but can also lead to a lot of bad code which is difficult to read, and very difficult to debug.

So, you MUST use type hinting for all variables, and functions.

#### How to find the `type` of something

Use the `python` or `ipython` console.

Example: Suppose you don't know what the type is of an open file descriptor

```text
>>> file = open("text.txt", "r")
>>> type(file)
_io.TextIOWrapper
```

So, now in your file, you can type hint appropriately

```python
file: io.TextIOWrapper = open("text.txt", "r")
```

#### imports

When using typing on classes, the type hinting protocol can get confused depending on the order of the declaration of classes.  To prevent this, add this to the TOP of your code.

```python
from __future__ import annotations
```

#### Basic types

Example:

```python
a: int = 0
b: float = 1.1
c: bool = True

a = None # Invalid
```

#### Optional Types

```python
a: Optional[int] = 0
b: float = 1.1
c: bool = True

a = None # s'ok
```

#### Collections (`list`, `tuple`, `set`)

Example where content of collection is not defined

```python
a: list = list()			# what is in the list is not specified
a.append(3)
a.append("hello")
a.append(False)
a.append(None)
```

Example where content of collection is limited to a single type

```python
a: list[int] = list()			# only ints allowed in a
a.append(3)
a.append("hello")		# Nope!
a.append(False)			# Nope!
a.append(None)			# Nope!
```

Example where content of collection is limited to two types only

```python
a: list[int|str] = list()			# only ints or strings allowed
a.append(3)
a.append("hello")
a.append(False)			# Nope!
a.append(None)			# Nope!
```

Example where content of collection can be either a specific type, or `None`

```python
from typing import Optional
a: list[ Optional[int] ] = list()			
a.append(3)
a.append("hello")		# Nope!
a.append(False)			# Nope!
a.append(None)			
```

#### Function Signatures

Must define all inputs with a type, and return value if there is one.

```python
def division(a:int, b:int) -> Optional[int]:
	if b != 0:
    return a/b
  else:
    return None
```

```python 
# notice that we didn't define what's in the list,
# because it doesn't matter what the content is.

# no return value

def print_list(data: list):		
  print ("[", end="")
  for i in data:
    print(i, end=", ")
  print("]")
```

