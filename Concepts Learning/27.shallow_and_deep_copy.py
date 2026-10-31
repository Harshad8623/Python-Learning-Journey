# ================================================================
# PYTHON: ASSIGNMENT (=), SHALLOW COPY & DEEP COPY
# ================================================================

"""
Understand exactly what happens with:

    b = a
    b = a.copy()
    b = copy.copy(a)
    b = copy.deepcopy(a)

The key idea is:

    =            -> same object
    shallow copy -> new outer object, nested objects may be shared
    deep copy    -> recursively copied nested objects

"""

import copy


# =================================================================
# 1. VARIABLES ARE REFERENCES TO OBJECTS
# =================================================================

"""
Python variables are names that refer to objects.

Example:

    a = [10, 20, 30]

Conceptually:

    a  ---------->  [10, 20, 30]

The variable `a` is not the list itself. It refers to the list.

This becomes important with:

    b = a

because b will refer to the same list.
"""


a = [10, 20, 30]

print("a:", a)
print("id(a):", id(a))


# =================================================================
# 2. NORMAL ASSIGNMENT: b = a
# =================================================================

"""
NORMAL ASSIGNMENT DOES NOT CREATE A COPY.

    b = a

means:

    "Make b refer to the same object as a."

Conceptually:

        a -------                  >------ [10, 20, 30]
        b -------/

There is only ONE list object.
"""


a = [10, 20, 30]
b = a

print("\nNORMAL ASSIGNMENT")
print("a:", a)
print("b:", b)
print("a is b:", a is b)
print("a == b:", a == b)


b.append(40)

print("\nAfter b.append(40):")
print("a:", a)
print("b:", b)


"""
Output:

a: [10, 20, 30, 40]
b: [10, 20, 30, 40]

WHY?

Because a and b point to the SAME list.

This is called ALIASING.
"""


# =================================================================
# 3. WHAT IS ALIASING?
# =================================================================

"""
Aliasing means multiple variables/references point to the same
object.

Example:

    a = [1, 2, 3]
    b = a

Now:

    a is b

is True.

Changing the object through b is visible through a.
"""


a = [1, 2, 3]
b = a

b[0] = 100

print("\nAliasing:")
print("a:", a)
print("b:", b)


# =================================================================
# 4. NORMAL ASSIGNMENT WITH A DICTIONARY
# =================================================================

student1 = {
    "name": "Harshad",
    "marks": [80, 90]
}

student2 = student1

student2["name"] = "Rahul"

print("\nDictionary assignment:")
print("student1:", student1)
print("student2:", student2)


"""
Both changed because there is only one dictionary.

This is NOT copying.
"""


# =================================================================
# 5. MUTABLE VS IMMUTABLE CONNECTION
# =================================================================

"""
COPYING becomes especially important with MUTABLE objects.

COMMON MUTABLE:
    list
    dict
    set
    bytearray

COMMON IMMUTABLE:
    int
    float
    bool
    str
    tuple
    frozenset
    bytes

Mutable objects can be changed in-place.

Immutable objects cannot be changed in-place.
"""


# Mutable
a = [1, 2, 3]
b = a

b.append(4)

print("\nMutable object:")
print("a:", a)
print("b:", b)


# Immutable
a = 10
b = a

b = 20

print("\nImmutable object:")
print("a:", a)
print("b:", b)


"""
Here b = 20 does not modify integer 10.

Instead, b is reassigned to another integer object.
"""


# =================================================================
# 6. SIMPLE LIST COPY
# =================================================================

"""
If the list is flat, we can create a separate outer list using:

    a.copy()
    a[:]
    list(a)
    copy.copy(a)

All are SHALLOW COPY operations.

For a flat list containing immutable values, this often behaves
exactly as expected.
"""


a = [1, 2, 3]
b = a.copy()

b.append(4)

print("\nlist.copy():")
print("a:", a)
print("b:", b)
print("a is b:", a is b)


a = [1, 2, 3]
b = a[:]

b.append(4)

print("\nSlicing copy:")
print("a:", a)
print("b:", b)


a = [1, 2, 3]
b = list(a)

b.append(4)

print("\nlist(a):")
print("a:", a)
print("b:", b)


# =================================================================
# 7. SHALLOW COPY
# =================================================================

