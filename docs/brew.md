# brew

Install Python using [Homebrew](https://brew.sh/).

## Search

Which Python do you want to install?

```sh
> brew search python
==> Formulae
app-engine-python             ptpython                      python@3.8
boost-python                  python-launcher               python@3.9 ✔
boost-python3                 python-markdown               reorder-python-imports
bpython                       python-tabulate               wxpython
gst-python                    python-tk@3.9                 pythran
ipython                       python-yq                     jython
micropython                   python@3.7 ✔                  cython
==> Casks
awips-python                                  mysql-connector-python

If you meant "python" specifically:
It was migrated from homebrew/cask to homebrew/core.
```

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

## Uninstall

```sh
> brew uninstall python@3.7
Uninstalling /usr/local/Cellar/python@3.7/3.7.10_2... (4,550 files, 71.7MB)
```

## Reinstall

```sh
> brew reinstall python@3.7
```

## Cleanup

Cleanup a package after uninstall:

```sh
> brew cleanup python@3.7
```

## Upgrade

Upgrade a package to a newer version:

```sh
> brew upgrade python@3.7
```

## Clear Cache

```sh
> rm -rf "$(brew --cache)"
```
