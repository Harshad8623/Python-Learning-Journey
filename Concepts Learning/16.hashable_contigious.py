# ============================================================
#       HASHABLE / NON-HASHABLE + CONTIGUOUS / NON-CONTIGUOUS
# ============================================================


# ============================================================
# PART 1: HASHABLE AND NON-HASHABLE
# ============================================================

"""
Before understanding hashable, understand HASHING.

HASHING:

Hashing converts an object into a fixed integer value
using the hash() function.

Example:

x = 10

hash(x)

Python can calculate a hash value for 10.


IMPORTANT:

An object is HASHABLE if:

1. It has a hash value that does not change during its lifetime.
2. It can be compared for equality.
3. It can be used as:
      - a dictionary key
      - a set element


Common HASHABLE types:

    int
    float
    bool
    str
    tuple (if all its elements are hashable)
    frozenset


Common NON-HASHABLE types:

    list
    set
    dict


The main reason:

Mutable objects generally cannot be safely hashed because
their contents can change.
"""


# ============================================================
# 1. hash() FUNCTION
# ============================================================

x = 10

print("Hash of x:", hash(x))


name = "Harshad"

print("Hash of name:", hash(name))


value = 10.5

print("Hash of float:", hash(value))


# ============================================================
# 2. HASHABLE INTEGER
# ============================================================

x = 100

print(hash(x))

"""
Integers are hashable.

Therefore they can be used as dictionary keys
and set elements.
"""


# ============================================================
# 3. HASHABLE STRING
# ============================================================

name = "Python"

print(hash(name))

"""
Strings are immutable.

Therefore strings are hashable.
"""


# ============================================================
# 4. HASHABLE BOOLEAN
# ============================================================

value = True

print(hash(value))

"""
True and False are hashable.

In Python:

True behaves like 1
False behaves like 0
"""


# ============================================================
# 5. HASHABLE TUPLE
# ============================================================

data = (10, 20, 30)

print(hash(data))

"""
A tuple is immutable.

Therefore a tuple containing only hashable elements
is hashable.
"""


# ============================================================
# 6. TUPLE WITH NON-HASHABLE ELEMENT
# ============================================================

data = ([1, 2], 3)

# print(hash(data))

"""
This gives:

TypeError: unhashable type: 'list'

Why?

The tuple itself is immutable, but it contains a list.

The list is mutable and non-hashable.

Therefore the tuple is also not hashable.
"""


# ============================================================
# 7. FROZENSET
# ============================================================

data = frozenset({1, 2, 3})

print(hash(data))

"""
frozenset is an immutable version of set.

Therefore it is hashable.
"""


# ============================================================
# 8. NON-HASHABLE LIST
# ============================================================

numbers = [1, 2, 3]

# print(hash(numbers))

"""
This gives:

TypeError: unhashable type: 'list'

Why?

Lists are mutable.

Example:

numbers[0] = 100

The contents can change.

Therefore lists are non-hashable.
"""


# ============================================================
# 9. NON-HASHABLE SET
# ============================================================

numbers = {1, 2, 3}

# print(hash(numbers))

"""
Set is mutable.

Therefore set is non-hashable.
"""


# ============================================================
# 10. NON-HASHABLE DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

# print(hash(student))

"""
Dictionary is mutable.

Therefore dictionary is non-hashable.
"""


# ============================================================
# 11. HASHABLE AS DICTIONARY KEY
# ============================================================

student_marks = {

    "Harshad": 90,

    "Rahul": 85,

    "Sanjay": 88

}

print(student_marks)


"""
Dictionary keys MUST be hashable.

Strings are hashable.

Therefore:

"Harshad"
"Rahul"
"Sanjay"

can be dictionary keys.
"""


# ============================================================
# 12. INTEGER AS DICTIONARY KEY
# ============================================================

marks = {

    101: 90,

    102: 85,

    103: 95

}

print(marks)


