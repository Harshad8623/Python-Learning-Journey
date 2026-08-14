# ============================================================
#             PYTHON MODULES AND PIP
# ============================================================

"""
This file covers:

1. What is a Module?
2. Why do we use Modules?
3. Types of Modules
4. Built-in Modules
5. User-defined Modules
6. import
7. from ... import
8. import ... as
9. dir()
10. __name__
11. __name__ == "__main__"
12. What is a Package?
13. Module vs Package
14. What is pip?
15. What is PyPI?
16. Installing Packages
17. Uninstalling Packages
18. Upgrading Packages
19. Checking Installed Packages
20. requirements.txt
21. Virtual Environment
22. pip + Virtual Environment
23. Common pip Commands
24. Interview Questions
"""


# ============================================================
# 1. WHAT IS A MODULE?
# ============================================================

"""
A MODULE is a Python file containing Python code.

A module can contain:

    - Variables
    - Functions
    - Classes
    - Statements

A module normally has:

    .py

extension.

Example:

math_operations.py

This file can contain:

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b


Another Python file can import and use these functions.

Therefore:

MODULE = A Python file containing reusable code.
"""


# ============================================================
# 2. WHY DO WE USE MODULES?
# ============================================================

"""
Modules are useful because they provide:

1. Code reusability
2. Better organization
3. Easier maintenance
4. Separation of functionality
5. Avoiding duplicate code
6. Namespace management

Instead of writing everything in one huge file,
we can divide the project into multiple files.
"""


# ============================================================
# 3. SIMPLE MODULE STRUCTURE
# ============================================================

"""
Suppose our project looks like this:

project/
|
|-- main.py
|
|-- calculator.py
|
|-- student.py
|
|-- utility.py


calculator.py

    def add(a, b):
        return a + b


main.py

    import calculator

    print(calculator.add(10, 20))


This is modular programming.
"""


# ============================================================
# 4. TYPES OF MODULES
# ============================================================

"""
There are mainly three categories you should know:

1. Built-in / Standard Library Modules
2. User-defined Modules
3. Third-party Modules


Examples:

Built-in / Standard Library:

    math
    os
    sys
    random
    datetime
    json


User-defined:

    calculator.py
    student.py
    helper.py


Third-party:

    requests
    flask
    pandas
    numpy
    fastapi
"""


# ============================================================
# 5. BUILT-IN / STANDARD LIBRARY MODULE
# ============================================================

"""
Python provides many modules as part of its standard
library.

You don't normally need to install them using pip.

Examples:

    math
    random
    os
    sys
    datetime
    json
"""


# ============================================================
# 6. import
# ============================================================

"""
The import statement is used to import a module.

Syntax:

    import module_name
"""


import math

print(math.sqrt(25))

print(math.pi)


"""
Here:

math = module

sqrt = function inside math

pi = variable/constant provided by math


We access members using:

    module.member
"""


# ============================================================
# 7. IMPORT ANOTHER MODULE
# ============================================================

import random

print(random.randint(1, 10))


"""
random is a standard library module.

No pip installation is required.
"""


# ============================================================
# 8. from ... import
# ============================================================

"""
Instead of importing the complete module name,
we can import a particular member.

Syntax:

    from module import member
"""


from math import sqrt

print(sqrt(100))


"""
Now we can directly write:

    sqrt(100)

instead of:

    math.sqrt(100)
"""


# ============================================================
# 9. IMPORT MULTIPLE MEMBERS
# ============================================================

from math import sqrt, pi

print(sqrt(16))

print(pi)


# ============================================================
# 10. import AS
# ============================================================

"""
We can give an alias to a module.

Syntax:

    import module as alias
"""


import math as m

print(m.sqrt(49))

print(m.pi)


"""
Instead of:

    math.sqrt()

we can use:

    m.sqrt()
"""


# ============================================================
# 11. from ... import ... as
# ============================================================

from math import sqrt as square_root

print(square_root(64))


