# pipenv

Item | Link
:--- | :---
Overview | <https://pipenv.pypa.io/en/latest/>
CLI | <https://pipenv.pypa.io/en/latest/cli/>

Tool installation:

```
$ brew install pipenv
```

Project installation:

```
$ pipenv install
```

Run a command inside the virtual environment. The target Python script should
contain the right shebang (`#!/usr/bin/env python3`):

```
$ pipenv run src/stdio/hello.py HTTP
Hello, HTTP
```

Enable shell:

```
$ pipenv shell
```

Enable completion:

```sh
# You can add it to dotfiles, such as ~/.bash_profile
$ eval "$(pipenv --completion)"
```

Update `requirements-tests.txt`:

```
$ pipenv lock --dev --requirements > requirements-tests.txt
```

Uninstall project:

```
$ pipenv --rm
```

## References

- Should I put `#!` (shebang) in Python scripts, and what form should it take?
  <https://stackoverflow.com/questions/6908143>
- Advanced Usage of Pipenv
  <https://pipenv-fork.readthedocs.io/en/latest/advanced.html>