"""
Integers are hashable.

Therefore integers can be dictionary keys.
"""


# ============================================================
# 13. TUPLE AS DICTIONARY KEY
# ============================================================

locations = {

    (18, 76): "Latur",

    (19, 74): "Pune"

}

print(locations)


"""
A tuple can be a dictionary key if every element
inside it is hashable.
"""


# ============================================================
# 14. LIST CANNOT BE DICTIONARY KEY
# ============================================================

# data = {
#     [1, 2, 3]: "Hello"
# }

"""
This gives:

TypeError: unhashable type: 'list'
"""


# ============================================================
# 15. LIST CANNOT BE SET ELEMENT
# ============================================================

# s = {[1, 2], [3, 4]}

"""
This gives:

TypeError: unhashable type: 'list'

Set elements must be hashable.
"""


# ============================================================
# 16. HASHABLE VS NON-HASHABLE SUMMARY
# ============================================================

"""
HASHABLE:

int
float
bool
str
tuple* 
frozenset

NON-HASHABLE:

list
set
dict

* Tuple is hashable only when all of its elements
  are hashable.
"""


# ============================================================
# 17. WHY IS HASHING IMPORTANT IN DSA?
# ============================================================

"""
Hashing is extremely important in DSA.

Python's:

set
dict

are based on hash tables.

This gives approximately O(1) average-time:

    insertion
    deletion
    membership/search
    dictionary lookup


Example:
"""


numbers = {10, 20, 30, 40, 50}

print(30 in numbers)

# Average case: O(1)


# Dictionary example:

frequency = {

    "apple": 3,

    "banana": 5,

    "orange": 2

}

print(frequency["banana"])

# Average case: O(1)


# ============================================================
# 18. DSA FREQUENCY COUNTING
# ============================================================

arr = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for number in arr:

    if number in frequency:

        frequency[number] += 1

    else:

        frequency[number] = 1


print(frequency)


"""
Output:

{
    1: 1,
    2: 2,
    3: 3,
    4: 1
}


This is one of the most important applications
of hashing in DSA.
"""


# ============================================================
# 19. CONTIGUOUS AND NON-CONTIGUOUS
# ============================================================

"""
Now let's understand another important DSA concept.

CONTIGUOUS:

Elements/items are next to each other without gaps.

Example:

Array:

[10, 20, 30, 40, 50]

The following are contiguous:

[10, 20]
[20, 30]
[30, 40]
[40, 50]

A contiguous section is also called a:

SUBARRAY

or

SUBSTRING (for strings)


NON-CONTIGUOUS:

Elements do NOT need to be next to each other.

You can skip elements.

Example:

[10, 30, 50]

from:

[10, 20, 30, 40, 50]

This is non-contiguous.

A non-contiguous selection is commonly called a:

SUBSEQUENCE
"""


# ============================================================
# 20. CONTIGUOUS EXAMPLE
# ============================================================

arr = [10, 20, 30, 40, 50]

"""
These are contiguous:

[10]
[20]
[30]

[10, 20]
[20, 30]
[30, 40]

[10, 20, 30]
[20, 30, 40]
[30, 40, 50]

[10, 20, 30, 40]
[20, 30, 40, 50]

[10, 20, 30, 40, 50]
"""


# ============================================================
# 21. CONTIGUOUS SUBARRAY
# ============================================================

arr = [1, 2, 3, 4, 5]

subarray = arr[1:4]

print(subarray)

# Output:
# [2, 3, 4]


"""
arr[1:4]

takes:

index 1 -> 2
index 2 -> 3
index 3 -> 4

These elements are next to each other.

Therefore this is a contiguous subarray.
"""


# ============================================================
# 22. NON-CONTIGUOUS SUBSEQUENCE
# ============================================================

arr = [1, 2, 3, 4, 5]

subsequence = [1, 3, 5]

print(subsequence)


"""
1 -> index 0
3 -> index 2
5 -> index 4

We skipped:

2
4

Therefore:

[1, 3, 5]

is NON-CONTIGUOUS.
"""