# ============================================================
# 12. DON'T USE from module import *
# ============================================================

"""
You may see:

    from math import *

This imports many names into the current namespace.

It is generally discouraged because:

    - It can cause name conflicts
    - It makes code less readable
    - It becomes difficult to know where a name came from

Prefer:

    import math

or:

    from math import sqrt
"""


# ============================================================
# 13. MODULE MEMBERS
# ============================================================

"""
A module can contain:

    - Variables
    - Functions
    - Classes
"""


# Example:

"""
calculator.py

PI = 3.14

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


main.py

import calculator

print(calculator.PI)
print(calculator.add(10, 20))
print(calculator.multiply(5, 6))
"""


# ============================================================
# 14. dir()
# ============================================================

"""
dir() can be used to inspect names available in an object
or module.
"""


import math

print(dir(math))


"""
This shows names available inside math module.

For example:

sqrt
pi
sin
cos
floor
ceil
etc.
"""


# ============================================================
# 15. __name__
# ============================================================

"""
Every Python module has a special variable:

    __name__

When a Python file is executed directly,
its __name__ is:

    "__main__"

When the file is imported as a module,
its __name__ is generally the module's name.
"""


print(__name__)


# ============================================================
# 16. __name__ == "__main__"
# ============================================================

"""
This is extremely important for interviews.

Example:

def greet():
    print("Hello")


if __name__ == "__main__":
    greet()


This means:

Run greet() only when this file is executed directly.

If another file imports this module,
the code inside the if block will not execute.
"""


# ============================================================
# 17. WHY IS __name__ == "__main__" USED?
# ============================================================

"""
It helps separate:

    Reusable module code

from:

    Code that should run when the file is executed directly.


Example:

calculator.py

def add(a, b):
    return a + b


if __name__ == "__main__":

    print(add(10, 20))


When running:

    python calculator.py

Output:

    30


But if another file does:

    import calculator

the test code inside:

    if __name__ == "__main__":

doesn't execute.
"""


# ============================================================
# 18. USER-DEFINED MODULE
# ============================================================

"""
Suppose we create:

calculator.py


Inside calculator.py:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


Now create:

main.py


Inside main.py:

import calculator

print(calculator.add(10, 20))

print(calculator.subtract(20, 5))


This is a USER-DEFINED MODULE.
"""


# ============================================================
# 19. USER-DEFINED MODULE EXAMPLE
# ============================================================

"""
File 1:

student.py

name = "Harshad"

age = 21

def greet():
    print("Hello", name)


File 2:

main.py

import student

print(student.name)
print(student.age)

student.greet()


This is how modules are used in real projects.
"""


# ============================================================
# 20. WHAT IS A PACKAGE?
# ============================================================

"""
A PACKAGE is a way of organizing related Python modules
into a directory structure.

Example:

myproject/
|
|-- main.py
|
|-- utilities/
|   |
|   |-- calculator.py
|   |-- string_utils.py
|   |-- file_utils.py


utilities is a package containing multiple modules.
"""


# ============================================================
# 21. MODULE VS PACKAGE
# ============================================================

"""
MODULE:

    Usually a single .py file.

Example:

    calculator.py


PACKAGE:

    A directory that organizes related modules/subpackages.

Example:

    utilities/
        calculator.py
        string_utils.py


Simple memory trick:

    Module = file

    Package = folder/collection of modules
"""


# ============================================================
# 22. WHAT IS pip?
# ============================================================

"""
pip is a package installer for Python.

pip is commonly used to:

    - Install packages
    - Uninstall packages
    - Upgrade packages
    - List installed packages
    - Show package information


Example:

    pip install requests
"""


# ============================================================
# 23. WHAT IS PyPI?
# ============================================================

"""
PyPI stands for:

    Python Package Index

PyPI is a large repository of Python packages.

Developers publish many third-party Python packages
on PyPI.

pip can install packages from package indexes such
as PyPI.
"""


