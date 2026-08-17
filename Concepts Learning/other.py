# ================================================================
#        PYTHON INTERVIEW CONCEPTS
# ================================================================
#
# TOPICS:
#   01. Mutable vs Immutable
#   02. is vs ==
#   03. Shallow Copy vs Deep Copy
#   04. Unpacking
#   05. Iterables vs Iterators
#   06. Generators and yield
#   07. map(), filter(), reduce()
#   08. sorted() vs list.sort()
#   09. key= in sorting
#   10. Exception Handling
#   11. Context Managers / with
#   12. Modules vs Packages
#   13. if __name__ == "__main__"
# ================================================================


# =================================================================
# 01. MUTABLE VS IMMUTABLE
# =================================================================

"""
INTERVIEW DEFINITION
--------------------

Mutable objects:
    Objects whose contents/state can be changed after creation.

Immutable objects:
    Objects whose contents/state cannot be changed after creation.

COMMON MUTABLE TYPES:
    list
    dict
    set
    bytearray

COMMON IMMUTABLE TYPES:
    int
    float
    bool
    str
    tuple
    frozenset
    bytes

IMPORTANT:
"Immutable" does NOT mean that a variable can never point to another
object.

Example:

    x = 10
    x = 20

The integer 10 was not changed. The variable x was simply made to
refer to another integer object.

WHY DOES THIS MATTER?
---------------------
This matters for:
    - function arguments
    - references
    - copying
    - dictionaries/sets
    - memory behavior
    - interview questions
"""


# Mutable example
numbers = [1, 2, 3]

numbers[0] = 100

print("Mutable list:", numbers)


# Immutable example
text = "Python"

# This would raise TypeError:
# text[0] = "J"

# Instead, a NEW string is created:
text = "J" + text[1:]

print("New string:", text)


# IMPORTANT REFERENCE EXAMPLE
a = [1, 2, 3]
b = a

b.append(4)

print("a:", a)
print("b:", b)

"""
Output:

a: [1, 2, 3, 4]
b: [1, 2, 3, 4]

Why?

a and b refer to the SAME list object.

Conceptually:

a ─────┐
       ├──> [1, 2, 3, 4]
b ─────┘
"""


# Immutable reference example
a = 10
b = a

b = 20

print("a:", a)
print("b:", b)

"""
a remains 10 because integers are immutable.

b is simply reassigned to another integer object.
"""


# FUNCTION EXAMPLE
def change_list(values):
    values.append(100)


numbers = [1, 2, 3]

change_list(numbers)

print("After function:", numbers)

"""
The list changed because the function received a reference to the
same mutable list object.
"""


def change_number(number):
    number += 100


number = 10

change_number(number)

print("After function:", number)

"""
number is still 10.

The operation number += 100 creates/rebinds an integer object.
It does not mutate the original integer.
"""


# INTERVIEW QUESTIONS
"""
Q: Is Python pass-by-value or pass-by-reference?

Best interview answer:

Python uses "pass-by-object-reference" (also called
call-by-sharing).

The function receives a reference to the same object.

If the object is mutable and we mutate it, the caller can observe
the mutation.

If we simply reassign the local parameter, the caller's variable
is not changed.

Example:

    def f(x):
        x.append(1)       # mutation -> caller sees it

    def g(x):
        x = [100]         # reassignment -> caller does not see it


Q: Is tuple immutable?

Yes, the tuple itself is immutable.

BUT a tuple can contain mutable objects.

Example:

    t = ([1, 2], 3)
    t[0].append(4)

This is allowed because we are mutating the list inside the tuple,
not changing the tuple's element reference.

Q: Why can an immutable object be a dictionary key?

Because dictionary keys must be hashable, and immutable objects
are generally hashable when their contents are hashable.
"""


# =================================================================
# 02. is VS ==
# =================================================================

"""
==  -> VALUE / EQUALITY COMPARISON
is  -> OBJECT IDENTITY COMPARISON

Use == when you want to know:
    "Do these objects have equal values?"

Use is when you want to know:
    "Are these two references pointing to the exact same object?"

NEVER use `is` as a general replacement for `==`.
"""


a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)
print("a is b:", a is b)

"""
True
False

Why?

The lists contain equal values, but they are two different objects.
"""


a = [1, 2, 3]
b = a