"""
A SHALLOW COPY creates a NEW OUTER OBJECT.

But nested objects are NOT recursively copied.

Example:

    a = [[1, 2], [3, 4]]
    b = a.copy()

Now:

    a is b          -> False

BUT:

    a[0] is b[0]    -> True
    a[1] is b[1]    -> True

So:

    outer list = different
    inner lists = shared
"""


a = [[1, 2], [3, 4]]
b = copy.copy(a)

print("\nSHALLOW COPY")
print("a:", a)
print("b:", b)
print("a is b:", a is b)
print("a[0] is b[0]:", a[0] is b[0])
print("a[1] is b[1]:", a[1] is b[1])


# =================================================================
# 8. THE MOST IMPORTANT SHALLOW COPY EXAMPLE
# =================================================================

a = [[10, 20], [30, 40]]
b = a.copy()

b[0].append(100)

print("\nShallow copy + nested modification:")
print("a:", a)
print("b:", b)


"""
Output:

a:
[[10, 20, 100], [30, 40]]

b:
[[10, 20, 100], [30, 40]]

WHY?

Because:

    a[0] is b[0]

Both point to the same inner list.

Therefore:

    b[0].append(100)

changes the shared inner list.
"""


# =================================================================
# 9. SHALLOW COPY: REPLACEMENT VS MUTATION
# =================================================================

"""
This is another very common interview question.

Compare:

    b[0].append(100)

with:

    b[0] = [100, 200]

They are NOT the same.

append() mutates the shared inner list.

Assignment replaces the reference stored in b's outer list.
"""


a = [[10, 20], [30, 40]]
b = a.copy()

b[0] = [100, 200]

print("\nShallow copy + replacing nested reference:")
print("a:", a)
print("b:", b)


"""
a remains unchanged.

Why?

a and b have DIFFERENT outer lists.

Replacing b[0] only changes b's outer list.
"""


# =================================================================
# 10. SHALLOW COPY VISUAL MODEL
# =================================================================

"""
Original:

    a ------> Outer List A
                  |
                  +----> Inner List 1 [1, 2]
                  |
                  +----> Inner List 2 [3, 4]


After shallow copy:

    a ------> Outer List A
                  |
                  +----> Inner List 1 [1, 2]
                  |
                  +----> Inner List 2 [3, 4]

    b ------> Outer List B
                  |
                  +----> SAME Inner List 1
                  |
                  +----> SAME Inner List 2

Therefore:

    a is b       -> False
    a[0] is b[0] -> True
"""


# =================================================================
# 11. DEEP COPY
# =================================================================

"""
A DEEP COPY creates a new outer object AND recursively copies
nested objects.

Use:

    copy.deepcopy(a)

Example:

    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(a)

Now:

    a is b           -> False
    a[0] is b[0]     -> False
    a[1] is b[1]     -> False
"""


a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)

print("\nDEEP COPY")
print("a:", a)
print("b:", b)
print("a is b:", a is b)
print("a[0] is b[0]:", a[0] is b[0])
print("a[1] is b[1]:", a[1] is b[1])


# =================================================================
# 12. DEEP COPY NESTED MODIFICATION
# =================================================================

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)

b[0].append(100)

print("\nDeep copy + nested modification:")
print("a:", a)
print("b:", b)


"""
Output:

a:
[[10, 20], [30, 40]]

b:
[[10, 20, 100], [30, 40]]

The original is unchanged.

Why?

Because b[0] is a different list from a[0].
"""


# =================================================================
# 13. DEEPLY NESTED DATA
# =================================================================

"""
Deep copy becomes especially useful when data has multiple levels:

    list
       |
       +--> dictionary
               |
               +--> list
"""


original = [
    {
        "name": "Harshad",
        "marks": [80, 90, 95]
    },
    {
        "name": "Rahul",
        "marks": [70, 85, 88]
    }
]

deep = copy.deepcopy(original)

deep[0]["marks"].append(100)

print("\nDeeply nested dictionary/list:")
print("original:", original)
print("deep:", deep)


# =================================================================
# 14. NORMAL vs SHALLOW vs DEEP - ONE EXAMPLE
# =================================================================

original = [
    ["A", "B"],
    ["C", "D"]
]