# ============================================================
# 24. pip VS PyPI
# ============================================================

"""
VERY IMPORTANT INTERVIEW QUESTION:


PyPI:

    Repository / index containing Python packages.


pip:

    Tool used to install and manage Python packages.


Simple memory trick:

    PyPI = Store

    pip = Tool used to get packages from the store
"""


# ============================================================
# 25. INSTALLING A PACKAGE
# ============================================================

"""
Command:

    pip install requests


This installs the requests package.
"""


# ============================================================
# 26. INSTALLING A SPECIFIC VERSION
# ============================================================

"""
Command:

    pip install requests==2.32.0


This asks pip to install that specific version.
"""


# ============================================================
# 27. INSTALL MINIMUM VERSION
# ============================================================

"""
Command:

    pip install requests>=2.30


This requests version 2.30 or newer,
subject to compatibility and dependency resolution.
"""


# ============================================================
# 28. UPGRADE A PACKAGE
# ============================================================

"""
Command:

    pip install --upgrade requests

or:

    python -m pip install --upgrade requests
"""


# ============================================================
# 29. UNINSTALL A PACKAGE
# ============================================================

"""
Command:

    pip uninstall requests
"""


# ============================================================
# 30. LIST INSTALLED PACKAGES
# ============================================================

"""
Command:

    pip list

This displays installed packages and versions.
"""


# ============================================================
# 31. SHOW PACKAGE INFORMATION
# ============================================================

"""
Command:

    pip show requests

This can show information such as:

    - Name
    - Version
    - Location
    - Dependencies
"""


# ============================================================
# 32. FREEZE
# ============================================================

"""
Command:

    pip freeze

This prints installed packages in requirements-style format.

Example:

    requests==2.x.x
    flask==3.x.x
    numpy==2.x.x
"""


# ============================================================
# 33. requirements.txt
# ============================================================

"""
requirements.txt is commonly used to record project
dependencies.

Example:

requirements.txt

    Flask==3.1.0
    requests==2.32.0
    pandas==2.2.0


Then another developer can install the dependencies using:

    pip install -r requirements.txt
"""


# ============================================================
# 34. WHY requirements.txt IS IMPORTANT
# ============================================================

"""
Suppose your project uses:

    Flask
    requests
    pandas
    numpy

Another developer clones your project.

Instead of manually installing every package:

    pip install Flask
    pip install requests
    pip install pandas
    pip install numpy

they can use:

    pip install -r requirements.txt


This makes dependency setup easier and more reproducible.
"""


# ============================================================
# 35. CREATE requirements.txt
# ============================================================

"""
Command:

    pip freeze > requirements.txt


This writes installed package versions into the file.

NOTE:

For real projects, be thoughtful about whether you want
every package from the environment or only direct project
dependencies.
"""


# ============================================================
# 36. VIRTUAL ENVIRONMENT
# ============================================================

"""
A virtual environment creates an isolated Python environment
for a project.

Why is this useful?

Suppose:

Project A needs:

    Flask version X

Project B needs:

    Flask version Y

Installing everything globally can create conflicts.

Virtual environments isolate project dependencies.
"""


# ============================================================
# 37. CREATE VIRTUAL ENVIRONMENT
# ============================================================

"""
Windows:

    python -m venv venv


Linux / macOS:

    python3 -m venv venv
"""


# ============================================================
# 38. ACTIVATE VIRTUAL ENVIRONMENT - WINDOWS
# ============================================================

"""
Command Prompt:

    venv\Scripts\activate


PowerShell:

    .\venv\Scripts\Activate.ps1
"""


# ============================================================
# 39. ACTIVATE VIRTUAL ENVIRONMENT - LINUX / MAC
# ============================================================

"""
Command:

    source venv/bin/activate
"""


# ============================================================
# 40. DEACTIVATE
# ============================================================

"""
After finishing:

    deactivate
"""


# ============================================================
# 41. INSTALL PACKAGE INSIDE VENV
# ============================================================