print("a == b:", a == b)
print("a is b:", a is b)

"""
True
True

Both variables refer to the same object.
"""


# BEST PRACTICE: use `is None`
value = None

if value is None:
    print("Value is None")


"""
Why use:

    value is None

instead of:

    value == None

Because None is a singleton object and identity is the intended
test.

Similarly, use:

    value is not None
"""


# id()
x = [1, 2]
y = x

print("id(x):", id(x))
print("id(y):", id(y))
print("x is y:", x is y)


"""
`id()` returns an integer identifying the object during its lifetime.

If:

    x is y

then both references point to the same object.
"""


# STRING / INTEGER TRAP
"""
You may sometimes see:

    a = 10
    b = 10
    print(a is b)

and get True.

Do NOT conclude that `is` should be used for integers.

Python may reuse/intern certain immutable objects.

The correct rule is:

    == -> compare values
    is -> compare identity

This is especially important in interviews.
"""


# =================================================================
# 03. SHALLOW COPY VS DEEP COPY
# =================================================================

"""
COPYING IS IMPORTANT WHEN WORKING WITH NESTED DATA.

Three different things must be understood:

1. Assignment
2. Shallow copy
3. Deep copy

ASSIGNMENT:
    b = a

No new outer object is created.

SHALLOW COPY:
    b = a.copy()
    b = list(a)
    b = a[:]
    copy.copy(a)

Creates a new outer object, but nested objects may still be shared.

DEEP COPY:
    copy.deepcopy(a)

Creates a new outer object AND recursively copies nested objects.
"""


# ASSIGNMENT
a = [[1, 2], [3, 4]]
b = a

b[0].append(100)

print("Assignment:")
print("a:", a)
print("b:", b)

"""
Both change because a and b point to the same outer list.
"""


# SHALLOW COPY
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

print("Same outer object:", a is b)
print("Same inner object:", a[0] is b[0])

b[0].append(100)

print("a:", a)
print("b:", b)

"""
Output concept:

Same outer object: False
Same inner object: True

Changing b[0] also changes a[0] because the inner list is shared.
"""


# SHALLOW COPY: changing an outer element
a = [[1, 2], [3, 4]]
b = a.copy()

b[0] = [100, 200]

print("a:", a)
print("b:", b)

"""
Here only b changes because b[0] is replaced in the new outer list.
"""


# DEEP COPY
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

print("Same outer object:", a is b)
print("Same inner object:", a[0] is b[0])

b[0].append(100)

print("a:", a)
print("b:", b)

"""
Now a remains unchanged.

Deep copy recursively creates independent nested objects.
"""


"""
INTERVIEW COMPARISON
--------------------

Assignment:
    b = a
    Same object
    No copy

Shallow copy:
    b = copy.copy(a)
    New outer object
    Nested objects may be shared

Deep copy:
    b = copy.deepcopy(a)
    New outer object
    Nested objects are recursively copied


COMMON SHALLOW COPY METHODS:
    a.copy()
    list(a)
    a[:]
    copy.copy(a)

IMPORTANT:
For dictionaries:
    d.copy()

For sets:
    s.copy()
"""


# =================================================================
# 04. UNPACKING
# =================================================================

"""
UNPACKING means extracting values from an iterable into variables.

Basic:

    a, b = [10, 20]

Python assigns:
    a = 10
    b = 20

The number of variables normally must match the number of values.
"""


a, b = [10, 20]

print(a)
print(b)


# Tuple unpacking
x, y, z = (1, 2, 3)

print(x, y, z)


# String unpacking
a, b, c = "cat"

print(a, b, c)


# Swap without temporary variable
a = 10
b = 20

a, b = b, a

print("a:", a)
print("b:", b)


"""
Python evaluates the right-hand side first and then performs the
assignments.

This is why:

    a, b = b, a

works safely.
"""


# STAR UNPACKING
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)


"""
first = 1
middle = [2, 3, 4]
last = 5

The starred variable collects remaining values into a LIST.
"""


# FIRST + REST
first, *rest = [10, 20, 30, 40]

print(first)
print(rest)


# REST + LAST
*start, last = [10, 20, 30, 40]

print(start)
print(last)


# FUNCTION ARGUMENT UNPACKING
def add(a, b, c):
    return a + b + c


