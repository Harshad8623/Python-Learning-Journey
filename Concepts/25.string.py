# ============================================================
#                     STRING IN PYTHON
#          COMPLETE NOTES + INTERVIEW + DSA
# ============================================================

"""
STRING IN PYTHON
================

A string is a sequence of characters.

Examples:

    "Hello"
    'Python'
    "Harshad"
    "12345"
    "Hello World"

Strings are:

1. Ordered
2. Indexed
3. Iterable
4. Immutable
5. Can contain duplicate characters
6. Can be sliced
7. Can be iterated using loops
8. Very important for DSA and coding interviews
"""


# ============================================================
# 1. CREATING STRINGS
# ============================================================

name = "Harshad"
language = 'Python'

print(name)
print(language)


# ============================================================
# 2. SINGLE CHARACTER IS ALSO A STRING
# ============================================================

char = "A"

print(char)
print(type(char))


"""
Python does not have a separate 'char' data type.

'A' is a string of length 1.
"""


# ============================================================
# 3. EMPTY STRING
# ============================================================

empty = ""

print(empty)
print(type(empty))
print(len(empty))


# ============================================================
# 4. STRING WITH NUMBERS
# ============================================================

num = "12345"

print(num)
print(type(num))


"""
Even though it contains numbers,
it is still a string because it is inside quotes.
"""


# ============================================================
# 5. STRING WITH SPECIAL CHARACTERS
# ============================================================

text = "Hello@123!"

print(text)


# ============================================================
# 6. MULTI-LINE STRING
# ============================================================

message = """
Hello Harshad
Welcome to Python
This is a multiline string
"""

print(message)


# ============================================================
# 7. TRIPLE SINGLE QUOTES
# ============================================================

message = '''
This is also
a multiline string.
'''

print(message)


# ============================================================
# 8. STRING IMMUTABILITY
# ============================================================

name = "Python"

"""
Strings are IMMUTABLE.

This is NOT allowed:

name[0] = "J"

Because individual characters of a string cannot be changed.
"""


# ============================================================
# 9. CREATING A NEW STRING
# ============================================================

name = "Python"

name = "J" + name[1:]

print(name)

"""
We didn't modify the original string.

We created a new string.
"""


# ============================================================
# 10. STRING INDEXING
# ============================================================

text = "Python"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])


"""
Index:

 P  y  t  h  o  n
 0  1  2  3  4  5
"""


# ============================================================
# 11. NEGATIVE INDEXING
# ============================================================

text = "Python"

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-4])
print(text[-5])
print(text[-6])


"""
Negative index:

 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
"""


# ============================================================
# 12. FIRST CHARACTER
# ============================================================

text = "Python"

print(text[0])


# ============================================================
# 13. LAST CHARACTER
# ============================================================

text = "Python"

print(text[-1])


# ============================================================
# 14. INDEX ERROR
# ============================================================

text = "Python"

"""
print(text[100])

IndexError
"""


# ============================================================
# 15. len()
# ============================================================

text = "Python"

print(len(text))


# ============================================================
# 16. STRING SLICING
# ============================================================

text = "Python"

print(text[0:3])

"""
Pyt
"""


# ============================================================
# 17. SLICING SYNTAX
# ============================================================

"""
string[start : stop : step]

start -> included
stop  -> excluded
step  -> jump size
"""


# ============================================================
# 18. BASIC SLICING
# ============================================================

text = "Python"

print(text[0:4])
print(text[1:5])
print(text[2:6])


# ============================================================
# 19. OMIT START
# ============================================================

text = "Python"

print(text[:4])


# ============================================================
# 20. OMIT STOP
# ============================================================

text = "Python"

print(text[2:])


# ============================================================
# 21. COPY ENTIRE STRING
# ============================================================

text = "Python"

print(text[:])


# ============================================================
# 22. STEP
# ============================================================

text = "Python"

print(text[::2])


# ============================================================
# 23. REVERSE STRING
# ============================================================

text = "Python"

print(text[::-1])


"""
Very important DSA trick:

    s[::-1]

reverses a string.
"""


# ============================================================
# 24. REVERSE USING LOOP
# ============================================================

text = "Python"

reverse = ""

for char in text:
    reverse = char + reverse

print(reverse)


# ============================================================
# 25. ITERATING THROUGH STRING
# ============================================================

text = "Python"

for char in text:
    print(char)


# ============================================================
# 26. ITERATING USING INDEX
# ============================================================

text = "Python"

for i in range(len(text)):
    print(text[i])


# ============================================================
# 27. REVERSE LOOP
# ============================================================

text = "Python"

