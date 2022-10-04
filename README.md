Algorithm test
===

### Introduction

This is an implementation of Boyer-Moore string-search algorithm. It finds the first occurrence of the pattern in the
text and returns the index. If the pattern is not found, it returns -1.

### Usage

```bash
$ python3 -m pip install pipenv

# Use virtualenv
$ PIPENV_VENV_IN_PROJECT=true pipenv shell

$ pipenv install --dev
```

- Unittest

```bash
$ pipenv run unittest
```

### References

- [Boyer-Moore string-search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm)
