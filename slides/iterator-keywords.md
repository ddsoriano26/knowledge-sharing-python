### Iterator Keywords

`pass` does nothing<br>
`continue` skips the rest of the loop and starts at the top<br>
`break` exits the loop

```python[0|1|3|4-10|12|3|10|12|6|5|3|12|8]
x = 1

while x < 10:
    if x % 2 == 0:
        x += 2
        continue
    elif x == 5:
        break
    else:
        pass

    x += 1
```