values = [10, 20, 30]

print(add(*values))


"""
*values means:
    unpack the list into positional arguments.

Equivalent to:

    add(10, 20, 30)
"""


# DICTIONARY UNPACKING
def introduce(name, age):
    print(f"{name} is {age} years old.")


data = {
    "name": "Harshad",
    "age": 21
}

introduce(**data)

"""
**data unpacks dictionary keys as keyword arguments.
"""


# MERGING DICTIONARIES
a = {"name": "Harshad"}
b = {"age": 21}

merged = {**a, **b}

print(merged)


"""
Python 3.9+ also supports:

    merged = a | b

for dictionary union.
"""


# UNPACKING IN LOOPS
pairs = [(1, 2), (3, 4), (5, 6)]

for x, y in pairs:
    print(x, y)


# INTERVIEW QUESTION
"""
Q: What is the difference between *args and **kwargs?

*args:
    Collects extra positional arguments into a tuple.

**kwargs:
    Collects extra keyword arguments into a dictionary.

Example:

    def test(*args, **kwargs):
        print(args)
        print(kwargs)

    test(1, 2, name="Harshad")

args:
    (1, 2)

kwargs:
    {'name': 'Harshad'}
"""


# =================================================================
# 05. ITERABLES VS ITERATORS
# =================================================================

"""
ITERABLE
--------

An iterable is an object from which we can obtain an iterator.

Examples:
    list
    tuple
    string
    set
    dictionary
    range

We can generally use them in:

    for x in iterable:
        ...


ITERATOR
--------

An iterator is an object that produces values one at a time.

It implements:
    __iter__()
    __next__()

When there are no more values, next() raises:
    StopIteration
"""


numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# The next call would raise StopIteration:
# print(next(iterator))


# ITERABLE -> ITERATOR
numbers = [1, 2, 3]

it = iter(numbers)

print("Iterator object:", it)


"""
A list is iterable.

The iterator returned by iter(list) keeps track of the current
position.
"""


# FOR LOOP INTERNAL IDEA
numbers = [10, 20, 30]

for number in numbers:
    print(number)


"""
Conceptually, Python does something similar to:

    iterator = iter(numbers)

    while True:
        try:
            number = next(iterator)
        except StopIteration:
            break

        print(number)
"""


# CUSTOM ITERATOR
class CountUpTo:

    def __init__(self, maximum):
        self.current = 1
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.maximum:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


counter = CountUpTo(5)

for number in counter:
    print(number)


"""
IMPORTANT INTERVIEW POINT:

An iterator is also an iterable because it implements __iter__()
and returns itself.

But not every iterable is an iterator.

Example:
    list -> iterable
    iter(list) -> iterator
"""


# INTERVIEW COMPARISON
"""
Iterable:
    Can provide an iterator.
    Examples: list, tuple, string, set, dict, range.

Iterator:
    Produces one value at a time.
    Has __next__().
    Keeps track of iteration state.

iter(obj):
    Returns an iterator.

next(iterator):
    Returns the next value.

StopIteration:
    Signals that iteration is finished.
"""


# =================================================================
# 06. GENERATORS AND yield
# =================================================================

"""
A GENERATOR is a special type of iterator.

A generator function contains `yield`.

When called, it does NOT execute the entire function immediately.
It returns a generator object.

Each next() resumes execution from where the previous yield stopped.

MAIN ADVANTAGE:
    Lazy evaluation.

The values are generated only when needed.

This can save memory for large data.
"""


def simple_generator():
    yield 1
    yield 2
    yield 3


g = simple_generator()

print(type(g))

print(next(g))
print(next(g))
print(next(g))


# FOR LOOP
for value in simple_generator():
    print(value)


# GENERATOR WITH LOOP
def count_numbers(n):

    for i in range(1, n + 1):
        yield i


for number in count_numbers(5):
    print(number)


"""
Normal function:

    return

ends the function and sends one result back.

Generator:

    yield

pauses the function and preserves its state.

Calling next() resumes execution.
"""


# RETURN VS YIELD
def normal_function():
    return [1, 2, 3]


def generator_function():
    yield 1
    yield 2
    yield 3


print(normal_function())
print(generator_function())


"""
normal_function() immediately creates/returns a list.

generator_function() returns a generator object.

The generator produces values lazily.
"""


