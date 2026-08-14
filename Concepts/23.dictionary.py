# ============================================================
#                  DICTIONARY IN PYTHON
# ============================================================

"""
A dictionary is a collection of data stored in
KEY : VALUE pairs.

Example:

    student = {
        "name": "Harshad",
        "age": 21,
        "marks": 85
    }

Here:

    "name"  -> KEY
    "Harshad" -> VALUE

    "age"   -> KEY
    21      -> VALUE

    "marks" -> KEY
    85      -> VALUE


IMPORTANT PROPERTIES:

1. Mutable
2. Ordered (Python 3.7+ insertion order is guaranteed)
3. Keys must be hashable
4. Values can be any Python object
5. Keys must be unique
6. Values can be duplicated
7. Very important for DSA
"""


# ============================================================
# 1. CREATING A DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 85
}

print(student)
print(type(student))


# ============================================================
# 2. EMPTY DICTIONARY
# ============================================================

d = {}

print(d)
print(type(d))


# ============================================================
# 3. dict() CONSTRUCTOR
# ============================================================

student = dict(
    name="Harshad",
    age=21,
    marks=85
)

print(student)


# ============================================================
# 4. DICTIONARY WITH DIFFERENT VALUE TYPES
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "percentage": 85.5,
    "is_student": True,
    "subjects": ["Python", "SQL", "DSA"]
}

print(student)


# ============================================================
# 5. VALUES CAN BE ANY DATA TYPE
# ============================================================

data = {
    "name": "Harshad",
    "age": 21,
    "marks": [80, 90, 85],
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}

print(data)


# ============================================================
# 6. DICTIONARY KEYS MUST BE UNIQUE
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "age": 22
}

print(student)


"""
The second "age" replaces the first one.

Output:

{'name': 'Harshad', 'age': 22}
"""


# ============================================================
# 7. DICTIONARY KEYS
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 85
}

print(student.keys())


# ============================================================
# 8. DICTIONARY VALUES
# ============================================================

print(student.values())


# ============================================================
# 9. DICTIONARY ITEMS
# ============================================================

print(student.items())


# ============================================================
# 10. ACCESS VALUE USING KEY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print(student["name"])
print(student["age"])


# ============================================================
# 11. KEYERROR
# ============================================================

"""
student = {
    "name": "Harshad"
}

print(student["age"])

This produces:

KeyError

because "age" does not exist.
"""


# ============================================================
# 12. get()
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print(student.get("name"))
print(student.get("age"))


# ============================================================
# 13. get() FOR MISSING KEY
# ============================================================

print(student.get("marks"))


"""
If the key does not exist:

    get()

returns:

    None

instead of raising KeyError.
"""


# ============================================================
# 14. get() WITH DEFAULT VALUE
# ============================================================

print(student.get("marks", 0))
print(student.get("city", "Unknown"))


# ============================================================
# 15. ADD NEW KEY-VALUE
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

student["marks"] = 90

print(student)


# ============================================================
# 16. UPDATE EXISTING VALUE
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

student["age"] = 22

print(student)


"""
IMPORTANT:

If key exists:

    value gets UPDATED

If key doesn't exist:

    new key-value pair is ADDED.
"""


# ============================================================
# 17. UPDATE MULTIPLE VALUES
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

student.update({
    "age": 22,
    "marks": 90
})

print(student)


# ============================================================
# 18. update() WITH ANOTHER DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

extra = {
    "marks": 90,
    "city": "Pune"
}

student.update(extra)

print(student)


# ============================================================
# 19. DELETE USING del
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 90
}

del student["age"]

print(student)


# ============================================================
# 20. pop()
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 90
}

result = student.pop("age")

print(result)
print(student)


"""
pop():

1. Removes key-value pair
2. Returns the removed VALUE
"""


# ============================================================
# 21. pop() WITH DEFAULT
# ============================================================

student = {
    "name": "Harshad"
}

result = student.pop("age", 0)

print(result)


"""
If key doesn't exist:

    pop("age")

would produce KeyError.

But:

    pop("age", 0)

returns 0.
"""


# ============================================================
# 22. popitem()
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 90
}

result = student.popitem()

print(result)
print(student)


