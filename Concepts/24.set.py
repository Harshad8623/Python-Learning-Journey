# ============================================================
#                         SET IN PYTHON
#              COMPLETE NOTES + INTERVIEW + DSA
# ============================================================

"""
A SET is an unordered collection of UNIQUE elements.

Example:

    numbers = {1, 2, 3, 4}

Important properties:

1. Mutable
2. Elements are UNIQUE
3. Unordered
4. No indexing
5. No duplicate elements
6. Elements must be HASHABLE
7. Very useful in DSA
8. Membership checking is O(1) average case
"""


# ============================================================
# 1. CREATING A SET
# ============================================================

numbers = {1, 2, 3, 4, 5}

print(numbers)
print(type(numbers))


# ============================================================
# 2. DUPLICATES ARE AUTOMATICALLY REMOVED
# ============================================================

numbers = {1, 2, 2, 3, 3, 3, 4}

print(numbers)

"""
Output will contain only unique values.

{1, 2, 3, 4}
"""


# ============================================================
# 3. EMPTY SET
# ============================================================

# IMPORTANT:
# {} creates an EMPTY DICTIONARY, not a set.

empty_dict = {}

print(type(empty_dict))


# To create an empty set:

empty_set = set()

print(type(empty_set))


# ============================================================
# 4. SET USING set()
# ============================================================

numbers = set([1, 2, 3, 4, 5])

print(numbers)


# String to set:

letters = set("harshad")

print(letters)

"""
Duplicate characters are removed.
"""


# ============================================================
# 5. SET FROM TUPLE
# ============================================================

numbers = set((1, 2, 3, 4))

print(numbers)


# ============================================================
# 6. SET FROM RANGE
# ============================================================

numbers = set(range(1, 6))

print(numbers)


# ============================================================
# 7. SET CAN CONTAIN DIFFERENT HASHABLE TYPES
# ============================================================

data = {
    10,
    20.5,
    "Python",
    True,
    (1, 2)
}

print(data)


# ============================================================
# 8. SET CANNOT CONTAIN LIST
# ============================================================

"""
This is INVALID:

data = {
    1,
    2,
    [3, 4]
}

Why?

Because list is UNHASHABLE.
"""


# ============================================================
# 9. SET CANNOT CONTAIN DICTIONARY
# ============================================================

"""
This is INVALID:

data = {
    1,
    {"a": 10}
}

Dictionary is unhashable.
"""


# ============================================================
# 10. SET CANNOT CONTAIN ANOTHER SET
# ============================================================

"""
This is invalid:

data = {
    1,
    {2, 3}
}

Normal set is unhashable.

However, frozenset can be used.
"""


# ============================================================
# 11. FROZENSET
# ============================================================

data = frozenset({1, 2, 3})

print(data)
print(type(data))


"""
frozenset is immutable.

Therefore, it can be used as a dictionary key
or as an element of another set.
"""


# ============================================================
# 12. SET HAS NO INDEXING
# ============================================================

numbers = {10, 20, 30, 40}

"""
This is invalid:

print(numbers[0])

Set does not support indexing.
"""


# ============================================================
# 13. SET HAS NO SLICING
# ============================================================

"""
This is invalid:

print(numbers[1:3])

Sets do not support slicing.
"""


# ============================================================
# 14. LOOP THROUGH SET
# ============================================================

numbers = {10, 20, 30, 40}

for num in numbers:
    print(num)


"""
The order should not be relied upon.
"""


# ============================================================
# 15. len()
# ============================================================

numbers = {10, 20, 30, 40}

print(len(numbers))


# ============================================================
# 16. MEMBERSHIP - in
# ============================================================

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(50 in numbers)


"""
Very important for DSA:

    x in set

has O(1) average time complexity.
"""


# ============================================================
# 17. not in
# ============================================================

print(50 not in numbers)


# ============================================================
# 18. add()
# ============================================================

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)


# ============================================================
# 19. ADD DUPLICATE
# ============================================================

numbers = {1, 2, 3}

numbers.add(2)

print(numbers)

"""
Nothing happens because 2 already exists.
"""


# ============================================================
# 20. add() ONE ELEMENT
# ============================================================

numbers = {1, 2, 3}

numbers.add(10)