normal = original
shallow = original.copy()
deep = copy.deepcopy(original)

normal[0].append("NORMAL")
shallow[1].append("SHALLOW")
deep[0].append("DEEP")

print("\nNORMAL vs SHALLOW vs DEEP")
print("original:", original)
print("normal:", normal)
print("shallow:", shallow)
print("deep:", deep)


"""
Interpretation:

normal shares the entire structure.

shallow has its own outer list but shares the inner lists with
original.

deep has independently copied nested lists.
"""


# =================================================================
# 15. DIFFERENCE TABLE
# =================================================================

"""
+----------------------+------------------+------------------+------------------+
| Feature              | Assignment =     | Shallow Copy     | Deep Copy        |
+----------------------+------------------+------------------+------------------+
| Example              | b = a            | b = a.copy()     | deepcopy(a)      |
|                      |                  | copy.copy(a)     |                  |
+----------------------+------------------+------------------+------------------+
| New outer object     | NO               | YES              | YES              |
+----------------------+------------------+------------------+------------------+
| Nested references    | SHARED           | SHARED           | COPIED           |
+----------------------+------------------+------------------+------------------+
| Independent outer    | NO               | YES              | YES              |
+----------------------+------------------+------------------+------------------+
| Independent nested   | NO               | NO               | YES              |
+----------------------+------------------+------------------+------------------+
| Speed                | Fastest          | Fast             | Usually slower   |
+----------------------+------------------+------------------+------------------+
| Memory               | Lowest           | Moderate         | Usually higher   |
+----------------------+------------------+------------------+------------------+

MEMORY TRICK:

    =          -> SAME
    shallow    -> NEW OUTSIDE, SHARED INSIDE
    deep       -> NEW OUTSIDE, COPIED INSIDE
"""


# =================================================================
# 16. DIFFERENCE BETWEEN copy.copy() AND list.copy()
# =================================================================

"""
For a list:

    a.copy()

and:

    copy.copy(a)

both perform a SHALLOW COPY.

Difference:

    a.copy()
        list-specific method

    copy.copy(a)
        general shallow-copy function from the copy module

Example:
"""


a = [[1, 2], [3, 4]]

b = a.copy()
c = copy.copy(a)

print("\ncopy.copy vs list.copy:")
print("a is b:", a is b)
print("a is c:", a is c)
print("a[0] is b[0]:", a[0] is b[0])
print("a[0] is c[0]:", a[0] is c[0])


# =================================================================
# 17. ALL COMMON SHALLOW COPY METHODS
# =================================================================

"""
LIST:

    a.copy()
    a[:]
    list(a)
    copy.copy(a)

DICTIONARY:

    d.copy()
    dict(d)
    copy.copy(d)

SET:

    s.copy()
    set(s)
    copy.copy(s)

These create shallow copies.
"""


# =================================================================
# 18. DICTIONARY SHALLOW COPY
# =================================================================

original = {
    "name": "Harshad",
    "skills": ["Python", "SQL"]
}

shallow = original.copy()

shallow["skills"].append("FastAPI")

print("\nDictionary shallow copy:")
print("original:", original)
print("shallow:", shallow)


"""
The nested list is shared.
"""


# =================================================================
# 19. DICTIONARY DEEP COPY
# =================================================================

original = {
    "name": "Harshad",
    "skills": ["Python", "SQL"]
}

deep = copy.deepcopy(original)

deep["skills"].append("FastAPI")

print("\nDictionary deep copy:")
print("original:", original)
print("deep:", deep)


"""
The original remains unchanged.
"""


# =================================================================
# 20. TUPLE TRICK
# =================================================================

"""
A tuple is immutable, but a tuple can contain mutable objects.

Example:

    t = ([1, 2], [3, 4])

You cannot do:

    t[0] = [100]

But you CAN do:

    t[0].append(100)

because the list inside the tuple is mutable.
"""


t = ([1, 2], [3, 4])
t[0].append(100)

print("\nTuple containing mutable objects:")
print(t)


# =================================================================
# 21. COPY AND IMMUTABLE OBJECTS
# =================================================================

"""
Deepcopy does not mean every value must become a completely
different physical object.

Immutable objects can safely be shared because they cannot be
mutated.

The important issue is independent mutable state.
"""


