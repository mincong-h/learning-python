# Errors

A list of Python errors that I made, and their solutions.

## Type Error

### TypeError: a bytes-like object is required, not 'str'

Error:

```
>>> base64.b64encode('user:pass')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/base64.py", line 58, in b64encode
    encoded = binascii.b2a_base64(s, newline=False)
TypeError: a bytes-like object is required, not 'str'
```

Solution:

```
>>> base64.b64encode('user:pass'.encode())
b'dXNlcjpwYXNz'
```
