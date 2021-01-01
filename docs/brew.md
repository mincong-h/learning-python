# brew

Install Python using [Homebrew](https://brew.sh/).

## Install

Install a specific version of Python, such as 3.7:

```sh
> brew install python@3.7
```

## Link

Use a specific version of Python to replace the current one. For example, replace 3.9 by 3.7:

```sh
> brew link python@3.7
```

It's possible that it will fail with the following message:

```
> brew link python@3.7
Linking /usr/local/Cellar/python@3.7/3.7.9_2...
Error: Could not symlink bin/2to3
Target /usr/local/bin/2to3
is a symlink belonging to python@3.9. You can unlink it:
  brew unlink python@3.9

To force the link and overwrite all conflicting files:
  brew link --overwrite python@3.7

To list all files that would be deleted:
  brew link --overwrite --dry-run python@3.7
```

In this case, follow brew's instruction to unlink python 3.9 and then link to 3.7 again.

```sh
> brew unlink python@3.9
Unlinking /usr/local/Cellar/python@3.9/3.9.1_3... 25 symlinks removed
```

```sh
> brew link python@3.7
Linking /usr/local/Cellar/python@3.7/3.7.9_2... 28 symlinks created

If you need to have this software first in your PATH instead consider running:
  echo 'export PATH="/usr/local/opt/python@3.7/bin:$PATH"' >> ~/.zshrc
```

Now, check the current version of Python:

```sh
> python3 --version
Python 3.7.9
```
