# Importing and `__name__`

## Importing

Assume we have these two files.

`bar.py`
```python
print ("I am executing bar.py")
```

`foo.py`
```python
import bar
print ("I am executing foo.py")
```

When we execute (run) `bar.py`, it prints what you would expect.
```text
I am executing bar.py
```

But, if we execute `foo.py`, it also prints the same line. 
```text
I am executing bar.py
I am executing foo.py
```

Why??

Because when python imports a file, it executes ALL of the code within that file.  Which means that it executes the `print` statement in `bar.py` as it is being imported.

![python import mechanism](./images/python_import.svg)


### `__name__` variable

Python has a series of special variables, that it sets as programs and files are being loaded into memory.  One of these is the `__name__` variable.  If the program is being run directly, `__name__` is set to the default `__main__`.

`bar.py`

```python
print( f"I'm in bar.py and the value of __name__ is {__name__}")
```

```text
> python3 bar.py
I'm in bar.py and the value of __name__ is __main__
```

What happens when `bar.py` is imported into foo?

`foo.py`

```python
import bar
print (f"I'm in foo.py and the value of __name__ is {__name__}")
```

```text
> python3 foo.py
I'm in bar.py and the value of __name__ is bar
I'm in foo.py and the value of __name__ is __main__
```

> NOTE: notice how the value of `__name__` is different if the file is imported, versus when it is executed directly.

### Why `if __name__ == "__main__"`

So, ultimately, we want to know why so many python scripts have:

```python
if __name__ == "__main__":
    main()
```

or

```python
if __name__ == "__main__":
    print("Put debugging statements here")
```

`bar.py`

```python
# if executed from the command line, python sets:
# __name__ = "__main__"
# otherwise, if imported in another file
# __name__ = "bar"

def some_func(): pass
def main(): print ("hello")

if __name__ == "__main__":
    main()
    print("Some debugging info")
if __name__ == "bar":
    print("bar.py is being imported!")
```

When this is executed from the command line, python will set the `__name__` variable to "__main__" so the `if` statement will return true.

`foo.py`

```python
import bar
```

```text
>python3 bar.py
hello
Some debugging info

>python3 foo.py
bar.py is being imported!

```



