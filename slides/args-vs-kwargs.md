### Arguments

Special symbols for declaring a variable number of arguments, `*args` and `**kwargs`

- `*args` - positional arguments
- `**kwargs` - keyword arguments

```python [0|1-8|5-6|10-12|14-23|17|18-23|25|16-23|26|16-23|18|27]
# *args example
def add_numbers(*num):
    result = 0

    for n in num:
        result += n

    return result

add_numbers(1)                          # 1
add_numbers(3, 10, 15)                  # 28
add_numbers(5, 1, 9, 10)                # 25

# **kwargs example
class Employee:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "name":
                self.name = value
            elif key == "gender":
                self.gender = value
            elif key == "level":
                self.level = value

emp1 = Employee(name="Denise", gender="Female", level=1)
emp2 = Employee("Ryan", gender="Male", level=1)
print(emp2.name)
```