print(numbers)


"""
add() adds ONE element.

It does NOT iterate through an iterable.
"""


# ============================================================
# 21. update()
# ============================================================

numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)


"""
update() adds multiple elements.
"""


# ============================================================
# 22. update() WITH TUPLE
# ============================================================

numbers = {1, 2}

numbers.update((3, 4, 5))

print(numbers)


# ============================================================
# 23. update() WITH STRING
# ============================================================

letters = {"a", "b"}

letters.update("cat")

print(letters)

"""
String is iterable.

So characters are added individually.
"""


# ============================================================
# 24. remove()
# ============================================================

numbers = {1, 2, 3, 4}

numbers.remove(3)

print(numbers)


"""
remove(x):

Removes x.

If x doesn't exist:

    KeyError

is raised.
"""


# ============================================================
# 25. discard()
# ============================================================

numbers = {1, 2, 3, 4}

numbers.discard(3)

print(numbers)


# ============================================================
# 26. discard() WITH MISSING ELEMENT
# ============================================================

numbers = {1, 2, 3}

numbers.discard(100)

print(numbers)


"""
discard() does NOT raise an error
if the element doesn't exist.
"""


# ============================================================
# 27. remove() VS discard()
# ============================================================

"""
remove(x):

    Missing element -> KeyError


discard(x):

    Missing element -> No error
"""


# ============================================================
# 28. pop()
# ============================================================

numbers = {10, 20, 30, 40}

result = numbers.pop()

print("Removed:", result)
print(numbers)


"""
IMPORTANT:

Set has no fixed index.

Therefore:

    set.pop()

removes and returns an arbitrary element.

Do NOT assume it removes the first or last element.
"""


# ============================================================
# 29. clear()
# ============================================================

numbers = {1, 2, 3}

numbers.clear()

print(numbers)


"""
clear() removes all elements.
"""


# ============================================================
# 30. copy()
# ============================================================

numbers = {1, 2, 3}

new_numbers = numbers.copy()

print(new_numbers)


# ============================================================
# 31. UNION
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)


"""
Union contains elements from BOTH sets.

Result:

{1, 2, 3, 4, 5}
"""


# ============================================================
# 32. UNION USING |
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

result = a | b

print(result)


"""
| is the set union operator.
"""


# ============================================================
# 33. UNION USING update()
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

a.update(b)

print(a)


"""
update() modifies the original set.
"""


# ============================================================
# 34. INTERSECTION
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a.intersection(b)

print(result)


"""
Intersection contains elements common to BOTH sets.

Result:

{2, 3}
"""


# ============================================================
# 35. INTERSECTION USING &
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a & b

print(result)


# ============================================================
# 36. intersection_update()
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)

print(a)


"""
Original set a is modified.

a becomes:

{2, 3}
"""


# ============================================================
# 37. DIFFERENCE
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a.difference(b)

print(result)


"""
Elements present in A but NOT in B.

Result:

{1}
"""


# ============================================================
# 38. DIFFERENCE USING -
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a - b

print(result)


# ============================================================
# 39. difference_update()
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

a.difference_update(b)

print(a)


"""
a becomes:

{1}
"""


# ============================================================
# 40. SYMMETRIC DIFFERENCE
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a.symmetric_difference(b)

print(result)


"""
Elements present in A OR B,
but NOT in both.

Result:

{1, 4}
"""


# ============================================================
# 41. SYMMETRIC DIFFERENCE USING ^
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a ^ b

print(result)


# ============================================================
# 42. symmetric_difference_update()
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

a.symmetric_difference_update(b)

print(a)


# ============================================================
# 43. SUBSET
# ============================================================

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))


"""
A is subset of B because every element of A
exists in B.
"""


# ============================================================
# 44. SUBSET USING <=
# ============================================================

a = {1, 2}
b = {1, 2, 3, 4}

print(a <= b)


# ============================================================
# 45. PROPER SUBSET USING <
# ============================================================

a = {1, 2}
b = {1, 2, 3, 4}

print(a < b)


"""
< means proper subset.

A must be a subset of B,
but A and B cannot be equal.
"""


# ============================================================
# 46. SUPERSET
# ============================================================

a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))


# ============================================================
# 47. SUPERSET USING >=
# ============================================================