for i in range(len(text) - 1, -1, -1):
    print(text[i])


# ============================================================
# 28. MEMBERSHIP OPERATOR
# ============================================================

text = "Python"

print("P" in text)
print("z" in text)


# ============================================================
# 29. NOT IN
# ============================================================

text = "Python"

print("z" not in text)


# ============================================================
# 30. STRING CONCATENATION
# ============================================================

first = "Hello"
second = "World"

result = first + " " + second

print(result)


# ============================================================
# 31. STRING REPETITION
# ============================================================

text = "Hi"

print(text * 3)

"""
HiHiHi
"""


# ============================================================
# 32. STRING COMPARISON
# ============================================================

a = "apple"
b = "banana"

print(a == b)
print(a != b)
print(a < b)
print(a > b)


"""
Strings are compared lexicographically
based on character ordering.
"""


# ============================================================
# 33. ASCII / UNICODE
# ============================================================

print(ord("A"))
print(ord("a"))
print(ord("0"))


"""
ord(character)

returns Unicode code point of a character.
"""


# ============================================================
# 34. chr()
# ============================================================

print(chr(65))
print(chr(97))
print(chr(48))


"""
chr(number)

converts Unicode code point into a character.
"""


# ============================================================
# 35. ord() + chr() IMPORTANT DSA IDEA
# ============================================================

char = "A"

value = ord(char)

print(value)

print(chr(value))


# ============================================================
# 36. STRING LENGTH
# ============================================================

text = "Hello World"

print(len(text))


"""
Spaces are also counted.
"""


# ============================================================
# 37. count()
# ============================================================

text = "banana"

print(text.count("a"))
print(text.count("n"))
print(text.count("x"))


"""
Returns number of occurrences.
"""


# ============================================================
# 38. count() WITH RANGE
# ============================================================

text = "banana"

print(text.count("a", 0, 4))


"""
count(substring, start, end)
"""


# ============================================================
# 39. find()
# ============================================================

text = "Hello Python"

print(text.find("Python"))
print(text.find("Hello"))
print(text.find("Java"))


"""
find():

Returns first index.

If not found:

    -1
"""


# ============================================================
# 40. rfind()
# ============================================================

text = "banana"

print(text.rfind("a"))


"""
rfind():

Searches from right side.

Returns the index of the last occurrence.
"""


# ============================================================
# 41. index()
# ============================================================

text = "Hello Python"

print(text.index("Python"))


"""
index() is similar to find().

Difference:

find()  -> -1 if not found
index() -> ValueError if not found
"""


# ============================================================
# 42. startswith()
# ============================================================

text = "Python Programming"

print(text.startswith("Python"))
print(text.startswith("Java"))


# ============================================================
# 43. endswith()
# ============================================================

text = "Python Programming"

print(text.endswith("Programming"))
print(text.endswith("Java"))


# ============================================================
# 44. LOWER()
# ============================================================

text = "PYTHON"

print(text.lower())


# ============================================================
# 45. UPPER()
# ============================================================

text = "python"

print(text.upper())


# ============================================================
# 46. CAPITALIZE()
# ============================================================

text = "python programming"

print(text.capitalize())


"""
Only first character becomes uppercase.
"""


# ============================================================
# 47. TITLE()
# ============================================================

text = "python programming language"

print(text.title())


"""
First character of each word becomes uppercase.
"""


# ============================================================
# 48. SWAPCASE()
# ============================================================

text = "PyThOn"

print(text.swapcase())


# ============================================================
# 49. CASEFOLD()
# ============================================================

text = "PYTHON"

print(text.casefold())


"""
casefold() is designed for aggressive,
Unicode-aware case-insensitive comparisons.

Useful when comparing text without caring about case.
"""


# ============================================================
# 50. STRIP()
# ============================================================

text = "   Python   "

print(text.strip())


"""
Removes whitespace from both ends.
"""


# ============================================================
# 51. LSTRIP()
# ============================================================

text = "   Python   "

print(text.lstrip())


"""
Removes whitespace from left side.
"""


# ============================================================
# 52. RSTRIP()
# ============================================================

text = "   Python   "

print(text.rstrip())


"""
Removes whitespace from right side.
"""


# ============================================================
# 53. STRIP WITH CHARACTERS
# ============================================================

text = "###Python###"

print(text.strip("#"))


"""
Important:

strip() does NOT remove an exact substring.

It removes matching characters from the ends.
"""


# ============================================================
# 54. REPLACE()
# ============================================================

text = "I like Java"

result = text.replace("Java", "Python")

print(result)


# ============================================================
# 55. REPLACE COUNT
# ============================================================

