### Conditional Operators

```python [0|1|2|3-4|5-6|7-8]
if type(x) == int:
    print("x is an integer")
elif type(x) == str:
    print("x is a string")
elif not type(x) == float:
    print("x is NOT a decimal number")
else:
    print("x is not an integer or string")
```

There is no `switch` statement in Python, but Python added a `match` statement in 3.10 onwards that is similar to `switch`:

```python [0|1|2-7|8-9]
match type(x):
    case int:
        print("x is an integer")
    case str:
        print("x is a string")
    case not float:
        print("x is NOT a decimal number")
    case _: # default
        print("x is not an integer or string")
```