# ================================================================
# PYTHON: PASS BY VALUE, PASS BY REFERENCE, REBINDING & MUTATING
# ================================================================

"""

One of the most common Python interview questions is:

    "Is Python pass-by-value or pass-by-reference?"

The best answer is:

    Python uses "call by sharing"
    (also described as "pass-by-object-reference" or
    "pass-by-object-sharing").

Python does NOT behave exactly like traditional pass-by-value
languages, and it does NOT behave exactly like traditional
pass-by-reference languages.

The important concepts are:

    1. Object
    2. Reference / name
    3. Assignment
    4. Passing an argument
    5. Rebinding
    6. Mutation
    7. Mutable vs immutable objects

MASTER IDEA:

    Function parameters receive references to the same objects.

    If the object is MUTATED:
        the caller can observe the change.

    If the parameter is REBOUND:
        the caller's variable is NOT changed.
"""


# =================================================================
# 1. FIRST UNDERSTAND OBJECTS AND NAMES
# =================================================================

"""
Consider:

    x = [10, 20, 30]

A useful mental model is:

    x  --------->  [10, 20, 30]
                    object

`x` is a NAME referring to an object.

It is better to think:

    variable/name -> object

rather than:

    variable = box containing value

This becomes very important when functions receive arguments.
"""


x = [10, 20, 30]

print("x:", x)
print("id(x):", id(x))


# =================================================================
# 2. ASSIGNMENT DOES NOT COPY
# =================================================================

"""
When we write:

    a = [1, 2, 3]
    b = a

Python does NOT create another list.

Instead:

    a ----\
           \
            ---> [1, 2, 3]
           /
    b ----/

Both names refer to the same object.
"""

a = [1, 2, 3]
b = a

print("\nAssignment:")
print("a is b:", a is b)

b.append(4)

print("a:", a)
print("b:", b)


# =================================================================
# 3. WHAT IS REBINDING?
# =================================================================

"""
REBINDING means making a name refer to a different object.

Example:

    x = 10
    x = 20

The integer 10 was not changed.

The name `x` was simply rebound from object 10 to object 20.

Similarly:

    a = [1, 2, 3]
    a = [100, 200, 300]

The original list was not modified.

The name `a` now refers to a different list.
"""


x = 10
print("\nBefore rebinding:")
print("x:", x)

x = 20

print("After rebinding:")
print("x:", x)


# =================================================================
# 4. MUTATING AN OBJECT
# =================================================================

"""
MUTATION means changing the existing object itself.

Example:

    numbers = [1, 2, 3]
    numbers.append(4)

The list object has been changed.

The name `numbers` still refers to the same list.

Common mutable objects:

    list
    dict
    set
    bytearray
"""


numbers = [1, 2, 3]

old_id = id(numbers)

numbers.append(4)

print("\nMutation:")
print("numbers:", numbers)
print("same object:", id(numbers) == old_id)


# =================================================================
# 5. REBINDING VS MUTATING
# =================================================================

"""
VERY IMPORTANT INTERVIEW DIFFERENCE:

MUTATION:

    a.append(4)

Changes the existing list.

REBINDING:

    a = [100, 200]

Makes `a` refer to a different list.

Compare:
"""


a = [1, 2, 3]

print("\nOriginal:")
print("a:", a)
print("id(a):", id(a))

a.append(4)

print("\nAfter mutation:")
print("a:", a)
print("id(a):", id(a))


a = [100, 200]

print("\nAfter rebinding:")
print("a:", a)
print("id(a):", id(a))


# =================================================================
# 6. FUNCTION ARGUMENTS
# =================================================================

"""
Now consider:

    def change(x):
        ...

    a = [1, 2, 3]
    change(a)

The parameter `x` refers to the SAME list object that `a`
refers to.

Conceptually:

    a ----\
           ---> [1, 2, 3]
    x ----/

There are two names, but one list object.
"""


def show_object(value):
    print("\nInside function:")
    print("value:", value)
    print("id(value):", id(value))


a = [10, 20, 30]

print("Outside:")
print("id(a):", id(a))

show_object(a)


# =================================================================
# 7. MUTATING A FUNCTION ARGUMENT
# =================================================================