a = (1, 2, 3)
b = copy.deepcopy(a)

print("\nImmutable tuple:")
print("a:", a)
print("b:", b)
print("a is b:", a is b) # True beacuse this tuple not contain any mutable objects that's why True if a = (1, 2, 3, [12, 14]) then False
print("a == b:", a == b)


# =================================================================
# 22. ALIASING VS COPYING
# =================================================================

"""
ALIASING:

    b = a

Same object.

COPYING:

    b = a.copy()

Different outer object.

DEEP COPYING:

    b = copy.deepcopy(a)

Independent nested mutable structure.
"""


# =================================================================
# 23. INTERVIEW QUESTION: WHY DOES b = a NOT COPY?
# =================================================================

"""
ANSWER:

Because Python assignment binds a new name to an existing object.
It does not automatically duplicate the object.

If duplication is required, we explicitly request a copy.
"""


# =================================================================
# 24. INTERVIEW QUESTION: WHEN USE SHALLOW COPY?
# =================================================================

"""
Use shallow copy when:

    - You need a new outer container.
    - Nested objects can safely be shared.
    - The structure is flat.
    - Nested objects are immutable.
    - Shared nested state is intentional.
"""


# =================================================================
# 25. INTERVIEW QUESTION: WHEN USE DEEP COPY?
# =================================================================

"""
Use deep copy when:

    - Data is nested.
    - Nested objects are mutable.
    - The copied structure must be independent.
    - Changes to the copy must not affect the original.
"""


# =================================================================
# 26. INTERVIEW QUESTION: WHY NOT ALWAYS USE DEEPCOPY?
# =================================================================

"""
Deep copy is not automatically "better".

It can:

    - take more time
    - use more memory
    - copy objects unnecessarily
    - be inappropriate for some resources/special objects

Good programmers choose the minimum copying required.
"""


# =================================================================
# 27. INTERVIEW QUESTION: WHAT IS id()?
# =================================================================

"""
id(obj) returns an integer identifying the object during its
lifetime.

The most useful interview connection is:

    a is b

means both references point to the same object.

You can inspect identity using id().
"""


a = [1, 2]
b = a
c = a.copy()

print("\nid() comparison:")
print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))
print("a is b:", a is b)
print("a is c:", a is c)


# =================================================================
# 28. INTERVIEW OUTPUT QUESTION 1
# =================================================================

"""
QUESTION:

    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)

ANSWER:

    [1, 2, 3, 4]

Reason:
    b and a reference the same list.
"""


# =================================================================
# 29. INTERVIEW OUTPUT QUESTION 2
# =================================================================

"""
QUESTION:

    a = [1, 2, 3]
    b = a.copy()
    b.append(4)

    print(a)
    print(b)

ANSWER:

    [1, 2, 3]
    [1, 2, 3, 4]
"""


# =================================================================
# 30. INTERVIEW OUTPUT QUESTION 3
# =================================================================

"""
QUESTION:

    a = [[1, 2], [3, 4]]
    b = a.copy()

    b[0].append(5)

    print(a)

ANSWER:

    [[1, 2, 5], [3, 4]]

Reason:
    a[0] and b[0] are the same inner list.
"""


# =================================================================
# 31. INTERVIEW OUTPUT QUESTION 4
# =================================================================

"""
QUESTION:

    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(a)

    b[0].append(5)

    print(a)

ANSWER:

    [[1, 2], [3, 4]]

Reason:
    Nested lists were copied independently.
"""


# =================================================================
# 32. INTERVIEW OUTPUT QUESTION 5
# =================================================================

"""
QUESTION:

    a = [1, 2, 3]
    b = a.copy()

    print(a is b)
    print(a == b)

ANSWER:

    False
    True

`is` checks identity.
`==` checks equality/value.
"""


# =================================================================
# 33. INTERVIEW OUTPUT QUESTION 6
# =================================================================

"""
QUESTION:

    a = [[1, 2]]
    b = a.copy()

    print(a is b)
    print(a[0] is b[0])

ANSWER:

    False
    True

Outer object differs.
Inner object is shared.
"""


# =================================================================
# 34. INTERVIEW OUTPUT QUESTION 7
# =================================================================