print(a >= b)


# ============================================================
# 48. PROPER SUPERSET USING >
# ============================================================

print(a > b)


# ============================================================
# 49. DISJOINT
# ============================================================

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))


"""
True means:

No common elements.
"""


# ============================================================
# 50. NOT DISJOINT
# ============================================================

a = {1, 2}
b = {2, 3}

print(a.isdisjoint(b))


# ============================================================
# 51. SET COMPARISON
# ============================================================

a = {1, 2, 3}
b = {3, 2, 1}

print(a == b)


"""
True.

Order does not matter in sets.
"""


# ============================================================
# 52. SET COMPARISON - ORDER DOES NOT MATTER
# ============================================================

a = {1, 2, 3}
b = {1, 3, 2}

print(a == b)


# ============================================================
# 53. SET COMPARISON - DUPLICATES DON'T MATTER
# ============================================================

a = {1, 2, 3}
b = {1, 2, 2, 3, 3}

print(a == b)


# ============================================================
# 54. SET COMPREHENSION
# ============================================================

squares = {
    x * x
    for x in range(1, 6)
}

print(squares)


# ============================================================
# 55. SET COMPREHENSION WITH CONDITION
# ============================================================

even_numbers = {
    x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_numbers)


# ============================================================
# 56. REMOVE DUPLICATES FROM LIST
# ============================================================

numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique = set(numbers)

print(unique)


"""
This is one of the most common uses of set.
"""


# ============================================================
# 57. REMOVE DUPLICATES WHILE PRESERVING ORDER
# ============================================================

numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique = list(dict.fromkeys(numbers))

print(unique)


"""
Important:

set(numbers)

does NOT guarantee that you should rely on
the original list's order.

If you need unique values while preserving
insertion order:

    list(dict.fromkeys(numbers))
"""


# ============================================================
# 58. FIND COMMON ELEMENTS OF TWO LISTS
# ============================================================

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = set(a) & set(b)

print(common)


# ============================================================
# 59. FIND UNIQUE ELEMENTS OF FIRST LIST
# ============================================================

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = set(a) - set(b)

print(result)


# ============================================================
# 60. FIND UNION OF TWO LISTS
# ============================================================

a = [1, 2, 3]
b = [3, 4, 5]

result = set(a) | set(b)

print(result)


# ============================================================
# 61. CHECK DUPLICATES IN LIST
# ============================================================

numbers = [1, 2, 3, 4, 2]

if len(numbers) != len(set(numbers)):
    print("Duplicates exist")
else:
    print("No duplicates")


"""
Very useful interview technique.
"""


# ============================================================
# 62. FIND DUPLICATE ELEMENTS
# ============================================================

numbers = [1, 2, 3, 2, 4, 3, 5]

seen = set()
duplicates = set()

for num in numbers:

    if num in seen:
        duplicates.add(num)

    seen.add(num)

print(duplicates)


"""
This is an important DSA pattern.

seen = set()

if x in seen:
    duplicate

seen.add(x)
"""


# ============================================================
# 63. FIND FIRST DUPLICATE
# ============================================================

numbers = [5, 3, 1, 3, 5]

seen = set()

for num in numbers:

    if num in seen:
        print("First duplicate:", num)
        break

    seen.add(num)


# ============================================================
# 64. CHECK IF TWO LISTS HAVE COMMON ELEMENT
# ============================================================

a = [1, 2, 3]
b = [7, 8, 3]

if set(a) & set(b):
    print("Common element exists")


# ============================================================
# 65. CHECK IF TWO LISTS ARE DISJOINT
# ============================================================

a = [1, 2]
b = [3, 4]

if set(a).isdisjoint(set(b)):
    print("No common elements")


# ============================================================
# 66. UNIQUE CHARACTERS
# ============================================================

text = "python"

unique_characters = set(text)

print(unique_characters)


# ============================================================
# 67. CHECK ALL CHARACTERS UNIQUE
# ============================================================

text = "python"

if len(text) == len(set(text)):
    print("All characters are unique")
else:
    print("Duplicate characters exist")


# ============================================================
# 68. CHECK DUPLICATE CHARACTERS
# ============================================================

text = "programming"