text = "apple apple apple"

print(text.replace("apple", "mango", 2))


"""
Only first 2 occurrences are replaced.
"""


# ============================================================
# 56. SPLIT()
# ============================================================

text = "Python is easy"

words = text.split()

print(words)


"""
Output:

['Python', 'is', 'easy']
"""


# ============================================================
# 57. SPLIT USING SEPARATOR
# ============================================================

text = "apple,banana,mango"

fruits = text.split(",")

print(fruits)


# ============================================================
# 58. SPLIT WITH LIMIT
# ============================================================

text = "a-b-c-d"

result = text.split("-", 2)

print(result)


"""
Maximum 2 splits.
"""


# ============================================================
# 59. RSPLIT()
# ============================================================

text = "a-b-c-d"

result = text.rsplit("-", 2)

print(result)


"""
Splits from right side.
"""


# ============================================================
# 60. SPLITLINES()
# ============================================================

text = "Hello\nPython\nWorld"

print(text.splitlines())


# ============================================================
# 61. JOIN()
# ============================================================

words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)


"""
join() is extremely important.

It joins iterable strings using a separator.
"""


# ============================================================
# 62. JOIN WITH COMMA
# ============================================================

words = ["Python", "Java", "C++"]

result = ", ".join(words)

print(result)


# ============================================================
# 63. JOIN WITH EMPTY STRING
# ============================================================

chars = ["P", "y", "t", "h", "o", "n"]

result = "".join(chars)

print(result)


# ============================================================
# 64. ISALPHA()
# ============================================================

print("Python".isalpha())
print("Python123".isalpha())


"""
True if all characters are alphabetic
and string is not empty.
"""


# ============================================================
# 65. ISDIGIT()
# ============================================================

print("12345".isdigit())
print("123a".isdigit())


# ============================================================
# 66. ISDECIMAL()
# ============================================================

print("123".isdecimal())


# ============================================================
# 67. ISNUMERIC()
# ============================================================

print("123".isnumeric())


"""
isdigit(), isdecimal(), isnumeric()
are related but not identical.

For basic coding problems,
isdigit() is commonly used.
"""


# ============================================================
# 68. ISALNUM()
# ============================================================

print("Python123".isalnum())
print("Python 123".isalnum())


"""
True if all characters are alphabetic or numeric.
"""


# ============================================================
# 69. ISSPACE()
# ============================================================

print("   ".isspace())
print("Python".isspace())


# ============================================================
# 70. ISLOWER()
# ============================================================

print("python".islower())
print("Python".islower())


# ============================================================
# 71. ISUPPER()
# ============================================================

print("PYTHON".isupper())
print("Python".isupper())


# ============================================================
# 72. ISTITLE()
# ============================================================

print("Python Programming".istitle())
print("python programming".istitle())


# ============================================================
# 73. ISIDENTIFIER()
# ============================================================

print("hello".isidentifier())
print("hello123".isidentifier())
print("123hello".isidentifier())


"""
Checks whether string can syntactically be used
as a Python identifier.

Note:

    "class".isidentifier()

is True because the syntax is identifier-like,
even though "class" is a Python keyword.
"""


# ============================================================
# 74. ISPRINTABLE()
# ============================================================

print("Hello".isprintable())
print("Hello\n".isprintable())


# ============================================================
# 75. ENCODING
# ============================================================

text = "Python"

encoded = text.encode()

print(encoded)
print(type(encoded))


# ============================================================
# 76. DECODE
# ============================================================

encoded = b"Python"

decoded = encoded.decode()

print(decoded)


"""
encode():

    str -> bytes

decode():

    bytes -> str
"""


# ============================================================
# 77. STRING FORMATTING - %
# ============================================================

name = "Harshad"
age = 21

print("Name: %s Age: %d" % (name, age))


"""
Older formatting style.
"""


# ============================================================
# 78. STRING FORMAT()
# ============================================================

name = "Harshad"
age = 21

print("Name: {} Age: {}".format(name, age))


# ============================================================
# 79. FORMAT WITH INDEX
# ============================================================

name = "Harshad"
age = 21

print("Name: {0} Age: {1}".format(name, age))


# ============================================================
# 80. FORMAT WITH KEYWORDS
# ============================================================

print(
    "Name: {name}, Age: {age}".format(
        name="Harshad",
        age=21
    )
)


# ============================================================
# 81. F-STRING
# ============================================================

name = "Harshad"
age = 21

print(f"Name: {name}, Age: {age}")


"""
F-string is the preferred modern style
for most normal Python formatting.
"""


# ============================================================
# 82. F-STRING EXPRESSIONS
# ============================================================