"""
Because the parameter refers to the same mutable object,
mutation can be observed by the caller.
"""


def add_item(items):
    items.append(100)


numbers = [1, 2, 3]

add_item(numbers)

print("\nMutation inside function:")
print(numbers)


"""
Output:

[1, 2, 3, 100]

WHY?

Because:

    items.append(100)

mutates the same list object that `numbers` refers to.
"""


# =================================================================
# 8. REBINDING A FUNCTION PARAMETER
# =================================================================

"""
Now compare that with:

    def change(items):
        items = [100, 200]

This REBINDS the local parameter `items`.

It does not rebind the caller's variable.
"""


def change_list(items):
    items = [100, 200]


numbers = [1, 2, 3]

change_list(numbers)

print("\nRebinding inside function:")
print(numbers)


"""
Output:

[1, 2, 3]

The caller's `numbers` is unchanged.

WHY?

Initially:

    numbers ----\
                 ---> [1, 2, 3]
    items -------/

After:

    numbers -------> [1, 2, 3]

    items -------> [100, 200]

The parameter `items` was rebound locally.
"""


# =================================================================
# 9. MOST IMPORTANT EXAMPLE
# =================================================================

def test(value):
    value.append(4)
    value = [100, 200]


x = [1, 2, 3]

test(x)

print("\nMutation + rebinding in same function:")
print(x)


"""
Output:

[1, 2, 3, 4]

Why?

Step 1:

    value.append(4)

MUTATES the original list.

Step 2:

    value = [100, 200]

REBINDS only the local name `value`.

The mutation remains visible.
The rebinding does not affect x.
"""


# =================================================================
# 10. IMMUTABLE OBJECT EXAMPLE
# =================================================================

"""
Integers are immutable.

Consider:

    def change(n):
        n = n + 10

The expression creates a new integer object.

Then `n` is rebound to that new object.

The caller's variable is unchanged.
"""


def change_number(n):
    n = n + 10
    print("Inside function:", n)


x = 10

change_number(x)

print("\nImmutable argument:")
print("Outside function:", x)


"""
Output:

Inside function: 20
Outside function: 10
"""


# =================================================================
# 11. WHY DOES THIS HAPPEN WITH int?
# =================================================================

"""
Integers cannot be modified in-place.

You cannot do something like:

    10.change_to(20)

Instead:

    n = n + 10

creates a new integer object and rebinds n.

So the caller remains unchanged.
"""


# =================================================================
# 12. STRING EXAMPLE
# =================================================================

"""
Strings are immutable too.

Methods that appear to "change" strings usually return a new
string.
"""


def change_string(text):
    text = text.upper()
    print("Inside:", text)


name = "harshad"

change_string(name)

print("\nString:")
print("Outside:", name)


"""
Output:

Inside: HARSHAD
Outside: harshad
"""


# =================================================================
# 13. LIST EXAMPLE
# =================================================================

"""
Lists are mutable.

A list can be modified in-place.
"""


def change_list_value(values):
    values[0] = 999


numbers = [10, 20, 30]

change_list_value(numbers)

print("\nList mutation:")
print(numbers)


"""
Output:

[999, 20, 30]
"""


# =================================================================
# 14. DICTIONARY EXAMPLE
# =================================================================

"""
Dictionaries are mutable.
"""


def update_student(student):
    student["marks"] = 95


student = {
    "name": "Harshad",
    "marks": 80
}

update_student(student)

print("\nDictionary mutation:")
print(student)


# =================================================================
# 15. SET EXAMPLE
# =================================================================

"""
Sets are mutable.
"""


def add_skill(skills):
    skills.add("Python")


skills = {"SQL", "Git"}

add_skill(skills)

print("\nSet mutation:")
print(skills)


# =================================================================
# 16. TUPLE EXAMPLE
# =================================================================

"""
Tuples are immutable.

A tuple itself cannot be changed.

But a tuple can contain a mutable object.

Example:

    t = ([1, 2], [3, 4])

The tuple cannot replace its element:

    t[0] = [100]    # TypeError

But the list inside it can be mutated:

    t[0].append(5)
"""


def modify_tuple_content(t):
    t[0].append(100)


data = ([1, 2], [3, 4])