# GENERATOR EXPRESSION
squares = (x * x for x in range(5))

for value in squares:
    print(value)


"""
List comprehension:

    [x*x for x in range(5)]

creates a list immediately.

Generator expression:

    (x*x for x in range(5))

creates values lazily.
"""


# MEMORY IDEA
"""
For a very large sequence:

    [x*x for x in range(1000000)]

stores all generated results in a list.

A generator:

    (x*x for x in range(1000000))

generates values when requested.

Generators are therefore useful for:
    - large files
    - large sequences
    - data pipelines
    - streaming
    - memory-efficient processing
"""


# IMPORTANT GENERATOR PROPERTY
g = (x for x in range(3))

print(next(g))
print(next(g))
print(next(g))

# next(g) now raises StopIteration


"""
A generator is exhausted after its values have been consumed.

To iterate again, create a new generator.
"""


# INTERVIEW QUESTIONS
"""
Q: What is yield?

A:
yield produces a value from a generator and pauses its execution.
When resumed, execution continues from the same point.

Q: return vs yield?

return:
    ends the function.

yield:
    pauses the generator and preserves its state.

Q: Why use generators?

A:
For lazy, memory-efficient processing, especially with large or
streaming data.

Q: Is a generator an iterator?

A:
Yes. Generator objects implement the iterator protocol.
"""


# =================================================================
# 07. map(), filter(), reduce()
# =================================================================

"""
map()
-----

Applies a function to every element.

    map(function, iterable)

It returns a map iterator in Python 3.


filter()
--------

Keeps elements for which a condition is True.

    filter(function, iterable)

It returns a filter iterator.


reduce()
--------

Repeatedly combines elements into one final result.

    reduce(function, iterable)

reduce is available from:

    functools
"""


# MAP
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))


"""
[2, 4, 6, 8, 10]
"""


# MAP WITHOUT LAMBDA
def square(x):
    return x * x


numbers = [1, 2, 3, 4]

print(list(map(square, numbers)))


# FILTER
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))


# FILTER WITH FUNCTION
def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, numbers)))


# REDUCE
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print(total)


"""
Process:

1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
"""


# REDUCE FOR PRODUCT
product = reduce(lambda a, b: a * b, numbers)

print(product)


# INITIAL VALUE
total = reduce(
    lambda a, b: a + b,
    numbers,
    100
)

print(total)

"""
Starts with:

100 + 1 + 2 + 3 + 4 + 5
"""


"""
INTERVIEW COMPARISON
--------------------

map:
    transform every item

filter:
    select some items

reduce:
    combine items into one result


Example:

    numbers = [1,2,3,4,5]

    map    -> [2,4,6,8,10]
    filter -> [2,4]
    reduce -> one final value


IMPORTANT:
In modern Python, list comprehensions are often more readable
than map/filter for simple operations.

Example:

    [x * 2 for x in numbers]

is often clearer than:

    list(map(lambda x: x * 2, numbers))
"""


# =================================================================
# 08. sorted() VS list.sort()
# =================================================================

"""
sorted()
--------

Built-in function.

Returns a NEW sorted list.

Works with many iterables.

Example:

    sorted([3,1,2])


list.sort()
-----------

List method.

Sorts the ORIGINAL list in-place.

Returns None.

Only available for lists.
"""


numbers = [4, 1, 3, 2]

result = sorted(numbers)

print("Original:", numbers)
print("Sorted:", result)


numbers = [4, 1, 3, 2]

result = numbers.sort()

print("numbers:", numbers)
print("return value:", result)

"""
numbers.sort() returns None.
"""


# DESCENDING
numbers = [4, 1, 3, 2]

print(sorted(numbers, reverse=True))

numbers.sort(reverse=True)

print(numbers)


# sorted() WORKS WITH OTHER ITERABLES
text = "python"

print(sorted(text))

"""
Returns:

['h', 'n', 'o', 'p', 't', 'y']

Because sorted() returns a list.
"""


# SORTING TUPLE
values = (3, 1, 2)

print(sorted(values))

"""
Returns a list.
"""