"""
popitem() removes and returns the LAST inserted
key-value pair.

Returns a tuple:

    (key, value)
"""


# ============================================================
# 23. clear()
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

student.clear()

print(student)


"""
clear():

Removes all elements.

Dictionary still exists but becomes empty.
"""


# ============================================================
# 24. copy()
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

new_student = student.copy()

print(new_student)


# ============================================================
# 25. len()
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 90
}

print(len(student))


"""
len(dictionary)

returns number of KEY-VALUE pairs.
"""


# ============================================================
# 26. MEMBERSHIP - in
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print("name" in student)
print("age" in student)
print("marks" in student)


"""
IMPORTANT:

    key in dictionary

checks KEYS, not values.
"""


# ============================================================
# 27. not in
# ============================================================

print("marks" not in student)


# ============================================================
# 28. CHECK VALUE
# ============================================================

print("Harshad" in student.values())
print(21 in student.values())


# ============================================================
# 29. LOOP THROUGH DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 90
}

for key in student:
    print(key)


"""
By default:

    for key in dictionary

iterates through KEYS.
"""


# ============================================================
# 30. LOOP THROUGH KEYS
# ============================================================

for key in student.keys():
    print(key)


# ============================================================
# 31. LOOP THROUGH VALUES
# ============================================================

for value in student.values():
    print(value)


# ============================================================
# 32. LOOP THROUGH ITEMS
# ============================================================

for key, value in student.items():
    print(key, value)


"""
This is VERY important for interviews and DSA.
"""


# ============================================================
# 33. DICTIONARY INDEXING DOES NOT EXIST
# ============================================================

"""
Dictionary does NOT use numeric indexing like:

    student[0]

unless 0 itself is a key.

Dictionary uses KEYS for access.
"""


# ============================================================
# 34. INTEGER KEYS
# ============================================================

data = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(data[1])
print(data[2])


# ============================================================
# 35. STRING KEYS
# ============================================================

data = {
    "name": "Harshad",
    "city": "Pune"
}

print(data["name"])


# ============================================================
# 36. TUPLE AS KEY
# ============================================================

data = {
    (1, 2): "Point A",
    (3, 4): "Point B"
}

print(data[(1, 2)])


"""
Tuples can be dictionary keys if all elements inside
the tuple are hashable.
"""


# ============================================================
# 37. LIST CANNOT BE KEY
# ============================================================

"""
This is invalid:

    data = {
        [1, 2]: "value"
    }

Because list is unhashable.
"""


# ============================================================
# 38. SET CANNOT BE KEY
# ============================================================

"""
This is invalid:

    data = {
        {1, 2}: "value"
    }

Because set is unhashable.
"""


# ============================================================
# 39. WHY DICTIONARY KEYS MUST BE HASHABLE
# ============================================================

"""
Dictionary internally uses HASHING.

Therefore keys must have a stable hash value.

Hashable examples:

    int
    float
    str
    tuple (if its elements are hashable)
    bool
    frozenset

Not hashable:

    list
    set
    dict
"""


# ============================================================
# 40. NESTED DICTIONARY
# ============================================================

students = {
    "student1": {
        "name": "Harshad",
        "age": 21
    },

    "student2": {
        "name": "Rahul",
        "age": 22
    }
}

print(students)


# ============================================================
# 41. ACCESS NESTED DICTIONARY
# ============================================================

print(students["student1"]["name"])
print(students["student2"]["age"])


# ============================================================
# 42. MODIFY NESTED DICTIONARY
# ============================================================

students["student1"]["age"] = 22

print(students)


# ============================================================
# 43. DICTIONARY WITH LIST VALUES
# ============================================================

students = {
    "Harshad": [85, 90, 88],
    "Rahul": [78, 82, 80]
}

print(students["Harshad"])


# ============================================================
# 44. ACCESS LIST INSIDE DICTIONARY
# ============================================================

print(students["Harshad"][0])


# ============================================================
# 45. DICTIONARY WITH TUPLE VALUES
# ============================================================

students = {
    "Harshad": (85, 90, 88),
    "Rahul": (78, 82, 80)
}

print(students["Harshad"])


# ============================================================
# 46. DICTIONARY WITH SET VALUES
# ============================================================