modify_tuple_content(data)

print("\nTuple containing mutable list:")
print(data)


# =================================================================
# 17. "PASS BY VALUE" EXPLAINED
# =================================================================

"""
In traditional PASS-BY-VALUE:

    A copy of the value is passed to the function.

Changes to the parameter do not affect the caller's variable.

For example, conceptually:

    caller x = 10

    function receives:
        copy of 10

    function changes its copy

    caller x remains 10
"""


# =================================================================
# 18. "PASS BY REFERENCE" EXPLAINED
# =================================================================

"""
In traditional PASS-BY-REFERENCE:

The function receives access to the caller's variable/reference
itself.

The function can reassign the caller's variable.

Python does NOT work this way.

Python does not give the function a direct mechanism to rebind
the caller's local name.

Instead, the parameter is another name referring to the same
object.
"""


# =================================================================
# 19. THE BEST PYTHON ANSWER
# =================================================================

"""
INTERVIEW QUESTION:

    "Is Python pass-by-value or pass-by-reference?"

GOOD ANSWER:

    "Python uses call-by-sharing, also called
    call-by-object-reference. Function arguments are passed as
    object references. If the referenced object is mutable, a
    mutation made inside the function can be visible to the
    caller. However, rebinding the parameter inside the function
    does not rebind the caller's variable."


# =================================================================
# 20. WHY "PASS BY REFERENCE" IS NOT THE BEST ANSWER
# =================================================================


Suppose:

    def change(x):
        x = 100

    a = 10
    change(a)

If Python were traditional pass-by-reference, we might expect
`a` to become 100.

But:

    a remains 10.

Therefore, saying simply:

    "Python is pass by reference"

is misleading.

"""


def change(x):
    x = 100


a = 10

change(a)

print("\nDoes rebinding parameter change caller?")
print(a)


# =================================================================
# 21. WHY "PASS BY VALUE" IS ALSO INCOMPLETE
# =================================================================

"""
Suppose:

    def add_item(items):
        items.append(100)

    numbers = [1, 2, 3]
    add_item(numbers)

The caller sees:

    [1, 2, 3, 100]

If you simply say:

    "Python is pass by value"

without explaining object sharing, this behavior becomes
confusing.

The accurate model is:

    call-by-sharing / object-reference semantics.
"""


# =================================================================
# 22. CALL-BY-SHARING
# =================================================================

"""
CALL-BY-SHARING means:

    The function receives a reference to the same object.

But the function's parameter is its own local name.

Therefore:

    MUTATION of shared mutable object
        -> visible outside

    REBINDING of local parameter
        -> not visible outside


This is the most useful mental model for Python.
"""


# =================================================================
# 23. VISUAL MODEL
# =================================================================

"""
Before function call:

    numbers --------\
                     \
                      ---> [1, 2, 3]
                     /
    function param --/


After:

    items.append(4)

    numbers --------\
                     \
                      ---> [1, 2, 3, 4]
                     /
    items -----------/


If:

    items = [100, 200]

then:

    numbers -----------> [1, 2, 3, 4]

    items -------------> [100, 200]

The local name `items` was rebound.
"""


# =================================================================
# 24. RETURNING A NEW OBJECT
# =================================================================

"""
A function can return a new object.

Then the caller can explicitly rebind its variable.
"""


def add_ten(n):
    return n + 10


x = 10

x = add_ten(x)

print("\nReturning and rebinding:")
print(x)


"""
Here the caller explicitly does:

    x = returned_value

That is different from the function directly rebinding the
caller's local variable.
"""


# =================================================================
# 25. FUNCTION CAN MUTATE AND RETURN
# =================================================================

def add_value(items):
    items.append(100)
    return items


numbers = [1, 2, 3]

result = add_value(numbers)

print("\nMutation + return:")
print("numbers:", numbers)
print("result:", result)
print("numbers is result:", numbers is result)


# =================================================================
# 26. DEFAULT ARGUMENT INTERVIEW TRAP
# =================================================================

"""
This is related to mutation and object sharing.

BAD / SURPRISING PATTERN:

    def add_item(item, items=[]):
        items.append(item)
        return items

The default list is created once, not every time the function
is called.
"""


