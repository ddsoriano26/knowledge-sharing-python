## `try` and `except`

Python's try-catch for errors/exceptions

```python [0|1|2|3|4|6|1-2,6-7|8|10]
try:
    x += 1
except ValueError as e:
    print(e)
    print("Value error")
except:
    print("Generic catch error")
else:
    x += y
finally:
    print(x)
```