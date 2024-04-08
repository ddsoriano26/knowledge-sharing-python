## Bitwise Operators

```python [1-2:1]
x = 0b100101
y = 0b110110

x & y == 0b100101                   # AND
x | y == 0b110111                   # OR
x ^ y == 0b010010                   # XOR
x << 1 == 0b1001010                 # Left-shift
y >> 1 == 0b11011                   # Right-shift
```

SIDE NOTE\: You can declare binary, octal, and hexadecimal values in Python

```python
bin_num = 0b101
oct_num = 0o171
hex_num = 0xAFE
```