def add_item_bad(item, items=[]):
    items.append(item)
    return items


print("\nMutable default argument trap:")
print(add_item_bad("A"))
print(add_item_bad("B"))


"""
Output:

['A']
['A', 'B']

The same default list is reused.

BETTER:
"""


def add_item_good(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print("\nSafe mutable default pattern:")
print(add_item_good("A"))
print(add_item_good("B"))


# =================================================================
# 27. INTERVIEW: WHY USE None?
# =================================================================

"""
Because None is immutable and acts as a sentinel.

Each function call can create a fresh list:

    if items is None:
        items = []

This avoids accidentally sharing one mutable default object.
"""


# =================================================================
# 28. REBINDING WITH DICTIONARY
# =================================================================

def replace_dict(data):
    data = {
        "name": "Rahul"
    }


student = {
    "name": "Harshad"
}

replace_dict(student)

print("\nDictionary rebinding:")
print(student)


# =================================================================
# 29. MUTATING DICTIONARY
# =================================================================

def mutate_dict(data):
    data["name"] = "Rahul"


student = {
    "name": "Harshad"
}

mutate_dict(student)

print("\nDictionary mutation:")
print(student)


# =================================================================
# 30. LIST: REBINDING VS MUTATION SIDE BY SIDE
# =================================================================

def rebind_list(values):
    values = [100, 200]


def mutate_list(values):
    values.clear()
    values.extend([100, 200])


a = [1, 2, 3]
b = [1, 2, 3]

rebind_list(a)
mutate_list(b)

print("\nRebinding vs mutation:")
print("After rebind:", a)
print("After mutate:", b)


"""
Output:

After rebind: [1, 2, 3]
After mutate: [100, 200]

This is one of the BEST examples to understand the concept.
"""


# =================================================================
# 31. INTERVIEW QUESTION: CAN A FUNCTION CHANGE A VARIABLE?
# =================================================================

"""
ANSWER:

A function cannot directly rebind the caller's local variable
just by rebinding its parameter.

But it can:

    1. Mutate a shared mutable object.
    2. Return a new object so the caller can rebind its variable.

Example:

    def f(x):
        x = 100

does not change caller's variable.

But:

    def f(x):
        x.append(100)

can change the caller's list.
"""


# =================================================================
# 32. INTERVIEW QUESTION: HOW TO CHANGE CALLER'S VALUE?
# =================================================================

"""
For immutable values:

    return the new value

Example:
"""


def increment(x):
    return x + 1


x = 10

x = increment(x)

print("\nChanging immutable value through return:")
print(x)


"""
For mutable objects:

    mutate the object

or return a new object and let the caller assign it.
"""


# =================================================================
# 33. INTERVIEW QUESTION: DOES PYTHON PASS REFERENCES?
# =================================================================

"""
Careful answer:

    "Python passes object references by value, which is commonly
    described as call-by-sharing."

The function receives a COPY OF THE REFERENCE, not a copy of the
object.

Therefore:

    parameter and caller name refer to the same object initially.

But the parameter itself is local.

This explains both mutation and rebinding behavior.
"""


# =================================================================
# 34. REFERENCE VS OBJECT
# =================================================================

"""
Important distinction:

OBJECT:
    The actual data structure/value stored in memory.

REFERENCE / NAME:
    A way to access that object.

PARAMETER:
    A local name created for the function call.

So:

    a = [1, 2, 3]

creates a name `a` referring to a list object.

When:

    f(a)

is called, the function receives a parameter referring to that
same list object.
"""


# =================================================================
# 35. is vs == CONNECTION
# =================================================================

"""
`==` checks whether objects have equal values.

`is` checks whether they are the SAME OBJECT.

Example:
"""


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("\nEquality vs identity:")
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)


"""
Output:

a == b -> True
a is b -> False

a == c -> True
a is c -> True
"""


# =================================================================
# 36. id() CONNECTION
# =================================================================

"""
id() can help visualize identity.

If:

    a is b

then a and b refer to the same object, so they have the same
identity during that object's lifetime.
"""


a = [1, 2]
b = a
c = a.copy()

print("\nid() example:")
print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))


# =================================================================
# 37. NESTED OBJECTS AND MUTATION
# =================================================================

