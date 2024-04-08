### Tuples

- Like arrays, but immutable

```python [0|1-2|3-8]
fruits = ("mangoes", "oranges", "apples", "jackfruits", 
"dragonfruits", "bananas")
fruits[0]          # "mangoes"
fruits[0:3]        # ["mangoes", "oranges", "apples"]
fruits[2:5]        # ["apples", "jackfruits", "dragonfruits"]
fruits[:3]         # ["mangoes", "oranges", "apples"]
fruits[4:]         # ["dragonfruits", "bananas"]
fruits[:-4]        # ["mangoes", "oranges"]
```