"""
INTERVIEW TABLE

                 sorted()          list.sort()
------------------------------------------------
Type             function          list method
New list         Yes               No
Original         unchanged        modified
Return value     sorted list       None
Works on tuple   Yes               No
Works on string  Yes               No
reverse=         Yes               Yes
key=             Yes               Yes

Time complexity:
    Python's list sorting uses Timsort.
    Typical/worst-case sorting complexity is O(n log n).
    It can be O(n) on some already/nearly ordered inputs.
"""


# =================================================================
# 09. key= IN SORTING
# =================================================================

"""
The `key` parameter tells Python what value should be used for
comparison while sorting.

Syntax:

    sorted(iterable, key=function)

or:

    list.sort(key=function)

IMPORTANT:
The key function is used to calculate a comparison key for each
element. Python then sorts based on those keys.
"""


# SORT BY LENGTH
words = ["python", "is", "very", "easy"]

result = sorted(words, key=len)

print(result)


# SORT BY LAST CHARACTER
words = ["apple", "banana", "mango", "kiwi"]

result = sorted(words, key=lambda word: word[-1])

print(result)


# SORT TUPLES BY SECOND ELEMENT
students = [
    ("Rahul", 80),
    ("Harshad", 95),
    ("Sanjay", 70)
]

result = sorted(students, key=lambda student: student[1])

print(result)


# DESCENDING SCORE
result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(result)


# SORT DICTIONARY ITEMS BY VALUE
marks = {
    "Rahul": 80,
    "Harshad": 95,
    "Sanjay": 70
}

result = sorted(
    marks.items(),
    key=lambda item: item[1]
)

print(result)


# SORT BY MULTIPLE CRITERIA
students = [
    ("Rahul", 80),
    ("Harshad", 80),
    ("Sanjay", 70),
    ("Akash", 80)
]

result = sorted(
    students,
    key=lambda student: (student[1], student[0])
)

print(result)

"""
Sort first by marks.
If marks are equal, sort by name.

This is extremely useful in coding interviews.
"""


"""
IMPORTANT INTERVIEW POINT:
Python's sorting is STABLE.

If two elements have equal keys, their original relative order
is preserved.

Example:

    data = [
        ("A", 90),
        ("B", 80),
        ("C", 90)
    ]

Sorting by score keeps A before C because both have score 90 and
A originally appeared first.
"""


# =================================================================
# 10. EXCEPTION HANDLING
# =================================================================

"""
An exception is an event that occurs during program execution and
interrupts the normal flow of the program.

Examples:
    ZeroDivisionError
    ValueError
    TypeError
    IndexError
    KeyError
    FileNotFoundError
    NameError
    AttributeError

Exception handling allows us to handle expected runtime errors
gracefully instead of crashing the program.
"""


# BASIC TRY / EXCEPT
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# VALUEERROR
try:
    number = int("abc")
except ValueError:
    print("Invalid integer.")


# MULTIPLE EXCEPTIONS
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# GENERIC EXCEPTION
try:
    x = 10 / 0
except Exception as e:
    print("Error:", e)


"""
INTERVIEW WARNING:

Avoid blindly using:

    except Exception:

when you know the exact exception you expect.

Prefer specific exceptions:

    except ValueError:
    except ZeroDivisionError:

Specific exception handling makes programs clearer and safer.
"""


# try / except / else
try:
    number = int("100")

except ValueError:
    print("Invalid number.")

else:
    print("Conversion successful:", number)


"""
else runs ONLY when no exception occurred.
"""


# try / except / finally
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Division error.")

finally:
    print("This always executes.")


"""
finally normally executes whether an exception occurred or not.

It is commonly used for cleanup.
"""


# try / except / else / finally
try:
    number = int("10")

except ValueError:
    print("Invalid value.")

else:
    print("Success:", number)

finally:
    print("Finished.")


# RAISE
def set_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


try:
    print(set_age(-5))
except ValueError as e:
    print("Error:", e)


"""
`raise` allows us to explicitly create an exception when a condition
is invalid.
"""


# CUSTOM EXCEPTION
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    return balance - amount


try:
    print(withdraw(1000, 1500))
except InsufficientBalanceError as e:
    print(e)


"""
Custom exceptions are useful when creating applications where
domain-specific errors need meaningful names.
"""