students = {
    "Harshad": {"Python", "SQL", "DSA"},
    "Rahul": {"Java", "C++"}
}

print(students)


# ============================================================
# 47. NESTED LIST OF DICTIONARIES
# ============================================================

students = [
    {
        "name": "Harshad",
        "marks": 90
    },

    {
        "name": "Rahul",
        "marks": 85
    }
]

print(students[0]["name"])
print(students[1]["marks"])


# ============================================================
# 48. dict.fromkeys()
# ============================================================

keys = ["name", "age", "marks"]

student = dict.fromkeys(keys)

print(student)


"""
Output:

{
    'name': None,
    'age': None,
    'marks': None
}
"""


# ============================================================
# 49. fromkeys() WITH DEFAULT VALUE
# ============================================================

keys = ["a", "b", "c"]

result = dict.fromkeys(keys, 0)

print(result)


"""
Output:

{'a': 0, 'b': 0, 'c': 0}
"""


# ============================================================
# 50. DICTIONARY COMPREHENSION
# ============================================================

"""
Syntax:

    {key: value for item in iterable}
"""


squares = {
    x: x * x
    for x in range(1, 6)
}

print(squares)


"""
Output:

{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
"""


# ============================================================
# 51. DICTIONARY COMPREHENSION WITH CONDITION
# ============================================================

even_squares = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)


# ============================================================
# 52. CONVERT LIST TO DICTIONARY
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]

result = {
    index: name
    for index, name in enumerate(names)
}

print(result)


# ============================================================
# 53. ZIP + DICTIONARY
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]
marks = [90, 85, 88]

student = dict(zip(names, marks))

print(student)


"""
Output:

{
    'Harshad': 90,
    'Rahul': 85,
    'Sanjay': 88
}
"""


# ============================================================
# 54. ZIP INTO DICTIONARY
# ============================================================

keys = ["name", "age", "city"]
values = ["Harshad", 21, "Pune"]

result = dict(zip(keys, values))

print(result)


# ============================================================
# 55. DICTIONARY UNPACKING
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

new_student = {
    **student,
    "marks": 90
}

print(new_student)


"""
** dictionary unpacking is very useful in Python.
"""


# ============================================================
# 56. MERGING DICTIONARIES USING |
# ============================================================

d1 = {
    "name": "Harshad",
    "age": 21
}

d2 = {
    "marks": 90,
    "city": "Pune"
}

result = d1 | d2

print(result)


"""
| dictionary merge operator is available in modern Python.
"""


# ============================================================
# 57. MERGING USING update()
# ============================================================

d1 = {
    "name": "Harshad",
    "age": 21
}

d2 = {
    "age": 22,
    "marks": 90
}

d1.update(d2)

print(d1)


"""
If the same key exists:

    d2's value replaces d1's value.
"""


# ============================================================
# 58. SHALLOW COPY
# ============================================================

original = {
    "name": "Harshad",
    "marks": [80, 90]
}

copy_data = original.copy()

copy_data["name"] = "Rahul"

print(original)
print(copy_data)


# ============================================================
# 59. SHALLOW COPY WITH NESTED OBJECT
# ============================================================

original = {
    "marks": [80, 90]
}

copy_data = original.copy()

copy_data["marks"].append(100)

print(original)
print(copy_data)


"""
Both dictionaries show the changed list.

Why?

copy() creates a SHALLOW COPY.

Nested objects are still shared.
"""


# ============================================================
# 60. DEEPCOPY
# ============================================================

import copy

original = {
    "marks": [80, 90]
}

copy_data = copy.deepcopy(original)

copy_data["marks"].append(100)

print(original)
print(copy_data)


"""
deepcopy() recursively copies nested objects.
"""


# ============================================================
# 61. SETDEFAULT()
# ============================================================

student = {
    "name": "Harshad"
}

result = student.setdefault("age", 21)

print(result)
print(student)


"""
If key doesn't exist:

    setdefault()

adds the key and returns the value.
"""


# ============================================================
# 62. setdefault() IF KEY EXISTS
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

result = student.setdefault("age", 100)

print(result)
print(student)


"""
Since "age" already exists:

    value is NOT changed.

This is useful in frequency/grouping problems.
"""