"""
After activation:

    pip install flask


The package is installed into the environment
associated with that project.
"""


# ============================================================
# 42. RECOMMENDED COMMAND STYLE
# ============================================================

"""
Instead of relying on a separate pip executable, you can
use:

    python -m pip install requests

This makes it explicit which Python interpreter is being
used to run pip.

This is especially useful when multiple Python versions
are installed.
"""


# ============================================================
# 43. CHECK PYTHON VERSION
# ============================================================

"""
Command:

    python --version


or:

    python -V
"""


# ============================================================
# 44. CHECK PIP VERSION
# ============================================================

"""
Command:

    python -m pip --version
"""


# ============================================================
# 45. COMMON pip COMMANDS
# ============================================================

"""
+-----------------------------------------------+
| COMMAND                                       |
+-----------------------------------------------+
| python -m pip install package                |
| python -m pip install package==1.0.0         |
| python -m pip install --upgrade package      |
| python -m pip uninstall package              |
| python -m pip list                            |
| python -m pip show package                   |
| python -m pip freeze                         |
| python -m pip install -r requirements.txt    |
+-----------------------------------------------+
"""


# ============================================================
# 46. THIRD-PARTY MODULE EXAMPLE
# ============================================================

"""
Suppose we install:

    pip install requests


Then in Python:

    import requests


Now requests is a third-party library available
to our program.

Example:

    response = requests.get("https://example.com")

"""


# ============================================================
# 47. STANDARD LIBRARY VS THIRD-PARTY
# ============================================================

"""
STANDARD LIBRARY:

Comes with Python installation.

Examples:

    math
    random
    os
    sys
    json
    datetime


THIRD-PARTY:

Usually installed separately.

Examples:

    requests
    flask
    fastapi
    pandas
    numpy


Remember:

Standard library -> generally no pip required.

Third-party package -> often installed using pip.
"""


# ============================================================
# 48. MODULE IMPORT PROCESS
# ============================================================

"""
When Python encounters:

    import math

Python searches for the module in locations available
through its import system.

You can inspect Python's module search path using:

    import sys

    print(sys.path)
"""


import sys

print(sys.path)


# ============================================================
# 49. sys.path
# ============================================================

"""
sys.path is a list of locations Python searches when
trying to import modules.

It can include:

    - Current/project-related locations
    - Standard library locations
    - Site-packages
    - Other configured import paths
"""


# ============================================================
# 50. MODULE CACHING
# ============================================================

"""
Python generally caches imported modules in:

    sys.modules

This helps avoid repeatedly loading the same module
during a process.

Example:
"""


import sys

import math

print("math" in sys.modules)


# ============================================================
# 51. IMPORTING THE SAME MODULE
# ============================================================

"""
If a module is imported multiple times during a process,
Python generally reuses the already loaded module rather
than executing its top-level code from scratch every time.

This is one reason module imports are efficient.
"""


# ============================================================
# 52. __pycache__
# ============================================================

"""
Python may create a directory called:

    __pycache__

It can contain cached bytecode files.

Example:

    __pycache__/
        calculator.cpython-xxx.pyc

These files help Python manage compiled bytecode.

You normally don't need to edit them manually.
"""


# ============================================================
# 53. MODULE SEARCH EXAMPLE
# ============================================================

"""
Suppose:

project/
|
|-- main.py
|
|-- calculator.py


main.py:

    import calculator


Python needs to find calculator.py through its
module search process.

Therefore project structure and import paths matter.
"""


# ============================================================
# 54. GOOD PROJECT STRUCTURE
# ============================================================

"""
Example:

my_project/
|
|-- main.py
|
|-- requirements.txt
|
|-- README.md
|
|-- utils/
|   |
|   |-- calculator.py
|   |-- validators.py
|
|-- services/
|   |
|   |-- user_service.py
|   |-- payment_service.py
|
|-- tests/
|   |
|   |-- test_calculator.py


This is much easier to maintain than putting
everything into one Python file.
"""