# ============================================================
# 23. IMPORTANT DIFFERENCE
# ============================================================

"""
CONTIGUOUS:

Original:

[1, 2, 3, 4, 5]

Choose:

[2, 3, 4]

No gap.

YES -> CONTIGUOUS


NON-CONTIGUOUS:

Original:

[1, 2, 3, 4, 5]

Choose:

[1, 3, 5]

Gaps exist.

YES -> NON-CONTIGUOUS
"""


# ============================================================
# 24. SUBARRAY VS SUBSEQUENCE
# ============================================================

"""
SUBARRAY:

Elements must be contiguous.

Example:

arr = [1, 2, 3, 4]

Valid subarrays:

[1]
[2]
[3]
[4]

[1, 2]
[2, 3]
[3, 4]

[1, 2, 3]
[2, 3, 4]

[1, 2, 3, 4]


SUBSEQUENCE:

Elements maintain their original order,
but they don't have to be adjacent.

Example:

[1, 3, 4]

from:

[1, 2, 3, 4]

is a subsequence.
"""


# ============================================================
# 25. SUBSEQUENCE ORDER IS IMPORTANT
# ============================================================

arr = [1, 2, 3, 4]

"""
[1, 3, 4]

is a subsequence.


But:

[4, 2, 1]

is NOT a subsequence of:

[1, 2, 3, 4]

because the original order is not maintained.
"""


# ============================================================
# 26. SUBSET VS SUBSEQUENCE
# ============================================================

"""
These concepts are different.

SUBSET:

Order does not matter.

Example:

{1, 3}

is a subset of:

{1, 2, 3}


SUBSEQUENCE:

Order matters.

Example:

[1, 3]

is a subsequence of:

[1, 2, 3]


But:

[3, 1]

is not a subsequence.

So:

SUBSET  -> order does NOT matter
SUBSEQUENCE -> order DOES matter
"""


# ============================================================
# 27. CONTIGUOUS STRING
# ============================================================

text = "ABCDE"

"""
Contiguous substrings:

"A"
"B"
"C"

"AB"
"BC"
"CD"
"DE"

"ABC"
"BCD"
"CDE"


For example:

"BCD"

is contiguous because B, C and D
are next to each other.
"""


# ============================================================
# 28. NON-CONTIGUOUS STRING
# ============================================================

text = "ABCDE"

"""
Examples of subsequences:

"ACE"
"ABD"
"BCD"
"AE"

"ACE":

A -> index 0
C -> index 2
E -> index 4

Elements are not adjacent.

Therefore it is non-contiguous.
"""


# ============================================================
# 29. CONTIGUOUS PROBLEMS IN DSA
# ============================================================

"""
When you see words like:

- subarray
- substring
- continuous segment
- contiguous segment

think:

CONTIGUOUS


Common DSA patterns:

1. Sliding Window
2. Prefix Sum
3. Kadane's Algorithm
4. Two Pointers (in some problems)
"""


# ============================================================
# 30. NON-CONTIGUOUS PROBLEMS IN DSA
# ============================================================

"""
When you see:

- subsequence
- choose elements
- pick / don't pick
- subset
- combinations

you may need:

1. Recursion
2. Backtracking
3. Dynamic Programming
4. Bit manipulation
"""


# ============================================================
# 31. SIMPLE CONTIGUOUS EXAMPLE
# ============================================================

arr = [1, 2, 3, 4, 5]

"""
Find sum of every contiguous subarray of size 3.

Windows:

[1, 2, 3] -> 6
[2, 3, 4] -> 9
[3, 4, 5] -> 12

This type of problem leads to:

SLIDING WINDOW
"""


# ============================================================
# 32. SIMPLE NON-CONTIGUOUS EXAMPLE
# ============================================================

arr = [1, 2, 3]

