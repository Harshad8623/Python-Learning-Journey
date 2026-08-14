# ============================================================
# 1. WHAT IS VARIABLE SCOPE?
# ============================================================

"""
Scope means:

"Where can I access this variable?"

Python mainly has these scopes:

1. Local
2. Enclosing
3. Global
4. Built-in

This is called the LEGB rule:

L -> Local
E -> Enclosing
G -> Global
B -> Built-in
"""


# ============================================================
# 2. GLOBAL VARIABLE
# ============================================================

"""
A variable created outside a function is generally
a GLOBAL variable.

It can be accessed from different functions
within the same module.
"""

name = "Rahul"


def greet():

    print(name)


greet()

# Output:
# Rahul


# The global variable can also be accessed outside
# the function.

print(name)


# ============================================================
# 3. LOCAL VARIABLE
# ============================================================

"""
A variable created inside a function is generally
a LOCAL variable.

It can normally be accessed only inside that function.
"""

def greet():

    message = "Hello"

    print(message)


greet()


# This will cause NameError because message is local
# to greet().
#
# print(message)


# ============================================================
# 4. YOUR EXAMPLE - GLOBAL + LOCAL
# ============================================================

name = "Rahul"


def greet():

    message = "Hello"   # Local variable

    print(f"{message}, {name}!")


greet()

# message -> Local variable
# name    -> Global variable


# This will give NameError:
#
# print(message)


# But this is valid:
print(name)


# ============================================================
# 5. LOCAL VARIABLE WITH SAME NAME AS GLOBAL
# ============================================================

name = "Rahul"


def greet():

    name = "Harshad"

    print(name)


greet()

print(name)


"""
Output:

Harshad
Rahul

Why?

Inside greet():

    name = "Harshad"

creates a LOCAL variable.

It does not change the GLOBAL name.

So:

Global name -> Rahul
Local name  -> Harshad
"""


# ============================================================
# 6. GLOBAL VARIABLE IS NOT CHANGED BY LOCAL VARIABLE
# ============================================================

count = 10


def test():

    count = 20

    print("Inside function:", count)


test()

print("Outside function:", count)


"""
Output:

Inside function: 20
Outside function: 10
"""


# ============================================================
# 7. READING A GLOBAL VARIABLE INSIDE FUNCTION
# ============================================================

name = "Rahul"


def greet():

    # We can READ the global variable
    # without using the global keyword.

    print(name)


greet()


# IMPORTANT:
#
# You DO NOT need:
#
# global name
#
# just to read name.


# ============================================================
# 8. MODIFYING A GLOBAL VARIABLE
# ============================================================

count = 10


def increase():

    global count

    count = count + 1


increase()

print(count)

# Output:
# 11


"""
Here global is required because we are
REASSIGNING the global variable.

Without global:

def increase():
    count = count + 1

Python will treat count as a local variable
and you will get an error because count is being
read before it has a local value.
"""


# ============================================================
# 9. WHY global IS REQUIRED
# ============================================================

count = 10


def test():

    # Python treats count as LOCAL because
    # we are assigning a value to it.

    # count = count + 1
    #
    # This causes:
    # UnboundLocalError


    pass


# ============================================================
# 10. CORRECT WAY USING global
# ============================================================

count = 10


def test():

    global count

    count = count + 1


test()

print(count)


# ============================================================
# 11. YOUR SECOND EXAMPLE
# ============================================================

name = "Rahul"


def greet():

    global message

    message = "Hello"

    print(f"{message}, {name}!")


greet()

print(message)


"""
This works because:

global message

tells Python that message refers to
a GLOBAL variable.

The variable is created/assigned in the global scope.

However, this style is generally NOT recommended
for normal programs.

Better practice is usually to return a value.
"""


# ============================================================
# 12. BETTER APPROACH - RETURN VALUE
# ============================================================

name = "Rahul"


def greet():

    message = "Hello"

    return message


message = greet()

print(message)


