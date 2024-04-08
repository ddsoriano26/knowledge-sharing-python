### Iterators

#### `for`
Iterate over a list or range of numbers

```python[0|1|2|4-6|5|6|0]
for i in range(0, 5):
    print(f"The number is {i}")

basket = ['apples', 'oranges', 'bananas', 'dragonfruits']
for fruit in basket:
    print(fruit)
```

#### `while`
Execute piece of code until a certain event or condition

```python [0|2]
x = 0
while x <= 5:
    x += 1
    print(x)
```