# ============================================================
# 63. FREQUENCY COUNT - VERY IMPORTANT FOR DSA
# ============================================================

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for num in numbers:

    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)


"""
Output:

{
    1: 1,
    2: 2,
    3: 3,
    4: 1
}
"""


# ============================================================
# 64. FREQUENCY COUNT USING get()
# ============================================================

numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)


"""
THIS PATTERN IS EXTREMELY IMPORTANT FOR DSA.

Memorize:

    d[x] = d.get(x, 0) + 1
"""


# ============================================================
# 65. CHARACTER FREQUENCY
# ============================================================

text = "banana"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)


"""
Output:

{
    'b': 1,
    'a': 3,
    'n': 2
}
"""


# ============================================================
# 66. WORD FREQUENCY
# ============================================================

text = "python is easy and python is powerful"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# ============================================================
# 67. FIRST NON-REPEATING CHARACTER
# ============================================================

text = "aabbcdde"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating:", char)
        break


# ============================================================
# 68. TWO SUM - VERY IMPORTANT DSA
# ============================================================

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):

    required = target - num

    if required in seen:
        print(seen[required], i)
        break

    seen[num] = i


"""
This is one of the MOST IMPORTANT dictionary/hash-map
patterns for coding interviews.

Time:

    O(n)

Space:

    O(n)
"""


# ============================================================
# 69. GROUPING VALUES
# ============================================================

students = [
    ("CSE", "Harshad"),
    ("ENTC", "Rahul"),
    ("CSE", "Sanjay"),
    ("ENTC", "Priya")
]

groups = {}

for branch, name in students:

    if branch not in groups:
        groups[branch] = []

    groups[branch].append(name)

print(groups)


# ============================================================
# 70. GROUPING USING setdefault()
# ============================================================

students = [
    ("CSE", "Harshad"),
    ("ENTC", "Rahul"),
    ("CSE", "Sanjay"),
    ("ENTC", "Priya")
]

groups = {}

for branch, name in students:
    groups.setdefault(branch, []).append(name)

print(groups)


# ============================================================
# 71. INVERT A DICTIONARY
# ============================================================

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

result = {
    value: key
    for key, value in data.items()
}

print(result)


"""
WARNING:

This only works safely when values are unique and hashable.
"""


# ============================================================
# 72. SORT DICTIONARY BY KEYS
# ============================================================

data = {
    "c": 3,
    "a": 1,
    "b": 2
}

result = dict(sorted(data.items()))

print(result)


# ============================================================
# 73. SORT DICTIONARY BY VALUES
# ============================================================

data = {
    "Harshad": 90,
    "Rahul": 85,
    "Sanjay": 95
}

result = dict(
    sorted(
        data.items(),
        key=lambda item: item[1]
    )
)

print(result)


# ============================================================
# 74. SORT DICTIONARY BY VALUES DESCENDING
# ============================================================

result = dict(
    sorted(
        data.items(),
        key=lambda item: item[1],
        reverse=True
    )
)

print(result)


# ============================================================
# 75. max() ON DICTIONARY
# ============================================================

numbers = {
    "a": 10,
    "b": 50,
    "c": 30
}

print(max(numbers))


"""
By default max(dictionary) checks KEYS.
"""


# ============================================================
# 76. MAX VALUE
# ============================================================

print(max(numbers.values()))


# ============================================================
# 77. KEY WITH MAX VALUE
# ============================================================

result = max(
    numbers,
    key=numbers.get
)

print(result)


"""
Output:

b

because b has maximum value 50.
"""


# ============================================================
# 78. MIN VALUE KEY
# ============================================================

result = min(
    numbers,
    key=numbers.get
)

print(result)


# ============================================================
# 79. KEY-VALUE WITH MAX VALUE
# ============================================================

result = max(
    numbers.items(),
    key=lambda item: item[1]
)

print(result)


"""
Returns:

(key, value)
"""


# ============================================================
# 80. DICTIONARY COMPREHENSION WITH CONDITIONS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

result = {
    x: "Even" if x % 2 == 0 else "Odd"
    for x in numbers
}

print(result)


# ============================================================
# 81. FILTER DICTIONARY
# ============================================================

