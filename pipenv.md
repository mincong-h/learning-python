# pipenv

<https://pipenv.pypa.io/en/latest/>

Tool installation:

```
brew install pipenv
```

Project installation:

```
pipenv install
```

Run a command inside the virtual environment. The target Python script should
contain the right shebang (`#!/usr/bin/env python3`):

```
$ pipenv run src/stdio/hello.py HTTP
Hello, HTTP
```

## References

- Should I put `#!` (shebang) in Python scripts, and what form should it take?
  <https://stackoverflow.com/questions/6908143>