if len(text) != len(set(text)):
    print("Duplicate characters exist")


# ============================================================
# 69. SET VS LIST MEMBERSHIP
# ============================================================

"""
LIST:

    numbers = [1, 2, 3, 4]

    4 in numbers

Average:

    O(n)


SET:

    numbers = {1, 2, 3, 4}

    4 in numbers

Average:

    O(1)


This is why sets are extremely useful in DSA.
"""


# ============================================================
# 70. TIME COMPLEXITY
# ============================================================

"""
Average-case complexity:

    add()              -> O(1)
    remove()           -> O(1)
    discard()          -> O(1)
    pop()              -> O(1)
    membership "in"    -> O(1)

Union:

    O(len(A) + len(B))

Intersection:

    approximately O(min(len(A), len(B)))

Difference:

    approximately O(len(A))

Iteration:

    O(n)


IMPORTANT:

Set operations are generally O(1) average-case because
Python sets use hash tables internally.
"""


# ============================================================
# 71. HASHING
# ============================================================

"""
A set uses HASHING internally.

For example:

    numbers = {10, 20, 30}

Python calculates hash values for elements and uses
a hash table internally.

This makes operations such as:

    x in numbers

very fast on average.
"""


# ============================================================
# 72. HASHABLE VS UNHASHABLE
# ============================================================

"""
HASHABLE:

    int
    float
    str
    bool
    tuple (if all elements are hashable)
    frozenset


UNHASHABLE:

    list
    set
    dict


Set elements MUST be hashable.
"""


# ============================================================
# 73. FROZENSET AS SET ELEMENT
# ============================================================

a = {
    1,
    2,
    frozenset({3, 4})
}

print(a)


"""
frozenset is immutable and hashable.
"""


# ============================================================
# 74. SET OF TUPLES
# ============================================================

points = {
    (1, 2),
    (3, 4),
    (5, 6)
}

print(points)


"""
Useful in DSA for storing coordinates.
"""


# ============================================================
# 75. GRAPH / VISITED SET
# ============================================================

"""
In graph problems, a set is commonly used
to track visited nodes.
"""

visited = set()

visited.add(1)
visited.add(2)
visited.add(3)

print(visited)


# ============================================================
# 76. GRAPH VISITED PATTERN
# ============================================================

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

visited = set()


def dfs(node):

    if node in visited:
        return

    visited.add(node)

    print(node)

    for neighbour in graph[node]:
        dfs(neighbour)


dfs(1)


"""
IMPORTANT DSA PATTERN:

if node in visited:
    return

visited.add(node)


You'll see this in:

    DFS
    BFS
    Graph traversal
    Cycle detection
    Backtracking
"""


# ============================================================
# 77. TWO SUM USING SET
# ============================================================

numbers = [2, 7, 11, 15]
target = 9

seen = set()

for num in numbers:

    required = target - num

    if required in seen:
        print("Pair:", required, num)
        break

    seen.add(num)


"""
Dictionary can also solve Two Sum when you need indices.

Set is enough when you only need to know
whether a complementary value exists.
"""


# ============================================================
# 78. LONGEST CONSECUTIVE SEQUENCE - DSA IDEA
# ============================================================

numbers = [100, 4, 200, 1, 3, 2]

num_set = set(numbers)

longest = 0

for num in num_set:

    # Start only when num is beginning of sequence.
    if num - 1 not in num_set:

        current = num
        length = 1

        while current + 1 in num_set:
            current += 1
            length += 1

        longest = max(longest, length)

print("Longest consecutive sequence:", longest)


"""
This is a very important LeetCode-style problem.

Time:

    O(n) average

Space:

    O(n)
"""


# ============================================================
# 79. INTERSECTION OF TWO ARRAYS
# ============================================================

a = [1, 2, 2, 3]
b = [2, 2, 4]

result = set(a) & set(b)

print(result)


# ============================================================
# 80. CHECK SUBSET
# ============================================================

a = [1, 2]
b = [1, 2, 3, 4]

if set(a).issubset(set(b)):
    print("A is subset of B")


# ============================================================
# 81. SET METHODS SUMMARY
# ============================================================

