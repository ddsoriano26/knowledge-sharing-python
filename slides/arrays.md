### Arrays

```python [1-2|1-3|1-2,4|1-2,5|1-2,6|1-2,7|1-2,8|10|10-11|13|13-14|16]
fruits = ["mangoes", "oranges", "apples", "jackfruits", "dragonfruits", 
"bananas"]
fruits[0]          # "mangoes"
fruits[0:3]        # ["mangoes", "oranges", "apples"]
fruits[2:5]        # ["apples", "jackfruits", "dragonfruits"]
fruits[:3]         # ["mangoes", "oranges", "apples"]
fruits[4:]         # ["dragonfruits", "bananas"]
fruits[:-4]        # ["mangoes", "oranges"]

name = "Hirai Momo"
name[-4:]          # "Momo"

uniform = [1] * 4
print(uniform)     # [1, 1, 1, 1]

data = ["mangoes", 1, 3+2j, 5.5]             # this is a list
```

- A string is considered an array of characters
- An array with more than one variable type is called a **list**