a = 10
b = 20

print(f"Sum = {a + b}")


# ============================================================
# 83. F-STRING FORMAT SPECIFIER
# ============================================================

price = 123.456789

print(f"{price:.2f}")


"""
2 digits after decimal.
"""


# ============================================================
# 84. STRING ALIGNMENT
# ============================================================

text = "Python"

print(text.ljust(10, "-"))
print(text.rjust(10, "-"))
print(text.center(10, "-"))


# ============================================================
# 85. ZFILL()
# ============================================================

num = "42"

print(num.zfill(5))


"""
42 -> 00042
"""


# ============================================================
# 86. PARTITION()
# ============================================================

text = "name=Harshad"

print(text.partition("="))


"""
Returns:

(
    before separator,
    separator,
    after separator
)
"""


# ============================================================
# 87. RPATITION()
# ============================================================

text = "a=b=c"

print(text.rpartition("="))


"""
Splits around the LAST occurrence.
"""


# ============================================================
# 88. REMOVEPREFIX()
# ============================================================

text = "PythonProgramming"

print(text.removeprefix("Python"))


# ============================================================
# 89. REMOVESUFFIX()
# ============================================================

text = "Python.py"

print(text.removesuffix(".py"))


# ============================================================
# 90. TRANSLATE()
# ============================================================

table = str.maketrans("abc", "123")

text = "abcabc"

print(text.translate(table))


"""
a -> 1
b -> 2
c -> 3
"""


# ============================================================
# 91. MAKETRANS()
# ============================================================

table = str.maketrans(
    "aeiou",
    "12345"
)

text = "education"

print(text.translate(table))


# ============================================================
# 92. STRING CONCATENATION USING LOOP
# ============================================================

chars = ["P", "y", "t", "h", "o", "n"]

result = ""

for char in chars:
    result += char

print(result)


# ============================================================
# 93. BETTER WAY - JOIN
# ============================================================

chars = ["P", "y", "t", "h", "o", "n"]

result = "".join(chars)

print(result)


"""
For joining many strings, join() is generally preferable
to repeatedly using +=.
"""


# ============================================================
# 94. PALINDROME
# ============================================================

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


"""
Palindrome:

    madam
    racecar
    level
"""


# ============================================================
# 95. PALINDROME USING LOOP
# ============================================================

text = "madam"

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:

    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(is_palindrome)


"""
This introduces an important DSA technique:

TWO POINTERS
"""


# ============================================================
# 96. COUNT VOWELS
# ============================================================

text = "python programming"

count = 0

for char in text:

    if char in "aeiou":
        count += 1

print("Vowels:", count)


# ============================================================
# 97. COUNT CONSONANTS
# ============================================================

text = "python programming"

count = 0

for char in text:

    if char.isalpha() and char not in "aeiou":
        count += 1

print("Consonants:", count)


# ============================================================
# 98. COUNT DIGITS
# ============================================================

text = "python123"

count = 0

for char in text:

    if char.isdigit():
        count += 1

print("Digits:", count)


# ============================================================
# 99. COUNT SPACES
# ============================================================

text = "Python is easy"

count = 0

for char in text:

    if char == " ":
        count += 1

print("Spaces:", count)


# ============================================================
# 100. CHARACTER FREQUENCY USING DICTIONARY
# ============================================================

text = "banana"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)


"""
Output:

{'b': 1, 'a': 3, 'n': 2}

VERY IMPORTANT DSA PATTERN.
"""


# ============================================================
# 101. CHARACTER FREQUENCY USING get()
# ============================================================

text = "banana"

frequency = {}

for char in text:

    frequency[char] = frequency.get(char, 0) + 1

print(frequency)


"""
This is a very important Python + DSA pattern:

frequency[x] = frequency.get(x, 0) + 1
"""


# ============================================================
# 102. FREQUENCY USING COUNTER
# ============================================================

from collections import Counter

text = "banana"

frequency = Counter(text)

print(frequency)


"""
Counter is extremely useful in coding interviews.
"""


# ============================================================
# 103. MOST COMMON CHARACTER
# ============================================================

text = "banana"

frequency = Counter(text)

print(frequency.most_common(1))


# ============================================================
# 104. FIRST NON-REPEATING CHARACTER
# ============================================================

text = "aabbcdde"

frequency = Counter(text)

for char in text:

    if frequency[char] == 1:
        print("First non-repeating:", char)
        break


"""
Important interview problem.
"""


# ============================================================
# 105. FIRST REPEATING CHARACTER
# ============================================================

text = "abcdbea"

seen = set()