# ============================================================
# 55. MODULES IN YOUR FUTURE PROJECTS
# ============================================================

"""
For your Python projects, you may eventually structure
your code like:

app/
|
|-- main.py
|
|-- database.py
|
|-- config.py
|
|-- models.py
|
|-- routes.py
|
|-- services.py
|
|-- utils.py


Each file can contain a specific responsibility.

This is very important when you start working with:

    Flask
    FastAPI
    PostgreSQL
    APIs
    Authentication
    AI applications
"""


# ============================================================
# 56. MODULE VS LIBRARY VS PACKAGE
# ============================================================

"""
These terms are often confused.

MODULE:

Usually a single Python file.

Example:

    calculator.py


PACKAGE:

A structured collection of modules/subpackages.

Example:

    myapp/
        calculator.py
        users.py


LIBRARY:

A broader term for reusable code distributed for
developers to use.

A library can contain multiple packages/modules.


FRAMEWORK:

A larger structure that provides an architecture and
controls much of the application's flow.

Examples:

    Django
    Flask
    FastAPI
"""


# ============================================================
# 57. INTERVIEW QUESTIONS
# ============================================================

"""
------------------------------------------------------------
Q1. What is a module in Python?
------------------------------------------------------------

ANSWER:

A module is a Python file containing reusable Python code,
such as functions, classes, and variables.


------------------------------------------------------------
Q2. Why do we use modules?
------------------------------------------------------------

ANSWER:

Modules improve code organization, reusability,
maintainability, and separation of functionality.


------------------------------------------------------------
Q3. How do you import a module?
------------------------------------------------------------

ANSWER:

Using:

    import module_name


Example:

    import math


------------------------------------------------------------
Q4. What is the difference between import and
from ... import?
------------------------------------------------------------

ANSWER:

    import math

requires:

    math.sqrt(25)


Whereas:

    from math import sqrt

allows:

    sqrt(25)


------------------------------------------------------------
Q5. What does import ... as do?
------------------------------------------------------------

ANSWER:

It creates an alias.

Example:

    import numpy as np

Then:

    np.array([1, 2, 3])


------------------------------------------------------------
Q6. What is a user-defined module?
------------------------------------------------------------

ANSWER:

A module created by the programmer.

Example:

    calculator.py


------------------------------------------------------------
Q7. What is a package?
------------------------------------------------------------

ANSWER:

A package is a way to organize related Python modules
and subpackages in a directory structure.


------------------------------------------------------------
Q8. Module vs Package?
------------------------------------------------------------

ANSWER:

Module:
    Usually one .py file.

Package:
    A directory structure used to organize modules
    and subpackages.


------------------------------------------------------------
Q9. What is pip?
------------------------------------------------------------

ANSWER:

pip is a package installer and package management tool
commonly used with Python.


------------------------------------------------------------
Q10. What is PyPI?
------------------------------------------------------------

ANSWER:

PyPI stands for Python Package Index.

It is a repository/index containing a large collection
of Python packages.


------------------------------------------------------------
Q11. pip vs PyPI?
------------------------------------------------------------

ANSWER:

PyPI is the package repository/index.

pip is the tool used to install and manage packages.


------------------------------------------------------------
Q12. How do you install a package?
------------------------------------------------------------

ANSWER:

    python -m pip install package_name


------------------------------------------------------------
Q13. How do you uninstall a package?
------------------------------------------------------------

ANSWER:

    python -m pip uninstall package_name


------------------------------------------------------------
Q14. How do you upgrade a package?
------------------------------------------------------------

ANSWER:

    python -m pip install --upgrade package_name


------------------------------------------------------------
Q15. How do you list installed packages?
------------------------------------------------------------

ANSWER:

    python -m pip list


------------------------------------------------------------
Q16. What is requirements.txt?
------------------------------------------------------------

ANSWER:

It is a file commonly used to record project dependencies
and their versions so they can be installed consistently.


------------------------------------------------------------
Q17. How do you install requirements.txt?
------------------------------------------------------------

ANSWER:

    python -m pip install -r requirements.txt


------------------------------------------------------------
Q18. What is a virtual environment?
------------------------------------------------------------

ANSWER:

A virtual environment is an isolated Python environment
used to keep project dependencies separate.


------------------------------------------------------------
Q19. Why use a virtual environment?
------------------------------------------------------------

ANSWER:

To prevent dependency and version conflicts between
different projects.


------------------------------------------------------------
Q20. How do you create a virtual environment?
------------------------------------------------------------

ANSWER:

    python -m venv venv


------------------------------------------------------------
Q21. What is __name__?
------------------------------------------------------------

ANSWER:

__name__ is a special module attribute.

When a file is executed directly, its value is generally:

    "__main__"

When imported, it normally has the module's name.


------------------------------------------------------------
Q22. Why use if __name__ == "__main__"?
------------------------------------------------------------

ANSWER:

To ensure certain code runs only when the file is
executed directly and not when the module is imported.


------------------------------------------------------------
Q23. What is dir()?
------------------------------------------------------------

ANSWER:

dir() returns a list of names available in an object
or module.


------------------------------------------------------------
Q24. What is sys.path?
------------------------------------------------------------

ANSWER:

sys.path contains locations Python searches when
importing modules.


------------------------------------------------------------
Q25. What is __pycache__?
------------------------------------------------------------

ANSWER:

It is a directory where Python may store cached
bytecode files.
"""


