"""
PYTHON TYPE ANNOTATIONS
====================

1. WHAT ARE TYPE ANNOTATIONS?
---------------------------
Type annotations are a way to specify the expected data type of a variable,
function parameter, or function return value.

In simple words, they tell developers what type of value a variable or
function is expected to work with.

2. WITHOUT TYPE ANNOTATIONS
---------------------------
Python does not explicitly show the expected types of a and b.

Example:

    def add(a, b):
        return a + b

    result = add(10, 20)
    print(result)

3. WITH TYPE ANNOTATIONS
------------------------
Example:

    def add(a: int, b: int) -> int:
        return a + b

    result = add(10, 20)
    print(result)

Meaning:
    a: int  -> a is expected to be an integer.
    b: int  -> b is expected to be an integer.
    -> int  -> the function is expected to return an integer.

4. VARIABLE TYPE ANNOTATIONS
----------------------------
Examples:

    name: str = "Harshad"
    age: int = 21
    salary: float = 25000.50
    is_student: bool = True

Common basic types:
    str   -> text/string
    int   -> integer/whole number
    float -> decimal number
    bool  -> True or False

5. FUNCTION TYPE ANNOTATIONS
----------------------------
Example:

    def greet(name: str) -> str:
        return "Hello " + name

    print(greet("Harshad"))

Here, name is expected to be a string and the function is expected to
return a string.

6. LIST TYPE ANNOTATIONS
------------------------
Example:

    marks: list[int] = [80, 90, 75]

This means marks is expected to be a list containing integers.

7. DOES PYTHON ENFORCE TYPE ANNOTATIONS?
----------------------------------------
No. Python does not automatically enforce type annotations at runtime.

Example:

    def add(a: int, b: int) -> int:
        return a + b

    print(add("Hello", "World"))

Output:
    HelloWorld

Even though int is specified, Python runs this code because type
annotations are generally hints, not runtime restrictions.

Tools such as MyPy and Pyright can check type annotations and report
potential type errors. Editors can also use them for autocomplete
and better code suggestions.

8. WHY ARE TYPE ANNOTATIONS USEFUL?
-----------------------------------
- Improve code readability.
- Help developers understand expected data types.
- Help identify potential errors with static type-checking tools.
- Provide better autocomplete and suggestions in IDEs.
- Make code easier to maintain, especially in large projects.



9. INTERVIEW ANSWER
--------------------
"Type annotations in Python are a way of specifying the expected data
types of variables, function parameters, and return values. They improve
code readability, maintainability, and error detection. Python does not
enforce them at runtime by default, but tools like MyPy and Pyright can
check them."

IMPORTANT:
----------
Type annotations describe expected types. They do not, by themselves,
force Python variables or function arguments to have those types.
"""