marks = {
    "Harshad": 90,
    "Rahul": 65,
    "Sanjay": 85
}

result = {
    name: score
    for name, score in marks.items()
    if score >= 80
}

print(result)


# ============================================================
# 82. DICTIONARY + enumerate()
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]

student = {
    index: name
    for index, name in enumerate(names, start=1)
}

print(student)


# ============================================================
# 83. DICTIONARY + zip()
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]
marks = [90, 85, 88]

student = dict(zip(names, marks))

print(student)


# ============================================================
# 84. DICTIONARY LENGTH
# ============================================================

data = {
    "a": 10,
    "b": 20
}

print(len(data))


# ============================================================
# 85. DICTIONARY ORDER
# ============================================================

"""
Modern Python guarantees dictionary insertion order.

Example:

    d = {}

    d["a"] = 1
    d["b"] = 2
    d["c"] = 3

Iteration follows:

    a
    b
    c
"""


# ============================================================
# 86. DICTIONARY KEYS VIEW
# ============================================================

data = {
    "a": 1,
    "b": 2
}

keys = data.keys()

print(keys)
print(type(keys))


"""
dict_keys is a view object.

It is not a list.
"""


# ============================================================
# 87. DICTIONARY VALUES VIEW
# ============================================================

values = data.values()

print(values)
print(type(values))


# ============================================================
# 88. DICTIONARY ITEMS VIEW
# ============================================================

items = data.items()

print(items)
print(type(items))


# ============================================================
# 89. CONVERT VIEWS TO LIST
# ============================================================

print(list(data.keys()))
print(list(data.values()))
print(list(data.items()))


# ============================================================
# 90. DICTIONARY VIEW BEHAVIOR
# ============================================================

"""
keys(), values(), items()

return dynamic view objects.

They reflect changes made to the dictionary.
"""


# ============================================================
# 91. DICTIONARY METHODS SUMMARY
# ============================================================

"""
IMPORTANT DICTIONARY METHODS:

    clear()
    copy()
    fromkeys()
    get()
    items()
    keys()
    pop()
    popitem()
    setdefault()
    update()
    values()


VERY IMPORTANT FOR DSA:

    get()
    setdefault()
    items()
    keys()
    values()
    update()
"""


# ============================================================
# 92. DICTIONARY VS LIST
# ============================================================

"""
LIST:

    data = ["Harshad", "Rahul", "Sanjay"]

Access:

    data[0]

Uses numeric index.


DICTIONARY:

    data = {
        101: "Harshad",
        102: "Rahul"
    }

Access:

    data[101]

Uses keys.
"""


# ============================================================
# 93. DICTIONARY VS SET
# ============================================================

"""
DICTIONARY:

    {
        key: value
    }


SET:

    {
        value1,
        value2,
        value3
    }


Empty dictionary:

    {}


Empty set:

    set()
"""


# ============================================================
# 94. VERY IMPORTANT: {} IS DICTIONARY
# ============================================================

x = {}

print(type(x))


# Empty set:

x = set()

print(type(x))


# ============================================================
# 95. DICTIONARY TIME COMPLEXITY
# ============================================================

"""
Average-case complexity:

Access:

    d[key]        -> O(1)

Search key:

    key in d      -> O(1)

Insert:

    d[key] = x    -> O(1)

Delete:

    del d[key]    -> O(1)

get():

    d.get(key)    -> O(1)

update:

    Usually O(k), where k is number of entries added/updated.

Iteration:

    O(n)


IMPORTANT:

These are average-case complexities.

Hash table behavior can have collision-related effects.
"""


# ============================================================
# 96. WHY DICTIONARY IS SO IMPORTANT IN DSA
# ============================================================

"""
Dictionary is basically one of the most important
HASH MAP data structures for coding interviews.

Common DSA applications:

    1. Frequency counting
    2. Two Sum
    3. Duplicate detection
    4. First unique element
    5. Character counting
    6. Prefix sum
    7. Subarray sum
    8. Sliding window
    9. Grouping
   10. Graph adjacency representation
   11. Memoization
   12. Caching
   13. Fast lookup
   14. Counting pairs
   15. Finding duplicates
"""