"""
EXCEPTION HIERARCHY IDEA
------------------------

BaseException
    |
    +-- Exception
          |
          +-- ArithmeticError
          |      +-- ZeroDivisionError
          |
          +-- LookupError
          |      +-- IndexError
          |      +-- KeyError
          |
          +-- ValueError
          +-- TypeError
          +-- OSError
                 +-- FileNotFoundError
                 ...


Most application errors should inherit from Exception,
not directly from BaseException.
"""


"""
IMPORTANT:
Do NOT use exceptions for normal control flow when a normal
condition check is clearer.

Also remember:
Syntax errors are different from runtime exceptions.

SyntaxError:
    Python cannot parse the code.

Exception:
    The code parsed successfully but something went wrong while
    executing it.
"""


# =================================================================
# 11. CONTEXT MANAGERS / with
# =================================================================

"""
A context manager manages setup and cleanup around a block of code.

The `with` statement is the common way to use a context manager.

Classic example:

    with open("file.txt") as file:
        data = file.read()

The context manager ensures that the file is properly closed,
including when an exception occurs.
"""


# FILE EXAMPLE
# This creates a temporary file for demonstration.
with open("interview_demo.txt", "w") as file:
    file.write("Python Context Manager")


with open("interview_demo.txt", "r") as file:
    print(file.read())


"""
Without `with`, you would need:

    file = open(...)
    try:
        ...
    finally:
        file.close()

The `with` statement handles cleanup automatically.
"""


# CONTEXT MANAGER PROTOCOL
"""
A context manager normally implements:

    __enter__()
    __exit__()

Example:

    class MyContext:

        def __enter__(self):
            # setup
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            # cleanup
            pass


The `with` statement roughly does:

    manager = MyContext()

    value = manager.__enter__()

    try:
        ...
    finally:
        manager.__exit__(...)
"""


# CUSTOM CONTEXT MANAGER
class DemoContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with DemoContext():
    print("Inside context")


"""
Output:

Entering context
Inside context
Exiting context
"""


# __exit__ CAN SEE EXCEPTIONS
class ExceptionContext:

    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_value, traceback):

        print("Exit")

        if exc_type is not None:
            print("Exception occurred:", exc_value)

        # Returning False/None means the exception is NOT suppressed.
        return False


try:
    with ExceptionContext():
        raise ValueError("Something went wrong")
except ValueError:
    print("Exception reached outside.")


"""
__exit__ receives:

    exc_type
    exc_value
    traceback

If __exit__ returns True, the exception can be suppressed.

Usually you should NOT suppress exceptions unless that is intentional.
"""


# contextlib.contextmanager
from contextlib import contextmanager


@contextmanager
def demo():

    print("Setup")

    try:
        yield
    finally:
        print("Cleanup")


with demo():
    print("Work")


"""
The @contextmanager decorator lets us create a context manager
using a generator-style function.

Code before yield:
    setup

yield:
    gives control to the with block

code after yield:
    cleanup
"""


"""
INTERVIEW QUESTIONS
-------------------

Q: Why use with open(...)?

A:
It ensures resource cleanup, especially file closing, even if an
exception occurs.

Q: What is a context manager?

A:
An object that defines behavior for entering and exiting a context,
typically through __enter__ and __exit__.

Q: What is __enter__?

A:
Called when entering the with block.

Q: What is __exit__?

A:
Called when leaving the with block, including during exception
handling.

Common uses:
    files
    database connections
    locks
    network resources
    temporary resources
"""


# =================================================================
# 12. MODULES VS PACKAGES
# =================================================================

"""
MODULE
------

A module is usually a single Python file (.py) containing Python
code such as functions, classes, variables, and statements.

Example:

    calculator.py

    def add(a, b):
        return a + b


PACKAGE
-------

A package is a directory used to organize related Python modules.

Example:

    mypackage/
        __init__.py
        calculator.py
        geometry.py

Modern Python also supports namespace packages that do not
necessarily require __init__.py, but understanding __init__.py is
still important for traditional packages and interviews.
"""


# MODULE EXAMPLE
"""
Suppose you have:

math_utils.py

    def add(a, b):
        return a + b

Then another file can do:

    import math_utils

    print(math_utils.add(10, 20))
"""


# DIFFERENT IMPORT STYLES
"""
1.

    import math

    math.sqrt(25)


2.

    from math import sqrt

    sqrt(25)


3.

    from math import sqrt, factorial


4.

    import math as m

    m.sqrt(25)
"""