"""
Returning values is generally better than creating
global variables from inside functions.

Why?

Because global variables can make programs:

- harder to understand
- harder to debug
- harder to test
- harder to maintain
"""


# ============================================================
# 13. GLOBAL LIST - IMPORTANT CONCEPT
# ============================================================

"""
There is an important difference between:

1. Modifying an object
2. Reassigning a variable
"""


numbers = [1, 2, 3]


def add_number():

    # We can MODIFY the global list
    # without using global.

    numbers.append(4)


add_number()

print(numbers)

# Output:
# [1, 2, 3, 4]


# ============================================================
# 14. MODIFYING VS REASSIGNING
# ============================================================

numbers = [1, 2, 3]


def modify_list():

    numbers.append(4)    # Modification is allowed


modify_list()

print(numbers)


# But this is REASSIGNMENT:

numbers = [1, 2, 3]


def replace_list():

    global numbers

    numbers = [10, 20, 30]


replace_list()

print(numbers)


"""
Remember:

numbers.append(4)
    -> modifies existing object

numbers = [10, 20, 30]
    -> reassigns variable

global is needed for reassignment.
"""


# ============================================================
# 15. LOCAL VARIABLE SHADOWING GLOBAL VARIABLE
# ============================================================

x = 100


def test():

    x = 200

    print("Local x:", x)


test()

print("Global x:", x)


"""
Output:

Local x: 200
Global x: 100

The local variable shadows the global variable
inside the function.
"""


# ============================================================
# 16. ACCESSING GLOBAL VARIABLE USING globals()
# ============================================================

name = "Rahul"


def test():

    print(globals()["name"])


test()

# Output:
# Rahul


"""
globals() returns a dictionary representing
the global namespace.

This is useful to know for interviews,
but you normally don't need to use it
in everyday programming.
"""


# ============================================================
# 17. LOCAL SCOPE
# ============================================================

def test():

    a = 10
    b = 20

    print(a)
    print(b)


test()


# a and b cannot normally be accessed here.
#
# print(a)
# print(b)


# ============================================================
# 18. FUNCTION PARAMETERS ARE LOCAL VARIABLES
# ============================================================

def greet(name):

    # name is a LOCAL variable/parameter

    print("Hello", name)


greet("Harshad")


# name does not exist outside this function
# unless another variable called name exists.


# ============================================================
# 19. LOCAL VARIABLES IN DIFFERENT FUNCTIONS
# ============================================================

def function1():

    x = 10

    print("Function 1:", x)


def function2():

    x = 20

    print("Function 2:", x)


function1()
function2()


"""
Both functions have their own local x.

Function 1 -> x = 10
Function 2 -> x = 20

They do not interfere with each other.
"""


# ============================================================
# 20. ENCLOSING SCOPE
# ============================================================

"""
Enclosing scope occurs when one function is
defined inside another function.

The inner function can access variables
from the outer function.
"""

def outer():

    message = "Hello"

    def inner():

        print(message)

    inner()


outer()


# ============================================================
# 21. ENCLOSING SCOPE EXAMPLE
# ============================================================

def outer():

    x = 100

    def inner():

        print(x)

    inner()


outer()


# ============================================================
# 22. nonlocal KEYWORD
# ============================================================

"""
nonlocal is used when an INNER function wants
to MODIFY a variable belonging to the
OUTER function.
"""


def outer():

    count = 0

    def inner():

        nonlocal count

        count = count + 1

        print(count)

    inner()
    inner()
    inner()


outer()

"""
Output:

1
2
3
"""


# ============================================================
# 23. global VS nonlocal
# ============================================================

"""
global
------------------------------------------------
Used to access/reassign a variable in GLOBAL scope.

nonlocal
------------------------------------------------
Used to access/reassign a variable in an
ENCLOSING (outer function) scope.

Example:

x = 10

def outer():

    y = 20

    def inner():

        global x
        nonlocal y

"""


# ============================================================
# 24. LEGB RULE
# ============================================================