for char in text:

    if char in seen:
        print("First repeating:", char)
        break

    seen.add(char)


"""
Set is useful when we only need to know whether
a character has already appeared.
"""


# ============================================================
# 106. REMOVE DUPLICATE CHARACTERS
# ============================================================

text = "programming"

result = ""

seen = set()

for char in text:

    if char not in seen:

        result += char
        seen.add(char)

print(result)


# ============================================================
# 107. ANAGRAM
# ============================================================

a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("Anagram")


"""
Anagram:

listen
silent

Both contain the same characters with
the same frequencies.
"""


# ============================================================
# 108. ANAGRAM USING COUNTER
# ============================================================

a = "listen"
b = "silent"

if Counter(a) == Counter(b):
    print("Anagram")


"""
Usually more efficient conceptually than sorting
when frequency counting is the intended approach.
"""


# ============================================================
# 109. ANAGRAM USING DICTIONARY
# ============================================================

a = "listen"
b = "silent"

if len(a) != len(b):
    print("Not Anagram")

else:

    freq = {}

    for char in a:
        freq[char] = freq.get(char, 0) + 1

    for char in b:

        if char not in freq:
            print("Not Anagram")
            break

        freq[char] -= 1

    else:
        if all(value == 0 for value in freq.values()):
            print("Anagram")


# ============================================================
# 110. REVERSE WORDS
# ============================================================

text = "Python is easy"

words = text.split()

words.reverse()

result = " ".join(words)

print(result)


# ============================================================
# 111. REVERSE WORDS USING SLICING
# ============================================================

text = "Python is easy"

result = " ".join(text.split()[::-1])

print(result)


# ============================================================
# 112. REVERSE EACH WORD
# ============================================================

text = "Python is easy"

words = text.split()

result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))


# ============================================================
# 113. CHECK SUBSTRING
# ============================================================

text = "Python programming"

if "Python" in text:
    print("Found")


# ============================================================
# 114. COUNT WORDS
# ============================================================

text = "Python is easy to learn"

words = text.split()

print("Number of words:", len(words))


# ============================================================
# 115. LONGEST WORD
# ============================================================

text = "Python programming is powerful"

words = text.split()

longest = ""

for word in words:

    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# ============================================================
# 116. SHORTEST WORD
# ============================================================

text = "Python is powerful"

words = text.split()

shortest = words[0]

for word in words:

    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)


# ============================================================
# 117. CAPITALIZE EVERY WORD
# ============================================================

text = "python programming language"

result = text.title()

print(result)


# ============================================================
# 118. TOGGLE CASE
# ============================================================

text = "PyThOn"

print(text.swapcase())


# ============================================================
# 119. CHECK PALINDROME IGNORING CASE
# ============================================================

text = "Madam"

text = text.lower()

if text == text[::-1]:
    print("Palindrome")


# ============================================================
# 120. PALINDROME IGNORING SPACES
# ============================================================

text = "nurses run"

clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")


# ============================================================
# 121. CLEAN STRING FOR PALINDROME
# ============================================================

text = "A man, a plan, a canal: Panama"

clean = ""

for char in text:

    if char.isalnum():
        clean += char.lower()

if clean == clean[::-1]:
    print("Palindrome")


"""
Very common interview problem.

This is similar to:

LeetCode - Valid Palindrome
"""


# ============================================================
# 122. TWO POINTER PALINDROME
# ============================================================

text = "racecar"

left = 0
right = len(text) - 1