"""
BEST PRACTICE:
Prefer clear imports.

For example:

    import math

is often clearer than importing many individual names.

Avoid wildcard imports:

    from math import *

because they can pollute the namespace and make code harder to
understand.
"""


# __init__.py
"""
Traditional package structure:

    mypackage/
        __init__.py
        calculator.py
        converter.py

__init__.py can:
    - mark a directory as a traditional Python package
    - run package initialization code
    - expose selected names
    - define package metadata

Example:

    from .calculator import add
"""


# RELATIVE IMPORT
"""
Inside a package:

    from .calculator import add

The dot means:
    current package.

Parent package can use:
    from ..something import x

Relative imports are mainly used inside packages.
"""


# PYTHON MODULE SEARCH PATH
"""
When importing a module, Python searches locations based on its
module search path, available through:

    import sys
    print(sys.path)

This helps explain why Python sometimes says:

    ModuleNotFoundError
"""


# MODULE VS PACKAGE INTERVIEW ANSWER
"""
Module:
    Usually one .py file.

Package:
    A directory that organizes modules/subpackages.

Example:

    project/
        main.py
        utils/
            __init__.py
            math_utils.py
            string_utils.py

Here:
    main.py          -> module
    math_utils.py    -> module
    string_utils.py  -> module
    utils             -> package
"""


# =================================================================
# 13. if __name__ == "__main__"
# =================================================================

"""
This is one of the MOST IMPORTANT Python interview concepts.

Every Python module has a special built-in variable:

    __name__

When a file is run directly:

    python file.py

Python sets:

    __name__ == "__main__"

When the file is imported:

    import file

Python sets:

    __name__ == "file"

(or the module's actual import name)


WHY IS THIS USED?
-----------------

It allows us to keep code that should run only when the file is
executed directly, rather than when it is imported.
"""


# EXAMPLE
"""
Suppose calculator.py contains:

    def add(a, b):
        return a + b


    def main():
        print(add(10, 20))


    if __name__ == "__main__":
        main()


If you run:

    python calculator.py

then:

    __name__ == "__main__"

so main() executes.


If another file does:

    import calculator

then:

    __name__ == "calculator"

so main() does NOT execute automatically.
"""


# DEMONSTRATION IN THIS FILE
def demo_function():
    return "Function executed."


def main():
    print(demo_function())


if __name__ == "__main__":
    main()


"""
This is the standard pattern for making a Python file both:

1. Importable as a module
2. Executable as a script


INTERVIEW ANSWER:

`if __name__ == "__main__":` is used to define code that should
execute only when the module is run directly, not when it is
imported into another module.
"""


# WHY THIS IS IMPORTANT IN PROJECTS
"""
Without the guard:

    print("Running program")

at the top level would execute whenever the module is imported.

With:

    if __name__ == "__main__":
        print("Running program")

it executes only when that file is run directly.

This is useful for:
    - testing
    - command-line programs
    - reusable modules
    - project entry points
"""


# =================================================================
#                  QUICK INTERVIEW REVISION
# =================================================================