"""
Nested structures are where these concepts become especially
important.

Example:

    data = [[1, 2], [3, 4]]

The outer list and inner lists are separate objects.

A function may mutate an inner list.
"""


def mutate_nested(data):
    data[0].append(100)


data = [[1, 2], [3, 4]]

mutate_nested(data)

print("\nNested mutation:")
print(data)


# =================================================================
# 38. COPY + FUNCTION ARGUMENTS
# =================================================================

"""
If you do NOT want a function to mutate the caller's list, you
can pass a copy.

For a flat list:

    function(data.copy())

For nested mutable data, you may need:

    function(copy.deepcopy(data))
"""


def dangerous_function(items):
    items.append(100)


data = [1, 2, 3]

dangerous_function(data.copy())

print("\nPassing a copy:")
print(data)


# =================================================================
# 39. DEEP COPY + FUNCTION
# =================================================================

import copy


def nested_function(data):
    data[0].append(100)


data = [[1, 2], [3, 4]]

nested_function(copy.deepcopy(data))

print("\nPassing deep copy:")
print(data)


# =================================================================
# 40. DSA CONNECTION: BACKTRACKING
# =================================================================

"""
This concept is extremely important in DSA.

Suppose:

    path = []

During backtracking, we modify path:

    path.append(value)
    ...
    path.pop()

If we save:

    result.append(path)

we save a reference to the same list.

Usually we want a snapshot:

    result.append(path.copy())

Example:



path = [1, 2]
result = []

result.append(path)

path.append(3)

print("\nBacktracking without copy:")
print(result)


path = [1, 2]
result = []

result.append(path.copy())

path.append(3)

print("Backtracking with copy:")
print(result)


# =================================================================
# 41. DSA CONNECTION: MATRIX ALIASING
# =================================================================


Classic trap:

    matrix = [[0] * 3] * 3
All rows refer to the same inner list.

Therefore changing one row changes every row.
"""


matrix = [[0] * 3] * 3

matrix[0][0] = 1

print("\nAliased matrix:")
print(matrix)


# Correct:

matrix = [[0] * 3 for _ in range(3)]

matrix[0][0] = 1

print("Independent matrix:")
print(matrix)


# =================================================================
# 42. INTERVIEW QUESTIONS
# =================================================================