"""
IMPORTANT SET METHODS:

    add()
    clear()
    copy()
    difference()
    difference_update()
    discard()
    intersection()
    intersection_update()
    isdisjoint()
    issubset()
    issuperset()
    pop()
    remove()
    symmetric_difference()
    symmetric_difference_update()
    union()
    update()


VERY IMPORTANT FOR DSA:

    add()
    remove()
    discard()
    union()
    intersection()
    difference()
    issubset()
    isdisjoint()
    in
"""


# ============================================================
# 82. SET OPERATORS SUMMARY
# ============================================================

"""
UNION:

    A | B

or:

    A.union(B)


INTERSECTION:

    A & B

or:

    A.intersection(B)


DIFFERENCE:

    A - B

or:

    A.difference(B)


SYMMETRIC DIFFERENCE:

    A ^ B

or:

    A.symmetric_difference(B)


SUBSET:

    A <= B

or:

    A.issubset(B)


PROPER SUBSET:

    A < B


SUPERSET:

    A >= B

or:

    A.issuperset(B)


PROPER SUPERSET:

    A > B


DISJOINT:

    A.isdisjoint(B)
"""


# ============================================================
# 83. SET VS LIST VS TUPLE VS DICTIONARY
# ============================================================

"""
LIST:

    [1, 2, 3]

    Ordered
    Mutable
    Duplicates allowed
    Indexing available


TUPLE:

    (1, 2, 3)

    Ordered
    Immutable
    Duplicates allowed
    Indexing available


SET:

    {1, 2, 3}

    Unordered
    Mutable
    Duplicates NOT allowed
    No indexing


DICTIONARY:

    {
        "name": "Harshad"
    }

    Key-value pairs
    Mutable
    Keys unique
    Keys must be hashable
"""


# ============================================================
# 84. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a set?

A:

A mutable collection of unique hashable elements.


Q2. Does a set allow duplicates?

A:

No.


Q3. Does a set maintain insertion order?

A:

Do not rely on set ordering.

Sets are conceptually unordered collections.


Q4. Can we use indexing with set?

A:

No.


Q5. Can we slice a set?

A:

No.


Q6. Can a list be an element of a set?

A:

No.

List is unhashable.


Q7. Can a tuple be an element of a set?

A:

Yes, if all elements inside the tuple are hashable.


Q8. Difference between remove() and discard()?

A:

remove():

Raises KeyError if element doesn't exist.

discard():

Does not raise an error.


Q9. What does pop() do?

A:

Removes and returns an arbitrary element.


Q10. What is the difference between set and frozenset?

A:

set is mutable.

frozenset is immutable.


Q11. What is the time complexity of:

    x in set

A:

O(1) average case.


Q12. Why is set membership fast?

A:

Because Python sets use hash tables.


Q13. How do you remove duplicates from a list?

A:

    list(set(arr))


But remember that set does not preserve the list's
ordering semantics.


Q14. How do you find common elements?

A:

    A & B


Q15. How do you find elements present in A but not B?

A:

    A - B


Q16. How do you find union?

A:

    A | B


Q17. How do you check whether A is a subset of B?

A:

    A.issubset(B)

or:

    A <= B


Q18. What is a frozen set?

A:

An immutable version of a set.
"""


# ============================================================
# 85. IMPORTANT OUTPUT QUESTIONS
# ============================================================

"""
Question:

s = {1, 2, 2, 3}

print(len(s))

Answer:

3


------------------------------------------------------------

Question:

s = {1, 2, 3}

print(2 in s)

Answer:

True


------------------------------------------------------------

Question:

s = {1, 2, 3}

s.add(2)

print(s)

Answer:

Still contains only:

{1, 2, 3}


------------------------------------------------------------

Question:

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)

Answer:

{3}


------------------------------------------------------------

Question:

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

Answer:

{1, 2, 3, 4, 5}


------------------------------------------------------------

Question:

a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)

Answer:

{1, 2}


------------------------------------------------------------

Question:

a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))

Answer:

True
"""


# ============================================================
# 86. MOST IMPORTANT DSA PATTERNS
# ============================================================

"""
PATTERN 1: CHECK DUPLICATE

seen = set()

for x in arr:

    if x in seen:
        print("Duplicate")

    seen.add(x)


------------------------------------------------------------

PATTERN 2: UNIQUE ELEMENTS