"""
===============================================================
01. MUTABLE VS IMMUTABLE
===============================================================

Mutable:
    list, dict, set

Immutable:
    int, float, bool, str, tuple, frozenset

Key idea:
    Mutation changes an existing object.
    Reassignment changes what a variable refers to.


===============================================================
02. is VS ==
===============================================================

==:
    value equality

is:
    object identity

Use:
    x is None

Do not use:
    x is 10
    x is "hello"

when you mean value comparison.


===============================================================
03. SHALLOW VS DEEP COPY
===============================================================

Assignment:
    same object

Shallow:
    new outer object
    nested objects may be shared

Deep:
    recursively independent copy


===============================================================
04. UNPACKING
===============================================================

a, b = [1, 2]

*args:
    positional argument collection

**kwargs:
    keyword argument collection

*a:
    iterable unpacking

**d:
    dictionary unpacking


===============================================================
05. ITERABLE VS ITERATOR
===============================================================

Iterable:
    can produce an iterator

Iterator:
    implements __next__()
    produces values one at a time

iter(obj):
    creates/gets iterator

next(it):
    gets next value


===============================================================
06. GENERATOR
===============================================================

Generator uses yield.

Benefits:
    lazy evaluation
    memory efficiency
    one value at a time

Generator is an iterator.


===============================================================
07. map/filter/reduce
===============================================================

map:
    transform

filter:
    select

reduce:
    combine


===============================================================
08. sorted vs sort
===============================================================

sorted():
    returns new list
    does not modify original

list.sort():
    modifies original
    returns None


===============================================================
09. key=
===============================================================

Controls what value is used for sorting.

Examples:

    sorted(words, key=len)

    sorted(students, key=lambda x: x[1])


===============================================================
10. EXCEPTIONS
===============================================================

try:
except:
else:
finally:
raise

Specific exceptions are preferred over overly broad handling.


===============================================================
11. CONTEXT MANAGER
===============================================================

with:

    setup
    work
    cleanup

Common example:

    with open(...) as file:


===============================================================
12. MODULE VS PACKAGE
===============================================================

Module:
    usually one .py file

Package:
    directory organizing modules


===============================================================
13. __name__
===============================================================

Direct execution:

    __name__ == "__main__"

Imported:

    __name__ == module_name

Use:

    if __name__ == "__main__":
        main()


# =================================================================
#                  RAPID-FIRE INTERVIEW QUESTIONS
# =================================================================
"""
"""
1. What is mutability?

2. Give examples of mutable and immutable types.

3. Is tuple mutable?

4. Can a tuple contain a mutable object?

5. What is the difference between == and is?

6. Why should `is` be used with None?

7. What is object identity?

8. What does id() return?

9. What is assignment vs shallow copy?

10. What is shallow copy?

11. What is deep copy?

12. Why does shallow copying nested lists sometimes cause problems?

13. What is unpacking?

14. What does * do in unpacking?

15. What does ** do in dictionary unpacking?

16. What are *args and **kwargs?

17. What is an iterable?

18. What is an iterator?

19. What does iter() do?

20. What does next() do?

21. What is StopIteration?

22. Is a list an iterator?

23. Is a list iterable?

24. What is a generator?

25. What is yield?

26. Difference between return and yield?

27. Why are generators memory efficient?

28. What does map() do?

29. What does filter() do?

30. What does reduce() do?

31. Where does reduce come from?

32. Difference between sorted() and sort()?

33. What does sort() return?

34. What is the key parameter?

35. Is Python sorting stable?

36. What is an exception?

37. Difference between SyntaxError and runtime exception?

38. Difference between ValueError and TypeError?

39. What does finally do?

40. What does else do in try/except?

41. What does raise do?

42. Why create custom exceptions?

43. What is a context manager?

44. Why use with open(...)?

45. What are __enter__ and __exit__?

46. What is a module?

47. What is a package?

48. What is __init__.py?

49. What is an import?

50. What is __name__?

51. What does __name__ contain when a file is executed directly?

52. What does __name__ contain when imported?

53. Why use if __name__ == "__main__"?

54. Can a Python file be both imported and executed directly?

55. Why is this pattern useful in real projects?

"""
# =================================================================
#                         FINAL ADVICE
# =================================================================

"""
For interviews, don't answer only with definitions.

A strong answer has this structure:

1. Definition
2. Simple example
3. Difference / why it matters
4. Real-world or DSA use case
5. Complexity when relevant

Example:

Interviewer:
    "What is a generator?"

Weak answer:
    "Generator uses yield."

Strong answer:
    "A generator is a type of iterator that produces values lazily
     using yield. Unlike a list, it doesn't store all generated
     values in memory at once. Each call to next() resumes execution
     from where the previous yield stopped. It is useful for large
     sequences, files, and streaming data."


IMPORTANT FOR YOUR DSA JOURNEY
------------------------------

The most useful topics from this file for DSA are:

    Mutable / Immutable
        ↓
    References / Copying
        ↓
    Unpacking
        ↓
    Iterables / Iterators
        ↓
    Sorting + key=
        ↓
    Hashing-related behavior
        ↓
    Exceptions / clean code
        ↓
    Modules / reusable code

You do NOT need to memorize every internal implementation detail
before starting DSA.

Understand the concepts, write the examples yourself, and then
move into problem solving.
"""

print("=" * 70)
print("13 PYTHON INTERVIEW CONCEPTS - REVISION COMPLETE")
print("=" * 70)
