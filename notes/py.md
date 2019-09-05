# Data Structure
# tuple
* cannot be modified
* merge `tup = tup1 + tup2`
* multiplication `tup = (1,) * 1000`


# I/O
## string justification
```python
>>> print('|' + 'hej'.ljust(20) + '|' + 'hej'.rjust(20) + '|' + 'hej'.center(20) + '|')
|hej                 |                 hej|        hej         |
>>> print('hej'.center(20, '+'))
++++++++hej+++++++++
```
# Stream
## try
```python
try:
    #
except：# if exception occurs
    #
else:
    #
```
```python
try:
    #
finally: # regardless of exception
    #
```
other case for `except`
```python
except ValueError, Argument:
    print("xxxxx", Argument)
```

| Error type |  |
| ---- | ---- |
| `KeyboardInterrupt` | `^C` |
| `AssertionError` |  |
| `IOError` |  |
| `ImportError` |  |
| `SyntaxError` |  |
| `IndentationError` |  |
| `TypeError` |  |
| `ValueError` |  |