"""
QUESTION:

    a = [[1, 2]]
    b = copy.deepcopy(a)

    print(a is b)
    print(a[0] is b[0])

ANSWER:

    False
    False
"""


# =================================================================
# 35. INTERVIEW QUESTION: MUTATION VS REASSIGNMENT
# =================================================================

"""
Very important distinction:

MUTATION:

    b[0].append(5)

Changes the existing inner object.

REASSIGNMENT:

    b[0] = [100, 200]

Changes which object b[0] refers to.

This distinction explains many shallow-copy interview questions.
"""


# =================================================================
# 36. CIRCULAR REFERENCES
# =================================================================

"""
A structure can contain a reference to itself:

    a = []
    a.append(a)

Deepcopy is designed to handle such recursive references using
internal memoization.
"""


a = []
a.append(a)

b = copy.deepcopy(a)

print("\nCircular reference:")
print("b is b[0]:", b is b[0])


# =================================================================
# 37. DSA CONNECTION: BACKTRACKING
# =================================================================

"""
Copying is very important in recursion and backtracking.

Example problem:

    path = [1, 2]
    result = []

If we do:

    result.append(path)

we store a reference to path.

Later:

    path.append(3)

can affect what is already stored in result.

Usually we want:

    result.append(path.copy())

for an independent snapshot of the current path.
"""


path = [1, 2]
result = []

result.append(path)
path.append(3)

print("\nBacktracking reference problem:")
print(result)


path = [1, 2]
result = []

result.append(path.copy())
path.append(3)

print("Backtracking using copy:")
print(result)


# =================================================================
# 38. DSA CONNECTION: MATRIX CREATION
# =================================================================

"""
FAMOUS INTERVIEW / DSA TRAP:

    matrix = [[0] * 3] * 3

This does NOT create three independent rows.

All three rows refer to the same list.
"""


matrix = [[0] * 3] * 3

matrix[0][0] = 1

print("\nWrong matrix creation:")
print(matrix)


"""
Output:

[[1, 0, 0],
 [1, 0, 0],
 [1, 0, 0]]

"""


# CORRECT
matrix = [[0] * 3 for _ in range(3)]

matrix[0][0] = 1

print("\nCorrect matrix creation:")
print(matrix)


"""
Output:

[[1, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
"""


# =================================================================
# 39. INTERVIEW QUESTIONS - THEORY
# =================================================================

"""
1. What is the difference between assignment and copying?

2. What happens when b = a?

3. What is aliasing?

4. What is a shallow copy?

5. What is a deep copy?

6. What is the difference between copy.copy() and
   copy.deepcopy()?

7. Is list.copy() shallow or deep?

8. Is list slicing a shallow or deep copy?

9. Is list(a) shallow or deep?

10. Why can modifying a nested list in a shallow copy affect the
    original?

11. Why can b[0] = new_list behave differently from
    b[0].append(value)?

12. When should you use shallow copy?

13. When should you use deep copy?

14. Why shouldn't deepcopy always be used?

15. What is the relationship between copying and mutability?

16. Can a tuple contain a mutable object?

17. What is the difference between is and ==?

18. How can id() help explain copying?

19. What is aliasing?

20. Why is [[0] * 3] * 3 dangerous?

21. How is copying relevant to backtracking?

22. Why can result.append(path) cause a bug in backtracking?

23. What is the difference between a reference and a copy?

24. Does Python pass variables by reference?

25. Explain Python's call-by-sharing/object-reference behavior.
"""


# =================================================================
# 40. OUTPUT-BASED INTERVIEW QUESTIONS
# =================================================================

"""
QUESTION A:

    a = [1, 2, 3]
    b = a
    b[0] = 100
    print(a)

Answer:
    [100, 2, 3]


QUESTION B:

    a = [1, 2, 3]
    b = a.copy()
    b[0] = 100
    print(a)

Answer:
    [1, 2, 3]


QUESTION C:

    a = [[1, 2], [3, 4]]
    b = a.copy()
    b[0][0] = 100
    print(a)

Answer:
    [[100, 2], [3, 4]]


QUESTION D:

    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(a)
    b[0][0] = 100
    print(a)

Answer:
    [[1, 2], [3, 4]]


QUESTION E:

    a = [1, 2]
    b = a

    print(a is b)
    print(a == b)

Answer:
    True
    True


QUESTION F:

    a = [1, 2]
    b = a.copy()

    print(a is b)
    print(a == b)

Answer:
    False
    True


QUESTION G:

    a = [[1]]
    b = a.copy()

    print(a is b)
    print(a[0] is b[0])

Answer:
    False
    True


QUESTION H:

    a = [[1]]
    b = copy.deepcopy(a)

    print(a is b)
    print(a[0] is b[0])

Answer:
    False
    False
"""


