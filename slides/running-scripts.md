### Running Python Scripts

```shell [0|1|2]
python script.py
python script.py -f
```

The built-in Python module `sys` is the most basic way to get command line arguments

```python [0|1|3|4]
import sys

arguments = sys.argv
print(arguments)          # ["script.py", "-f"]
```

There's a better module, [`argparse`](https://docs.python.org/3/library/argparse.html), to get arguments