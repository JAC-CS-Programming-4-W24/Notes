# Python  OO (Summary)

> Python gives you a lot of flexibility (to make mistakes).  Code carefully!

## Simple Class

```python
class class_name:
```

### Initializer (Constructor)

If not initializer is defined, the default initiallizer is used (i.e. does nothing)

```python
class Foo:
  def print_hi(self):
    print("hi")
```



To define an initializer (constructor), override the method `__init__`

```python
class Foo:
  def __init__(self):
    self.x = 3
  def print_hi(self):
    print(f"x is equal to {self.x})
```



### Properties

#### instance properties

Unlike C#, all properties in python must be attached to the object variable (`self`).  

```python
class Foo:
  
  def __init__(self, y):
    self.y = y
    
  def some_method(self):
    y = 33		    # does nothing, as y is a local variable
    self.y = 55		# this changes the instance variable

foo = Foo(3)
print (foo.y)		# prints 3

foo.some_method()
print (foo.y)		# prints 55

```



##### Cool Python Stuff

To see what properties are attached to an object, use the `__dict__` property

```python
class Foo:
  
  def __init__(self, y):
    self.y = y
    self.something = "sandy"

foo = Foo(3)
print(foo.__dict__)		# prints {'y': 3, 'something': 'sandy'}

```



#####  WEIRD PYTHON STUFF (why we need to use type hinting)

You can create instance properties *outside* of the initializer method.

```python
class Foo:
  def __init__(self,y):
    self.y = y
  def some_method(self):
    self.hello = "hello"

foo = Foo(6)
print (foo.hello)			# Error: foo has no attribute "hello"
foo.some_method()
print(foo.hello)			# prints hello
```



##### VERY VERY WEIRD PYTHON STUFF (why we need to use type hinting)

You can create instance properties *outside* of the class.

```python
class Foo:
  def __init__(self,y):
    self.y = y

foo = Foo()
foo.hello = "hello" 	# no error
print(foo.hello)			# prints hello
```
**LESSON LEARNED** Always use type hinting, AND fix all warnings!


#### class properties

If a variable is described outside of any method, then the variable will be a `class variable` (in C# this would be called a static variable).

Class variables must be defined.
```python
class Foo:
  x: int = 300
  def __init__(self, y):
    self.y = y

foo3 = Foo(3)
foo5 = Foo(5)

print (Foo.x)  	# print 300

# WEIRD PYTHON
print (foo3.x) 	# print 300 (can access class variables - read only - through an instance)


```



##### Weird python stuff

Class variables can be accessed via the instance, as long as there is no instance attribute of the same name.

```python
class Foo:
  x: int = 300
  y: int = 200
  def __init__(self,y):
    self.y
  def change_x(self):
    Foo.x = 900
    
f = Foo(3)
other = Foo(6)

print(f.x)		# prints 300 (the class property)
print(f.y)		# prints 3 (the instance property)
print(Foo.y) 	# prints 200 (the class property)

f.change_x()
print (other.x)	# prints 900 (the class property)
```



**Lesson Learned**: Don't use class properties unless you have to, and if you do, capitilize their name so that you *know* that it is a class property and not an instance property.

## Inheritance Syntax

In python (and other languages), we start with a `super` class, not a `base` class

To inherit from a super/base class, use the following syntax

```python
class Super:
  pass
    
class SubClass(Super):
  pass
```



If no `__init__` is defined for the `SubClass`, then the `__init__` of the `Super` class will be called by default.

```python
class Super:
  
  def __init__(self):
    self.hello = "hello"
    self.goodbye = "goodbye"
      
class SubClass(Super):
  pass

s = SubClass()
print(s.hello)			# prints hello
print(s.goodbye)		# prints goodbye
```



If an `__init__` is defined for `SubClass`, then the `Super.__init__` will not be called

```python
class Super:
  
  def __init__(self):
    self.hello = "hello"
    self.goodbye = "goodbye"
      
class SubClass(Super):
  def __init__(self):
    self.hello = "bonjour"

s = SubClass()
print(s.hello)			# prints bonjour
print(s.goodbye)		# AttributeError: 'SubClass' object has no attribute 'goodbye'
```



What to do?  Call the super class's `__init__` function directly, using `super()` to get the `super object`.
```python
class Super:
  
  def __init__(self):
    self.hello = "hello"
    self.goodbye = "goodbye"
      
class SubClass(Super):
  def __init__(self):
    super().__init__()
    self.hello = "bonjour"

s = SubClass()
print(s.hello)			# prints bonjour
print(s.goodbye)		# prints goodbye
```



Use the same idea for any method

```python
class Super:
  def __init__(self):
    self.hello = "hello"
    self.goodbye = "goodbye"
    
  def talk(self):
    print(self.hello)
    

class SubClass(Super):
  def talk(self):
    print("This is me talking:")
    super().talk()
    print("This is me stopping")
    
f = SubClass()
f.talk()

# OUTPUT
# This is me talking:
# hello
# This is me stopping
```



#### Checking `type` of object

Don't use `type`.  Use `isinstance`.

```python
class Super:
	pass
    

class SubClass(Super):
	pass


foo = SubClass()

type(foo) == Super   	  # False

isinstance(foo, Super)	# True


```