# =================================================================
# 41. HOW TO ANSWER IN AN INTERVIEW
# =================================================================

"""
If interviewer asks:

"Explain assignment, shallow copy and deep copy."

A strong answer:

"Normal assignment, such as b = a, does not create a copy.
It creates another reference to the same object, so both variables
can affect the same mutable object.

A shallow copy creates a new outer container, but nested objects
can still be shared. list.copy() and copy.copy() are examples.

A deep copy recursively copies nested objects, so the copied
structure can be modified independently from the original.
We use copy.deepcopy() for this.

In short:

    assignment = same object
    shallow copy = new outer object, shared nested objects
    deep copy = recursively independent copy."


# =================================================================
# 42. IMPORTANT INTERVIEW MISTAKES TO AVOID
# =================================================================

'''
WRONG:
    "b = a creates a copy."

CORRECT:
    "b = a creates another reference to the same object."


WRONG:
    "Shallow copy copies only the first element."

CORRECT:
    "Shallow copy creates a new outer object but does not
     recursively copy nested objects."


WRONG:
    "Deep copy is always better."

CORRECT:
    "Deep copy provides more independence but can cost more
     memory and time, so use it only when needed."


WRONG:
    "is and == are the same."

CORRECT:
    "`is` checks identity; `==` checks equality."


WRONG:
    "A tuple can never contain mutable data."

CORRECT:
    "The tuple itself is immutable, but it can contain mutable
     objects such as lists or dictionaries."
'''
# =================================================================
# 43. FINAL MASTER REVISION
# =================================================================


                    ASSIGNMENT      SHALLOW       DEEP
                    =               COPY          COPY
----------------------------------------------------------------
Outer object        SAME            NEW           NEW

Nested objects      SHARED          SHARED        COPIED

Independent?        NO              Outer only    Yes

Example:
    b = a            b = a.copy()   b = copy.deepcopy(a)

For flat lists:
    shallow copy is usually enough.

For nested mutable structures:
    deep copy may be needed.

For intentional sharing:
    normal assignment may be exactly what you want.


ONE-LINE MEMORY TRICK:

    =       -> SAME
    SHALLOW -> NEW OUTSIDE, SHARED INSIDE
    DEEP    -> NEW OUTSIDE, COPIED INSIDE
"""


# =================================================================
# 44. PRACTICE TASKS
# =================================================================

"""
Solve these without looking at the notes:

TASK 1
------
Predict the output:

    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)


TASK 2
------
Predict:

    a = [1, 2, 3]
    b = a.copy()
    b.append(4)

    print(a)
    print(b)


TASK 3
------
Predict:

    a = [[1, 2], [3, 4]]
    b = a.copy()
    b[0].append(5)

    print(a)


TASK 4
------
Predict:

    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(a)
    b[0].append(5)

    print(a)


TASK 5
------
Explain:

    matrix = [[0] * 3] * 3

and fix it.


TASK 6
------
Create a nested student dictionary.

Make:
    1. normal assignment
    2. shallow copy
    3. deep copy

Modify a nested list and compare all three.


TASK 7
------
For each of these, predict whether nested changes affect the
original:

    b = a
    b = a.copy()
    b = a[:]
    b = list(a)
    b = copy.copy(a)
    b = copy.deepcopy(a)


TASK 8
------
Explain the difference between:

    b[0].append(10)

and:

    b[0] = [10]


# =================================================================
# END
# =================================================================

print("\n" + "=" * 70)
print("ASSIGNMENT / SHALLOW COPY / DEEP COPY - COMPLETE")
print("=" * 70)
print("Remember:")
print("=          -> same object")
print("Shallow    -> new outer object, nested references may be shared")
print("Deep       -> recursively copied nested mutable objects")
print("=" * 70)

"""