"""
Python searches for a variable in this order:

L -> Local
E -> Enclosing
G -> Global
B -> Built-in


Example:

x = "Global"


def outer():

    x = "Enclosing"

    def inner():

        x = "Local"

        print(x)

    inner()


outer()


Python finds:

Local x first.

Therefore output:

Local
"""


# ============================================================
# 25. LEGB EXAMPLE
# ============================================================

x = "Global"


def outer():

    x = "Enclosing"

    def inner():

        print(x)

    inner()


outer()

"""
Output:

Enclosing

Why?

There is no Local x inside inner(),
so Python checks Enclosing scope.
"""


# ============================================================
# 26. LEGB - GLOBAL
# ============================================================

x = "Global"


def outer():

    def inner():

        print(x)

    inner()


outer()

"""
Python searches:

Local      -> not found
Enclosing  -> not found
Global     -> found

Output:

Global
"""


# ============================================================
# 27. LEGB - BUILT-IN
# ============================================================

"""
If Python doesn't find a variable in:

Local
Enclosing
Global

it searches Built-in scope.

Examples of built-in functions:

len()
print()
sum()
max()
min()
type()
"""


def test():

    # len is found in built-in scope

    print(len([1, 2, 3]))


test()


# ============================================================
# 28. GLOBAL KEYWORD - IMPORTANT INTERVIEW EXAMPLE
# ============================================================

score = 0


def increase_score():

    global score

    score += 10


increase_score()
increase_score()
increase_score()

print(score)

# Output:
# 30


# ============================================================
# 29. WITHOUT GLOBAL
# ============================================================

score = 0


def test():

    # This would cause UnboundLocalError:
    #
    # score += 10

    pass


# ============================================================
# 30. BEST PRACTICE
# ============================================================

"""
Avoid unnecessary global variables.

BAD STYLE:

total = 0


def add():
    global total
    total += 10


Better:

def add(total):
    return total + 10


total = 0

total = add(total)

print(total)


Returning values makes functions easier to:

- Understand
- Test
- Debug
- Reuse
"""


# ============================================================
# 31. PRACTICAL EXAMPLE - BETTER DESIGN
# ============================================================

def calculate_total(price, tax):

    total = price + tax

    return total


result = calculate_total(1000, 180)

print("Total:", result)


# ============================================================
# 32. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a local variable?

A variable created inside a function and normally
accessible only within that function.


Q2. What is a global variable?

A variable defined outside functions and available
in the global scope.


Q3. Can a function read a global variable?

Yes.

Example:

x = 10

def test():
    print(x)


Q4. Can a function modify a global variable?

Yes, but when REASSIGNING it, use global.

Example:

x = 10

def test():
    global x
    x = 20


Q5. Is global required to read a global variable?

NO.


Q6. Is global required to modify a mutable global object?

Not necessarily.

Example:

numbers = [1, 2]

def test():
    numbers.append(3)


Q7. What is LEGB?

L -> Local
E -> Enclosing
G -> Global
B -> Built-in


Q8. What is nonlocal?

It allows an inner function to modify a variable
from its enclosing/outer function.


Q9. global vs nonlocal?

global  -> Global scope
nonlocal -> Enclosing scope


Q10. What is variable shadowing?

When a local variable has the same name as a
global variable, the local variable takes precedence
inside that function.
"""


# ============================================================
# 33. QUICK REVISION
# ============================================================

"""
GLOBAL:

x = 10


LOCAL:

def test():
    x = 20


READ GLOBAL:

x = 10

def test():
    print(x)


REASSIGN GLOBAL:

x = 10

def test():
    global x
    x = 20


ENCLOSING:

def outer():

    x = 10

    def inner():
        print(x)


NONLOCAL:

def outer():

    x = 10

    def inner():

        nonlocal x

        x += 1


LEGB:

Local
Enclosing
Global
Built-in


IMPORTANT:

global -> use when REASSIGNING global variable

nonlocal -> use when REASSIGNING enclosing variable
"""


# ============================================================
#                         END
# ============================================================