while left < right:

    if text[left] != text[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1

else:
    print("Palindrome")


"""
This is a core DSA technique:

LEFT  -> moves forward
RIGHT -> moves backward
"""


# ============================================================
# 123. CHECK ONLY DIGITS
# ============================================================

text = "123456"

if text.isdigit():
    print("Only digits")


# ============================================================
# 124. STRING TO INTEGER
# ============================================================

text = "123"

num = int(text)

print(num)
print(type(num))


# ============================================================
# 125. INTEGER TO STRING
# ============================================================

num = 123

text = str(num)

print(text)
print(type(text))


# ============================================================
# 126. STRING TO FLOAT
# ============================================================

text = "123.45"

num = float(text)

print(num)


# ============================================================
# 127. INTEGER TO ASCII CHARACTER
# ============================================================

print(chr(65))


# ============================================================
# 128. ASCII CHARACTER TO INTEGER
# ============================================================

print(ord("A"))


# ============================================================
# 129. ALPHABET CHECK
# ============================================================

char = "A"

if "a" <= char.lower() <= "z":
    print("Alphabet")


# ============================================================
# 130. LOWERCASE ASCII CHECK
# ============================================================

char = "g"

if "a" <= char <= "z":
    print("Lowercase")


# ============================================================
# 131. UPPERCASE ASCII CHECK
# ============================================================

char = "G"

if "A" <= char <= "Z":
    print("Uppercase")


# ============================================================
# 132. DIGIT ASCII CHECK
# ============================================================

char = "7"

if "0" <= char <= "9":
    print("Digit")


"""
This is important in DSA.

Characters can be compared based on Unicode code points.
"""


# ============================================================
# 133. CHARACTER FREQUENCY USING ASCII ARRAY
# ============================================================

text = "banana"

frequency = [0] * 26

for char in text:

    index = ord(char) - ord("a")

    frequency[index] += 1

print(frequency)


"""
This technique is extremely important for coding interviews.

Instead of dictionary:

    frequency = {}

we can use:

    frequency = [0] * 26

when input contains only lowercase English letters.

This gives O(1) extra space because 26 is constant.
"""


# ============================================================
# 134. CHECK ANAGRAM USING 26 ARRAY
# ============================================================

a = "listen"
b = "silent"

if len(a) != len(b):

    print("Not Anagram")

else:

    frequency = [0] * 26

    for char in a:
        frequency[ord(char) - ord("a")] += 1

    for char in b:
        frequency[ord(char) - ord("a")] -= 1

    if all(value == 0 for value in frequency):
        print("Anagram")
    else:
        print("Not Anagram")


# ============================================================
# 135. STRING BUILDER PATTERN
# ============================================================

text = "hello"

result = []

for char in text:

    if char != "l":
        result.append(char)

result = "".join(result)

print(result)


"""
When constructing a large string repeatedly,
building a list and joining it can be preferable
to repeated string concatenation.
"""


# ============================================================
# 136. STRING COMPARISON IGNORING CASE
# ============================================================

a = "Python"
b = "python"

if a.lower() == b.lower():
    print("Same")


# Better Unicode-aware comparison:

if a.casefold() == b.casefold():
    print("Same")


# ============================================================
# 137. STRING INTERNING - INTERVIEW CONCEPT
# ============================================================

a = "hello"
b = "hello"

print(a == b)
print(a is b)


"""
==

Checks VALUE equality.


is

Checks OBJECT IDENTITY.

Do NOT use 'is' to compare string values.

Use:

    ==

instead.
"""


# ============================================================
# 138. STRING OBJECT ID
# ============================================================

text = "Python"

print(id(text))


"""
id() returns the identity of the object during its lifetime.
"""


# ============================================================
# 139. STRING METHODS - QUICK LIST
# ============================================================

"""
CASE:

    lower()
    upper()
    capitalize()
    title()
    swapcase()
    casefold()


SEARCH:

    find()
    rfind()
    index()
    rindex()
    count()
    startswith()
    endswith()


MODIFICATION / CREATION:

    replace()
    strip()
    lstrip()
    rstrip()
    removeprefix()
    removesuffix()


SPLITTING:

    split()
    rsplit()
    splitlines()
    partition()
    rpartition()


JOINING:

    join()


CHECKING:

    isalpha()
    isdigit()
    isdecimal()
    isnumeric()
    isalnum()
    isspace()
    islower()
    isupper()
    istitle()
    isidentifier()
    isprintable()


FORMATTING:

    format()
    f-string
    center()
    ljust()
    rjust()
    zfill()


ENCODING:

    encode()
    decode()


TRANSLATION:

    translate()
    maketrans()
"""


# ============================================================
# 140. IMPORTANT DIFFERENCES
# ============================================================

"""
find() vs index()

find():

    not found -> -1

index():

    not found -> ValueError


------------------------------------------------------------

remove() vs replace()

remove() is NOT a string method.

Strings use:

    replace()


------------------------------------------------------------

split() vs join()

split():

    string -> list

join():

    iterable of strings -> string


Example:

    "a,b,c".split(",")

    ["a", "b", "c"]


    ",".join(["a", "b", "c"])

    "a,b,c"


------------------------------------------------------------

lower() vs casefold()

lower():

    normal lowercase conversion


casefold():

    stronger Unicode-aware case-insensitive comparison


------------------------------------------------------------

strip() vs replace()

strip():

    removes characters from beginning/end


replace():

    replaces occurrences throughout the string
"""


# ============================================================
# 141. STRING COMPLEXITY
# ============================================================

"""
For a string of length n:

Index access:

    s[i] -> O(1)


len():

    O(1)


Search:

    x in s -> O(n) worst case


find():

    generally O(n)


count():

    O(n) approximately


Slicing:

    s[a:b] -> O(k)

where k is size of resulting substring.


lower():

    O(n)


upper():

    O(n)


replace():

    O(n) approximately


split():

    O(n)


join():

    O(total characters)


Reverse:

    s[::-1] -> O(n)

because a new string is created.


IMPORTANT:

Strings are immutable, so operations that appear
to modify strings usually create new strings.
"""


# ============================================================
# 142. IMPORTANT DSA STRING PATTERNS
# ============================================================

"""
You should learn these patterns:

1. Two Pointers

2. Frequency Dictionary

3. Frequency Array

4. Set for duplicates

5. Sliding Window

6. Prefix/Suffix

7. String parsing

8. Sorting

9. Stack with strings

10. Hashing


These appear frequently in coding interviews.
"""


# ============================================================
# 143. TWO POINTER TEMPLATE
# ============================================================

"""
left = 0
right = len(s) - 1

while left < right:

    # process s[left] and s[right]

    left += 1
    right -= 1
"""


# ============================================================
# 144. FREQUENCY DICTIONARY TEMPLATE
# ============================================================

"""
frequency = {}

for char in s:

    frequency[char] = frequency.get(char, 0) + 1
"""


# ============================================================
# 145. FREQUENCY ARRAY TEMPLATE
# ============================================================

"""
frequency = [0] * 26

for char in s:

    frequency[ord(char) - ord('a')] += 1
"""


# ============================================================
# 146. SET TEMPLATE
# ============================================================

"""
seen = set()

for char in s:

    if char in seen:
        # duplicate

    seen.add(char)
"""


# ============================================================
# 147. SLIDING WINDOW IDEA
# ============================================================

"""
Sliding window is very important for string DSA.

Example:

    "abcabcbb"

Find longest substring without repeating characters.

Typical tools:

    set
    two pointers
    while loop
"""


# ============================================================
# 148. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ============================================================

s = "abcabcbb"

seen = set()

left = 0
longest = 0

for right in range(len(s)):

    while s[right] in seen:

        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    longest = max(longest, right - left + 1)

print("Longest substring:", longest)


"""
Very important DSA pattern:

    Sliding Window + Set
"""


# ============================================================
# 149. STRING SLICING DSA PATTERNS
# ============================================================

s = "abcdef"

print(s[:3])
print(s[3:])
print(s[::-1])
print(s[::2])
print(s[1::2])


# ============================================================
# 150. COMMON STRING INTERVIEW PROBLEMS
# ============================================================

"""
BEGINNER:

1. Reverse a string
2. Check palindrome
3. Count vowels
4. Count consonants
5. Count digits
6. Count spaces
7. Find string length
8. Convert uppercase/lowercase
9. Remove spaces
10. Remove duplicate characters


INTERMEDIATE:

11. Valid Palindrome
12. Valid Anagram
13. First Unique Character
14. First Repeating Character
15. Longest Common Prefix
16. Reverse Words in a String
17. Longest Substring Without Repeating Characters
18. Group Anagrams
19. String Compression
20. Isomorphic Strings


ADVANCED:

21. Minimum Window Substring
22. Longest Palindromic Substring
23. Longest Repeating Character Replacement
24. Permutation in String
25. Find All Anagrams in a String
26. Word Break
27. Edit Distance
28. Regular Expression Matching
"""


# ============================================================
# 151. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a string?

A:

A sequence of Unicode characters.


------------------------------------------------------------

Q2. Are strings mutable?

A:

No.

Strings are immutable.


------------------------------------------------------------

Q3. Does Python have a char data type?

A:

No.

A single character is a string of length 1.


------------------------------------------------------------

Q4. Can strings contain duplicate characters?

A:

Yes.


------------------------------------------------------------

Q5. Does string support indexing?

A:

Yes.


------------------------------------------------------------

Q6. Does string support slicing?

A:

Yes.


------------------------------------------------------------

Q7. How do you reverse a string?

A:

    s[::-1]


------------------------------------------------------------

Q8. Difference between find() and index()?

A:

find():

    returns -1 if not found.


index():

    raises ValueError.


------------------------------------------------------------

Q9. How do you check if a substring exists?

A:

    substring in string


------------------------------------------------------------

Q10. How do you remove whitespace from both ends?

A:

    strip()


------------------------------------------------------------

Q11. Difference between split() and join()?

A:

split:

    string -> list


join:

    iterable -> string


------------------------------------------------------------

Q12. How do you count occurrences?

A:

    s.count("x")


------------------------------------------------------------

Q13. Why can't we modify:

    s[0]

A:

Because strings are immutable.


------------------------------------------------------------

Q14. How do you convert string to integer?

A:

    int(s)


------------------------------------------------------------

Q15. How do you convert integer to string?

A:

    str(n)


------------------------------------------------------------

Q16. What does ord() do?

A:

Character -> Unicode code point.


------------------------------------------------------------

Q17. What does chr() do?

A:

Unicode code point -> character.


------------------------------------------------------------

Q18. Difference between == and is?

A:

== compares values.

is compares object identity.


------------------------------------------------------------

Q19. What is string interning?

A:

Python may reuse certain immutable string objects
to save memory and improve efficiency.

Do not rely on this for value comparison.


------------------------------------------------------------

Q20. What is the time complexity of s[i]?

A:

O(1).


------------------------------------------------------------

Q21. What is the time complexity of searching a character?

A:

O(n) in the general case.


------------------------------------------------------------

Q22. What data structure is commonly used for character frequency?

A:

Dictionary / Counter.

For lowercase English letters,
a 26-element array is also common.
"""


# ============================================================
# 152. VERY IMPORTANT DSA CHEAT SHEET
# ============================================================

"""
REVERSE:

    s[::-1]


LENGTH:

    len(s)


SEARCH:

    x in s


COUNT:

    s.count(x)


FIRST INDEX:

    s.find(x)


LAST INDEX:

    s.rfind(x)


LOWERCASE:

    s.lower()


UPPERCASE:

    s.upper()


REMOVE OUTER SPACES:

    s.strip()


REPLACE:

    s.replace(a, b)


SPLIT:

    s.split()


JOIN:

    " ".join(words)


CHARACTER -> NUMBER:

    ord(c)


NUMBER -> CHARACTER:

    chr(n)


PALINDROME:

    s == s[::-1]


SORTED CHARACTERS:

    sorted(s)


ANAGRAM:

    Counter(a) == Counter(b)


UNIQUE CHARACTERS:

    set(s)


ALL UNIQUE:

    len(s) == len(set(s))


REVERSE LOOP:

    for i in range(len(s)-1, -1, -1):
        print(s[i])


FREQUENCY:

    freq[c] = freq.get(c, 0) + 1


ASCII ARRAY:

    freq[ord(c) - ord('a')] += 1
"""


# ============================================================
# 153. MOST IMPORTANT THINGS FOR YOUR DSA
# ============================================================

"""
DO NOT JUST MEMORIZE STRING METHODS.

For DSA, MASTER THESE:

                    STRING
                       |
        +--------------+--------------+
        |              |              |
   Two Pointer    Hashing/Frequency  Sliding Window
        |              |              |
   Palindrome       Anagram        Substrings
   Reverse          Duplicates     Longest Window
   Comparison       Counting       Minimum Window


And understand:

    String
       |
       +-- List
       |
       +-- Set
       |
       +-- Dictionary
       |
       +-- Stack
       |
       +-- Two Pointers
       |
       +-- Sliding Window


These concepts together form a huge portion
of beginner/intermediate string DSA problems.
"""


# ============================================================
# 154. FINAL REMINDER
# ============================================================

"""
MOST IMPORTANT STRING METHODS TO REMEMBER:

    len()
    lower()
    upper()
    strip()
    split()
    join()
    replace()
    find()
    count()
    startswith()
    endswith()
    isalpha()
    isdigit()
    isalnum()
    ord()
    chr()


MOST IMPORTANT DSA TECHNIQUES:

    s[::-1]
    x in s
    set(s)
    Counter(s)
    dictionary frequency
    26-element frequency array
    two pointers
    sliding window
    sorting
    substring processing


MOST IMPORTANT CONCEPT:

    STRINGS ARE IMMUTABLE.


For coding interviews, don't try to memorize every
string method. Understand what problem each technique
solves and practice implementing it.
"""

target = 10
ch = '1'
# 1. Reverse
s[::-1]

# 2. Palindrome
s == s[::-1]

# 3. Count characters
from collections import Counter
Counter(s)

# 4. Check duplicates
len(s) != len(set(s))

# 5. Remove duplicates
set(s)

# 6. Anagram
Counter(a) == Counter(b)

# 7. Split words
s.split()

# 8. Join words
" ".join(words)

# 9. Character -> ASCII/Unicode
ord('a')

# 10. ASCII/Unicode -> character
chr(97)

# 11. Frequency array
freq = [0] * 26
freq[ord(ch) - ord('a')] += 1

# 12. Two pointer
left = 0
right = len(s) - 1

# 13. Sliding window
seen = set()
left = 0

# 14. Substring search
if target in s:
    print("Found")



print("\n================================================")
print("           STRING LEARNING COMPLETE")
print("================================================")