# ============================================================
# 97. DUPLICATE DETECTION
# ============================================================

numbers = [1, 2, 3, 2, 5]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for num, count in frequency.items():

    if count > 1:
        print("Duplicate:", num)


# ============================================================
# 98. COUNT PAIRS
# ============================================================

numbers = [1, 5, 7, -1, 5]
target = 6

frequency = {}
count = 0

for num in numbers:

    required = target - num

    count += frequency.get(required, 0)

    frequency[num] = frequency.get(num, 0) + 1

print("Number of pairs:", count)


# ============================================================
# 99. PREFIX SUM + DICTIONARY
# ============================================================

"""
This is an important advanced DSA pattern.

Used for:

    Subarray Sum Equals K
"""

nums = [1, 2, 3]
target = 3

prefix_sum = 0
frequency = {0: 1}
count = 0

for num in nums:

    prefix_sum += num

    required = prefix_sum - target

    count += frequency.get(required, 0)

    frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

print(count)


# ============================================================
# 100. MEMOIZATION WITH DICTIONARY
# ============================================================

memo = {}


def fibonacci(n):

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


print(fibonacci(10))


"""
Dictionary stores already calculated results.

This is called MEMOIZATION.
"""


# ============================================================
# 101. GRAPH USING DICTIONARY
# ============================================================

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print(graph)


# ============================================================
# 102. GRAPH TRAVERSAL IDEA
# ============================================================

for node in graph:

    print(
        node,
        "->",
        graph[node]
    )


# ============================================================
# 103. DICTIONARY INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a dictionary?

A:

A mutable collection of key-value pairs.


Q2. Are dictionary keys unique?

A:

Yes.


Q3. Can dictionary values be duplicated?

A:

Yes.


Q4. Can dictionary keys be duplicated?

A:

No.

If duplicate key occurs, the latest value replaces
the previous value.


Q5. Can a list be a dictionary key?

A:

No.

List is unhashable.


Q6. Can a tuple be a dictionary key?

A:

Yes, if all elements inside it are hashable.


Q7. Is dictionary mutable?

A:

Yes.


Q8. Is dictionary ordered?

A:

Yes. In modern Python, insertion order is guaranteed.


Q9. What is the difference between:

    d[key]

and:

    d.get(key)

A:

d[key]

raises KeyError if key doesn't exist.

d.get(key)

returns None by default if key doesn't exist.


Q10. What does pop() return?

A:

The removed value.


Q11. What does popitem() return?

A:

A tuple containing the removed key and value.


Q12. What does keys() return?

A:

A dict_keys view.


Q13. What does values() return?

A:

A dict_values view.


Q14. What does items() return?

A:

A dict_items view containing key-value pairs.


Q15. What does update() do?

A:

Adds new key-value pairs and updates existing keys.


Q16. What does setdefault() do?

A:

Returns the existing value if key exists.

Otherwise inserts the key with the supplied default value
and returns that value.


Q17. What is dictionary comprehension?

A:

A compact way to construct dictionaries.


Q18. What is hashing?

A:

A technique used to map keys to positions/buckets using
a hash function, enabling fast average-case lookup.


Q19. What is average lookup complexity?

A:

O(1)


Q20. Why is dictionary useful in DSA?

A:

It provides fast average-case lookup and is commonly used
for frequency counting, hashing, grouping, prefix sums,
Two Sum, sliding window, graphs, etc.
"""


# ============================================================
# 104. IMPORTANT OUTPUT QUESTIONS
# ============================================================

"""
Question:

d = {
    "a": 10,
    "b": 20
}

print("a" in d)

Answer:

True


------------------------------------------------------------

Question:

d = {
    "a": 10,
    "b": 20
}

print(10 in d)

Answer:

False

Because `in` checks keys.


------------------------------------------------------------

Question:

d = {
    "a": 10,
    "b": 20
}

print(10 in d.values())

Answer:

True


------------------------------------------------------------

Question:

d = {}

d["a"] = 10
d["a"] = 20

print(d)

Answer:

{'a': 20}


------------------------------------------------------------

Question:

d = {
    "a": 10
}

print(d.get("b"))

Answer:

None


------------------------------------------------------------