"""
Possible subsequences include:

[]
[1]
[2]
[3]

[1, 2]
[1, 3]
[2, 3]

[1, 2, 3]

Notice:

[1, 3]

is valid even though 2 is skipped.

This leads to:

SUBSEQUENCE / RECURSION / BACKTRACKING / DP
"""


# ============================================================
# 33. INTERVIEW QUESTIONS - HASHING
# ============================================================

"""
Q1. What is a hashable object?

An object whose hash value remains stable during
its lifetime and which can be compared for equality.

It can be used as a dictionary key or set element.


Q2. Is a list hashable?

NO.


Q3. Is a tuple hashable?

Usually YES, provided all its elements are hashable.


Q4. Is a string hashable?

YES.


Q5. Is a dictionary hashable?

NO.


Q6. Is a set hashable?

NO.


Q7. Is frozenset hashable?

YES.


Q8. Why can't a list be a dictionary key?

Because lists are mutable and therefore not hashable.


Q9. What data structures use hashing in Python?

set and dict.


Q10. Average lookup time in a set/dict?

Approximately O(1) average case.
"""


# ============================================================
# 34. INTERVIEW QUESTIONS - CONTIGUOUS
# ============================================================

"""
Q1. What is a subarray?

A contiguous portion of an array.


Q2. What is a substring?

A contiguous portion of a string.


Q3. What is a subsequence?

A sequence obtained by deleting zero or more elements
while maintaining the relative order of the remaining
elements.


Q4. Is [1, 3] a subarray of [1, 2, 3]?

NO.

Because 1 and 3 are not adjacent.


Q5. Is [1, 3] a subsequence of [1, 2, 3]?

YES.

Because the order is maintained.


Q6. Is [3, 1] a subsequence of [1, 2, 3]?

NO.

Because the order is not maintained.


Q7. What is the difference between subset and subsequence?

Subset:
Order does not matter.

Subsequence:
Relative order matters.
"""


# ============================================================
# 35. VERY IMPORTANT DSA TABLE
# ============================================================

"""
+----------------+-------------------------+
| CONCEPT        | KEY IDEA                |
+----------------+-------------------------+
| Hashable       | Can be hashed            |
| Non-hashable   | Cannot be hashed         |
| Subarray       | Contiguous               |
| Substring      | Contiguous               |
| Subsequence    | Order maintained         |
| Subset         | Order doesn't matter     |
+----------------+-------------------------+


HASHABLE:
    int
    float
    bool
    str
    tuple*
    frozenset

NON-HASHABLE:
    list
    set
    dict


* tuple must contain only hashable elements.
"""


# ============================================================
# 36. THE MOST IMPORTANT CONNECTION TO DSA
# ============================================================

"""
Think about these concepts like this:

HASHING
   |
   +----> set
   |
   +----> dict
   |
   +----> Frequency counting
   |
   +----> Two Sum
   |
   +----> Duplicate detection
   |
   +----> Fast lookup
   |
   +----> Average O(1)


CONTIGUOUS
   |
   +----> Subarray
   |
   +----> Substring
   |
   +----> Sliding Window
   |
   +----> Prefix Sum
   |
   +----> Kadane's Algorithm


NON-CONTIGUOUS
   |
   +----> Subsequence
   |
   +----> Subset
   |
   +----> Recursion
   |
   +----> Backtracking
   |
   +----> Dynamic Programming
"""


# ============================================================
# 37. QUICK MEMORY TRICK
# ============================================================

"""
HASHABLE:

"Can Python safely create a hash for this object
and use it as a dictionary key / set element?"

LIST -> NO
DICT -> NO
SET  -> NO

STR  -> YES
INT  -> YES
TUPLE -> YES*


CONTIGUOUS:

"Are the elements NEXT TO EACH OTHER?"

YES -> Subarray / Substring


NON-CONTIGUOUS:

"Can I SKIP elements while maintaining order?"

YES -> Subsequence
"""


# ============================================================
#                         END
# ============================================================