# ============================================================
# 58. RAPID-FIRE INTERVIEW REVISION
# ============================================================

"""
MODULE
    =
Python file containing reusable code


PACKAGE
    =
Organization of related modules


pip
    =
Python package installer / management tool


PyPI
    =
Python Package Index


requirements.txt
    =
Project dependency specification file


venv
    =
Virtual environment


import
    =
Import a module


from ... import
    =
Import specific members


as
    =
Create an alias


dir()
    =
Inspect available names


__name__
    =
Special module attribute


__main__
    =
Value of __name__ when file is executed directly


sys.path
    =
Module search locations


__pycache__
    =
Cached bytecode directory
"""


# ============================================================
# 59. MOST IMPORTANT COMMANDS TO REMEMBER
# ============================================================

"""
CREATE VIRTUAL ENVIRONMENT:

    python -m venv venv


ACTIVATE ON WINDOWS:

    venv\Scripts\activate


ACTIVATE ON MAC/LINUX:

    source venv/bin/activate


INSTALL PACKAGE:

    python -m pip install package


INSTALL SPECIFIC VERSION:

    python -m pip install package==1.0.0


UPGRADE:

    python -m pip install --upgrade package


UNINSTALL:

    python -m pip uninstall package


LIST PACKAGES:

    python -m pip list


PACKAGE INFORMATION:

    python -m pip show package


FREEZE DEPENDENCIES:

    python -m pip freeze


INSTALL REQUIREMENTS:

    python -m pip install -r requirements.txt


DEACTIVATE:

    deactivate
"""


# ============================================================
# 60. FINAL MEMORY MAP
# ============================================================

"""
                    PYTHON PROJECT
                          |
             +------------+------------+
             |                         |
          MODULES                   PACKAGES
             |                         |
        .py files              Collection / organization
             |
       +-----+-----+
       |           |
    Standard    User-defined
    Library     Modules
       |
       +---- math
       +---- os
       +---- sys
       +---- json
       +---- random


                  THIRD-PARTY
                      |
                      ↓
                     PyPI
                      |
                      ↓
                     pip
                      |
        +-------------+-------------+
        |             |             |
      install       upgrade      uninstall


                  PROJECT
                      |
                      ↓
             Virtual Environment
                      |
                      ↓
                    venv
                      |
                      ↓
             requirements.txt
"""