"""
THEORY QUESTIONS
----------------

1. Is Python pass-by-value or pass-by-reference?

2. What is call-by-sharing?

3. What does b = a do?

4. Does b = a create a copy?

5. What is rebinding?

6. What is mutation?

7. What is the difference between rebinding and mutation?

8. Why does modifying a list inside a function affect the caller?

9. Why does assigning a new list to a function parameter not
   affect the caller?

10. Why do integers behave differently from lists?

11. Are strings mutable?

12. Are tuples immutable?

13. Can a tuple contain mutable objects?

14. What does "Python passes references by value" mean?

15. What is an object reference?

16. What is aliasing?

17. What is the difference between `is` and `==`?

18. How does id() relate to object identity?

19. Why is `items=[]` as a default argument dangerous?

20. Why is `items=None` commonly used instead?

21. How can you prevent a function from mutating the caller's list?

22. When would you use list.copy() before passing an argument?

23. When would you use deepcopy() before passing an argument?

24. How does this concept affect recursion and backtracking?

25. Why is `[[0] * 3] * 3` a problem?


OUTPUT QUESTIONS
----------------

26.

    def f(x):
        x.append(10)

    a = [1, 2]
    f(a)
    print(a)

Answer:
    [1, 2, 10]


27.

    def f(x):
        x = x + [10]

    a = [1, 2]
    f(a)
    print(a)

Answer:
    [1, 2]

Why?
    `x + [10]` creates a new list and x is rebound.


28.

    def f(x):
        x += [10]

    a = [1, 2]
    f(a)
    print(a)

Answer:
    [1, 2, 10]

Why?
    For a list, `+=` mutates the list in-place.


29.

    def f(x):
        x = x + 10

    a = 5
    f(a)
    print(a)

Answer:
    5


30.

    def f(x):
        x += 10

    a = 5
    f(a)
    print(a)

Answer:
    5

The integer is immutable.


31.

    def f(x):
        x[0] = 100

    a = [1, 2, 3]
    f(a)
    print(a)

Answer:
    [100, 2, 3]


32.

    def f(x):
        x = [100, 200]
        x.append(300)

    a = [1, 2, 3]
    f(a)
    print(a)

Answer:
    [1, 2, 3]

Because the parameter was rebound before the mutation.


33.

    def f(x):
        x.append(100)
        x = [200]

    a = [1, 2, 3]
    f(a)
    print(a)

Answer:
    [1, 2, 3, 100]


34.

    a = [1, 2]
    b = a
    b.append(3)
    print(a is b)

Answer:
    True


35.

    a = [1, 2]
    b = a.copy()
    b.append(3)
    print(a is b)

Answer:
    False


# =================================================================
# 43. INTERVIEW-READY 30-SECOND ANSWER
# =================================================================


If the interviewer asks:

"Explain pass by value and pass by reference in Python."

Say:

    "Python is best described as using call-by-sharing, also
    called pass-by-object-reference. When an argument is passed,
    the function receives a reference to the same object through
    its local parameter. Therefore, if the object is mutable and
    the function mutates it, the caller can see that change.
    However, if the function rebinds the parameter to another
    object, the caller's variable is unaffected.

    For example, appending to a passed list changes the caller's
    list, but assigning a completely new list to the parameter
    does not change the caller's variable."


# =================================================================
# 44. MASTER DIFFERENCE
# =================================================================

"""
# +----------------------+------------------------------------------+
# | Concept              | Meaning                                  |
# +----------------------+------------------------------------------+
# | Assignment           | Name refers to an object                 |
# | Aliasing             | Multiple names refer to same object      |
# | Mutation             | Existing object is changed               |
# | Rebinding            | Name refers to a different object        |
# | Pass by value        | Copy of value is passed                  |
# | Pass by reference    | Caller variable/reference can be changed |
# | Python               | Call-by-sharing / object-reference       |
# +----------------------+------------------------------------------+
"""

MOST IMPORTANT:

    MUTATION
        |
        +--> changes the existing object
        |
        +--> caller may see the change


    REBINDING
        |
        +--> changes what the local name refers to
        |
        +--> caller's name is NOT rebound


MEMORY TRICK:

    SAME OBJECT + MUTATE
        -> visible outside

    NEW OBJECT + REBIND
        -> local only


FINAL INTERVIEW SENTENCE:

    "Python passes object references by value, or more precisely,
    uses call-by-sharing: the parameter is a local name referring
    to the same object, so mutation is visible but rebinding is
    local."

# =================================================================
# 45. PRACTICE TASKS
# =================================================================

"""

"""
Try these yourself before checking any solution:

TASK 1
------
Write a function that mutates a list by adding 10 to every
element.

TASK 2
------
Write a function that attempts to replace the entire list.
Predict whether the caller changes.

TASK 3
------
Write two functions:

    mutate_list()
    rebind_list()

Demonstrate the difference.

TASK 4
------
Create a nested list and pass it to a function. Mutate an inner
list and explain why the caller changes.

TASK 5
------
Create a function with a mutable default argument. Observe the
problem and fix it using None.

TASK 6
------
Explain why:

    x += [10]

behaves differently for a list than:

    x += 10

for an integer.

TASK 7
------
Explain the difference between:

    result.append(path)

and:

    result.append(path.copy())

in backtracking.

TASK 8
------
Explain why:

    [[0] * 3] * 3

is dangerous and write the correct matrix initialization.

TASK 9
------
Predict the output:

    def test(x):
        x.append(20)
        x = [50]

    a = [10]
    test(a)
    print(a)

TASK 10
-------
Explain this statement in your own words:

    "Python passes object references by value."


# =================================================================
# END OF FILE
# =================================================================

print("\n" + "=" * 70)
print("PASS BY VALUE / REFERENCE / REBINDING / MUTATING - COMPLETE")
print("=" * 70)
print("Remember:")
print("Mutation  -> changes the existing object")
print("Rebinding -> changes what a local name refers to")
print("Python    -> call-by-sharing / object-reference semantics")
print("=" * 70)
"""