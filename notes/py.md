# Data Structure
# tuple
* cannot be modified
* merge `tup = tup1 + tup2`
* multiplication `tup = (1,) * 1000`


# I/O
## join
```python
>>> str = ','
>>> seq = ['1','2','3'] # tuple is also ok
>>> str.join(seq)
'1,2,3'
```
## string justification
### ljust, rjust
```python
>>> print('|' + 'hej'.ljust(20) + '|' + 'hej'.rjust(20) + '|' + 'hej'.center(20) + '|')
|hej                 |                 hej|        hej         |
>>> print('hej'.center(20, '+'))
++++++++hej+++++++++
```
### zfill
```python
>>> s = '123'
>>> s.zfill(5)
'00123'
>>> s = '-123'
>>> s.zfill(5)
'-0123'
>>> a = 123
>>> "%05d" % a
'00123'
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