unique = set(arr)


------------------------------------------------------------

PATTERN 3: TWO SUM EXISTENCE

seen = set()

for x in arr:

    required = target - x

    if required in seen:
        ...


------------------------------------------------------------

PATTERN 4: GRAPH VISITED

visited = set()

if node in visited:
    return

visited.add(node)


------------------------------------------------------------

PATTERN 5: INTERSECTION

common = set(a) & set(b)


------------------------------------------------------------

PATTERN 6: UNION

all_elements = set(a) | set(b)


------------------------------------------------------------

PATTERN 7: DIFFERENCE

only_a = set(a) - set(b)


------------------------------------------------------------

PATTERN 8: UNIQUE CHARACTERS

unique = set(string)


------------------------------------------------------------

PATTERN 9: CHECK ALL UNIQUE

if len(s) == len(set(s)):
    print("Unique")


------------------------------------------------------------

PATTERN 10: LONGEST CONSECUTIVE SEQUENCE

num_set = set(nums)

for num in num_set:

    if num - 1 not in num_set:

        # start sequence
        ...


These patterns are extremely useful in coding interviews.
"""


# ============================================================
# 87. SET CHEAT SHEET
# ============================================================

"""
CREATE:

    s = {1, 2, 3}

EMPTY:

    s = set()


ADD:

    s.add(x)


ADD MULTIPLE:

    s.update(iterable)


REMOVE:

    s.remove(x)


SAFE REMOVE:

    s.discard(x)


REMOVE ARBITRARY:

    s.pop()


CLEAR:

    s.clear()


COPY:

    s.copy()


CHECK:

    x in s


UNION:

    A | B


INTERSECTION:

    A & B


DIFFERENCE:

    A - B


SYMMETRIC DIFFERENCE:

    A ^ B


SUBSET:

    A <= B


SUPERSET:

    A >= B


DISJOINT:

    A.isdisjoint(B)


LENGTH:

    len(s)


SET COMPREHENSION:

    {x*x for x in range(5)}


REMOVE DUPLICATES:

    set(list)


TIME COMPLEXITY:

    Search -> O(1) average
    Insert -> O(1) average
    Delete -> O(1) average
"""


# ============================================================
# 88. WHAT TO PRACTICE NEXT FOR DSA
# ============================================================

"""
After learning sets, solve these problems:

BEGINNER:

1. Remove duplicates from a list
2. Find duplicate elements
3. Find first duplicate
4. Find unique elements
5. Check if all elements are unique
6. Find common elements
7. Find union
8. Find intersection
9. Find difference
10. Check subset


INTERMEDIATE:

11. Two Sum
12. Intersection of Two Arrays
13. Happy Number
14. Contains Duplicate
15. Longest Consecutive Sequence
16. Valid Sudoku
17. Missing Number
18. Find the Difference
19. Jewels and Stones
20. Isomorphic Strings


IMPORTANT PATTERNS:

    Hashing
    Membership
    Frequency
    Two Pointer + Set
    Sliding Window + Set
    Graph + Visited Set
    Prefix Sum + Set
"""


# ============================================================
#                         FINAL NOTE
# ============================================================

"""
For your DSA preparation, remember this:

LIST:

    Search -> O(n)


SET:

    Search -> O(1) average


DICTIONARY:

    Search -> O(1) average


This is why:

    List
       ↓
    Set
       ↓
    Dictionary
       ↓
    Hashing
       ↓
    DSA


Set + Dictionary are the foundation of many
hashing-based coding interview problems.
"""

arr  = [1, 2, 2 ,1, 3 ,5]

# 1. Create
s = {1, 2, 3}

# 2. Add
s.add(4)

# 3. Remove
s.remove(2)

# 4. Safe remove
s.discard(100)

# 5. Membership
if 3 in s:
    print("Found")

# 6. Union
a | b

# 7. Intersection
a & b

# 8. Difference
a - b

# 9. Duplicate detection
seen = set()

for x in arr:
    if x in seen:
        print("Duplicate")
    seen.add(x)

# 10. All elements unique
if len(arr) == len(set(arr)):
    print("All unique")


print("\n==========================================")
print("          SET LEARNING COMPLETE")
print("==========================================")