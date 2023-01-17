## `unittest` setup example

Seems like the following is required:

- A directory inside which the code lives (in our case `lib/`), with an
`__init__.py` file therein
- A subdirectory of this directory called `test/`, again with an `__init__.py`
file within
- test files for (for example) `lib/foo.py` should live in `lib/test/test_foo.py`

Functions from the `lib/` folder can then be imported as follows:

```py
# File: lib/test/test_foo.py
from lib import foo

a_variable = foo.fun(1)
```