Question:

d = {
    "a": 10
}

print(d.get("b", 0))

Answer:

0


------------------------------------------------------------

Question:

d = {
    "a": 10,
    "b": 20
}

print(d.pop("a"))

Answer:

10


------------------------------------------------------------

Question:

d = {
    "a": 10,
    "b": 20
}

print(d.popitem())

Answer:

('b', 20)


------------------------------------------------------------

Question:

d = {
    "a": 10,
    "b": 20
}

for x in d:
    print(x)

Answer:

a
b


------------------------------------------------------------

Question:

d = {
    "a": 10,
    "b": 20
}

for x, y in d.items():
    print(x, y)

Answer:

a 10
b 20
"""


# ============================================================
# 105. MOST IMPORTANT DSA PATTERNS TO MEMORIZE
# ============================================================

"""
PATTERN 1: FREQUENCY COUNT

frequency[x] = frequency.get(x, 0) + 1


PATTERN 2: CHECK EXISTENCE

if x in frequency:
    ...


PATTERN 3: TWO SUM

required = target - num

if required in seen:
    ...


PATTERN 4: GROUPING

groups.setdefault(key, []).append(value)


PATTERN 5: PREFIX SUM

prefix += num

required = prefix - target

if required in frequency:
    ...


PATTERN 6: MEMOIZATION

if n in memo:
    return memo[n]


PATTERN 7: SORT BY VALUE

sorted(data.items(), key=lambda x: x[1])


PATTERN 8: KEY WITH MAX VALUE

max(data, key=data.get)


These patterns will appear repeatedly in DSA.
"""


# ============================================================
# 106. FINAL DICTIONARY CHEAT SHEET
# ============================================================

"""
CREATION:

    d = {}

    d = {
        "name": "Harshad",
        "age": 21
    }


ACCESS:

    d["name"]

    d.get("name")


ADD:

    d["marks"] = 90


UPDATE:

    d["marks"] = 95

    d.update({...})


DELETE:

    del d["marks"]

    d.pop("marks")

    d.popitem()


CLEAR:

    d.clear()


CHECK KEY:

    "name" in d


CHECK VALUE:

    "Harshad" in d.values()


KEYS:

    d.keys()


VALUES:

    d.values()


ITEMS:

    d.items()


LOOP:

    for key, value in d.items():
        ...


LENGTH:

    len(d)


COPY:

    d.copy()


DEFAULT:

    d.get(key, default)


SET DEFAULT:

    d.setdefault(key, default)


COMPREHENSION:

    {x: x*x for x in range(5)}


MERGE:

    d1.update(d2)

    d3 = d1 | d2


UNPACK:

    {**d1, **d2}


FREQUENCY:

    freq[x] = freq.get(x, 0) + 1


TIME COMPLEXITY:

    Search -> O(1) average
    Insert -> O(1) average
    Delete -> O(1) average
    Access -> O(1) average


DSA IMPORTANCE:

    ⭐⭐⭐⭐⭐ VERY HIGH
"""


# ============================================================
# 107. WHAT YOU SHOULD PRACTICE NEXT
# ============================================================

"""
After learning dictionary, DON'T immediately jump to
advanced DSA.

First solve these problems:

BEGINNER:

1. Count frequency of numbers
2. Count frequency of characters
3. Find duplicate elements
4. Find unique elements
5. Find first non-repeating character
6. Find most frequent element
7. Find least frequent element
8. Check if two strings are anagrams
9. Count vowels using dictionary
10. Find common elements


INTERMEDIATE:

11. Two Sum
12. Group Anagrams
13. Intersection of Two Arrays
14. Top K Frequent Elements
15. Majority Element
16. Subarray Sum Equals K
17. Longest Consecutive Sequence
18. Isomorphic Strings
19. Happy Number
20. Longest Substring Without Repeating Characters


ADVANCED:

21. Sliding Window + HashMap
22. Prefix Sum + HashMap
23. Grouping + HashMap
24. Heap + HashMap
25. Graph + HashMap
26. Memoization + HashMap
"""


# ============================================================
#                         END
# ============================================================

print("\n==========================================")
print("       DICTIONARY LEARNING COMPLETE")
print("==========================================")