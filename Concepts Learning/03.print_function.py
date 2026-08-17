# ============================================================
#                    PRINT STATEMENT IN PYTHON
#       Complete Notes + Examples + Interview Preparation
# ============================================================

"""
print() is a built-in Python function used to display
output on the screen.

Basic syntax:

print(object1, object2, ..., sep=' ', end='\n')

Important parameters:

1. objects -> Values that we want to print
2. sep     -> Separator between multiple objects
3. end     -> What should be printed at the end
4. file    -> Where output should be sent
5. flush   -> Whether output should be flushed immediately
"""


# ============================================================
# 1. BASIC PRINT
# ============================================================

print("Hello World")

print(10)

print(10.5)

print(True)


# ============================================================
# 2. PRINT VARIABLES
# ============================================================

name = "Harshad"
age = 21
is_student = True

print(name)
print(age)
print(is_student)


# ============================================================
# 3. PRINT LABEL + VARIABLE
# ============================================================

print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)


# Output:
# Name: Harshad
# Age: 21
# Is Student: True


# ============================================================
# 4. PRINT MULTIPLE VALUES
# ============================================================

print("Name:", name, "Age:", age, "Is Student:", is_student)


"""
By default, print() separates multiple values with a space.

Therefore:

print("Hello", "World")

produces:

Hello World
"""


# ============================================================
# 5. sep PARAMETER
# ============================================================

"""
sep means separator.

Default:

sep = " "
"""

print(name, age, is_student)

# Output:
# Harshad 21 True


# Custom separator:

print(name, age, is_student, sep=", ")

# Harshad, 21, True


print(name, age, is_student, sep=" | ")

# Harshad | 21 | True


print(name, age, is_student, sep=" - ")

# Harshad - 21 - True


# ============================================================
# 6. sep WITH NEWLINE
# ============================================================

print(name, age, is_student, sep="\n")


"""
Output:

Harshad
21
True
"""


# ============================================================
# 7. end PARAMETER
# ============================================================

"""
By default:

end = "\n"

So print() moves to a new line after printing.
"""

print("Hello")
print("World")


# Output:
# Hello
# World


# ============================================================
# 8. CUSTOM end
# ============================================================

print("Hello", end=" ")
print("World")

# Output:
# Hello World


print("Hello", end="!!!")
print("World")

# Output:
# Hello!!!World


# ============================================================
# 9. end WITH NEWLINE
# ============================================================

print("Hello", end="\n")
print("World")


# ============================================================
# 10. sep AND end TOGETHER
# ============================================================

print(name, age, is_student, sep=" - ", end=".\n")

# Output:
# Harshad - 21 - True.


# ============================================================
# 11. F-STRING - RECOMMENDED
# ============================================================

"""
F-strings are one of the best and most readable ways
to format strings in modern Python.

Syntax:

f"Text {variable}"
"""

print(f"Name: {name} Age: {age} Is Student: {is_student}")


# ============================================================
# 12. F-STRING WITH SEPARATE LINES
# ============================================================

print(f"Name: {name}\nAge: {age}\nIs Student: {is_student}")


# ============================================================
# 13. F-STRING EXPRESSIONS
# ============================================================

a = 10
b = 20

print(f"Sum = {a + b}")

print(f"Product = {a * b}")

print(f"Average = {(a + b) / 2}")


# ============================================================
# 14. F-STRING WITH FORMATTING
# ============================================================

percentage = 97.85678

print(f"Percentage: {percentage:.2f}")


"""
:.2f

means:

2 digits after decimal point.

97.85678

becomes:

97.86
"""


# ============================================================
# 15. F-STRING NUMBER FORMATTING
# ============================================================

number = 1234567

print(f"{number:,}")

# Output:
# 1,234,567


# ============================================================
# 16. F-STRING WIDTH / ALIGNMENT
# ============================================================

name = "Harshad"

print(f"{name:>10}")   # Right aligned
print(f"{name:<10}")   # Left aligned
print(f"{name:^10}")   # Center aligned


# ============================================================
# 17. str.format()
# ============================================================

"""
Older but still important formatting technique.
"""

print(
    "Name: {} Age: {} Is Student: {}".format(
        name,
        age,
        is_student
    )
)


# ============================================================
# 18. format() USING INDEX
# ============================================================

print(
    "Name: {0} Age: {1} Is Student: {2}".format(
        name,
        age,
        is_student
    )
)


# ============================================================
# 19. format() USING KEYWORD ARGUMENTS
# ============================================================

print(
    "Name: {name} Age: {age} Is Student: {is_student}".format(
        name=name,
        age=age,
        is_student=is_student
    )
)


# ============================================================
# 20. format() USING CUSTOM NAMES
# ============================================================

print(
    "Name: {n} Age: {a} Is Student: {s}".format(
        n=name,
        a=age,
        s=is_student
    )
)


# ============================================================
# 21. OLD % FORMATTING
# ============================================================

"""
Python also supports old-style % formatting.

%s -> string
%d -> integer
%f -> floating point
"""

print(
    "Name: %s Age: %d Is Student: %s"
    % (name, age, is_student)
)


# ============================================================
# 22. %f FLOAT FORMATTING
# ============================================================

percentage = 97.8567

print("Percentage: %f" % percentage)

print("Percentage: %.2f" % percentage)


# ============================================================
# 23. COMPARING FORMATTING METHODS
# ============================================================

"""
1. F-string       -> Modern + recommended
2. str.format()   -> Older but important
3. % formatting   -> Legacy, still seen in old code

For new Python code:

Prefer F-strings.
"""

print(f"Name: {name}, Age: {age}")

print("Name: {}, Age: {}".format(name, age))

print("Name: %s, Age: %d" % (name, age))


# ============================================================
# 24. STRING CONCATENATION WITH +
# ============================================================

"""
You can concatenate strings using +.

BUT all operands must be strings.
"""

print("Hello, " + name + "!")


# This causes TypeError:

# print("Age: " + age)


# Correct:

print("Age: " + str(age))


# ============================================================
# 25. + VS COMMA
# ============================================================

"""
Using +:

Both values must be strings.
"""

print("Hello " + name)


"""
Using comma:

Python automatically separates objects
and converts them for display.
"""

print("Hello", name)

print("Age:", age)


# ============================================================
# 26. PRINT EXPRESSIONS
# ============================================================

a = 10
b = 20

print(a + b)

print(a * b)

print(a > b)

print(a == b)


# ============================================================
# 27. PRINT LIST
# ============================================================

numbers = [10, 20, 30, 40]

print(numbers)


# ============================================================
# 28. PRINT TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers)


# ============================================================
# 29. PRINT SET
# ============================================================

numbers = {10, 20, 30, 40}

print(numbers)


# ============================================================
# 30. PRINT DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print(student)


# ============================================================
# 31. PRINT EACH LIST ELEMENT
# ============================================================

numbers = [10, 20, 30, 40]

for number in numbers:

    print(number)


# ============================================================
# 32. PRINT LIST ON ONE LINE
# ============================================================

numbers = [10, 20, 30, 40]

print(*numbers)


"""
Output:

10 20 30 40

The * unpacks the list.
"""


# ============================================================
# 33. LIST WITH CUSTOM SEPARATOR
# ============================================================

numbers = [10, 20, 30, 40]

print(*numbers, sep=", ")

# Output:
# 10, 20, 30, 40


# ============================================================
# 34. VERY USEFUL DSA TECHNIQUE
# ============================================================

"""
Suppose:

arr = [1, 2, 3, 4, 5]

To print:

1 2 3 4 5
"""

arr = [1, 2, 3, 4, 5]

print(*arr)


# Print with commas:

print(*arr, sep=", ")


# ============================================================
# 35. PRINT WITHOUT NEW LINE
# ============================================================

for i in range(5):

    print(i, end=" ")


# Output:
# 0 1 2 3 4


print()


# ============================================================
# 36. PRINT PATTERN USING end
# ============================================================

for i in range(1, 6):

    for j in range(1, 6):

        print("*", end=" ")

    print()


# Output:

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# ============================================================
# 37. PRINT PATTERN USING sep
# ============================================================

print(1, 2, 3, 4, 5, sep=" ")


# ============================================================
# 38. repr() VS str()
# ============================================================

"""
str() is generally intended for readable output.

repr() gives a representation useful for debugging
and often shows quotes/escape characters explicitly.
"""

text = "Hello\nWorld"

print(str(text))

print(repr(text))


"""
str(text):

Hello
World

repr(text):

'Hello\\nWorld'
"""


# ============================================================
# 39. print() AND repr()
# ============================================================

name = "Harshad"

print(name)

print(repr(name))


# ============================================================
# 40. PRINT MULTIPLE LINES
# ============================================================

print("""
Hello
My name is Harshad
I am learning Python
""")


# ============================================================
# 41. print() WITH ESCAPE SEQUENCES
# ============================================================

print("Hello\nWorld")

print("Hello\tWorld")

print("C:\\Users\\Harshad")


# ============================================================
# 42. PRINT SPECIAL CHARACTERS
# ============================================================

print("He said \"Hello\"")

print('It\'s Python')


# ============================================================
# 43. print() RETURN VALUE
# ============================================================

"""
IMPORTANT INTERVIEW QUESTION:

What does print() return?

Answer:

None
"""

result = print("Hello")

print(result)

# Output:
# Hello
# None


# ============================================================
# 44. print() RETURNS NONE
# ============================================================

result = print("Python")

print(type(result))

# <class 'NoneType'>


# ============================================================
# 45. print() WITH flush
# ============================================================

"""
flush=True forces the output to be flushed immediately.

Normally Python may buffer output.

This is useful in some situations involving:

- real-time output
- progress indicators
- long-running programs
"""

print("Processing...", flush=True)


# ============================================================
# 46. print() TO A FILE
# ============================================================

"""
The file parameter can redirect output.

Example:
"""

with open("output.txt", "w") as file:

    print("Hello Python", file=file)


"""
The output is written into:

output.txt
"""


# ============================================================
# 47. print() RETURN VALUE VS OUTPUT
# ============================================================

"""
Don't confuse:

print()

with:

return

print() -> displays something
return -> sends a value back from a function
"""

def add(a, b):

    print(a + b)


result = add(10, 20)

print("Result:", result)


"""
Output:

30
Result: None

Because the function printed the value
but did not return it.
"""


# ============================================================
# 48. print() VS return
# ============================================================

def add(a, b):

    return a + b


result = add(10, 20)

print("Result:", result)


"""
Here:

return -> gives the value to the caller.

print -> displays the value.
"""


# ============================================================
# 49. COMMON DSA USE
# ============================================================

arr = [10, 20, 30, 40, 50]

print(*arr)


# ============================================================
# 50. PRINT REVERSE ARRAY
# ============================================================

arr = [10, 20, 30, 40, 50]

print(*arr[::-1])


# ============================================================
# 51. PRINT ARRAY WITH CUSTOM SEPARATOR
# ============================================================

arr = [10, 20, 30, 40, 50]

print(*arr, sep=" -> ")


# Output:

# 10 -> 20 -> 30 -> 40 -> 50


# ============================================================
# 52. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is print()?

print() is a built-in Python function used to display output.


Q2. What is the default value of sep?

" " (a single space)


Q3. What is the default value of end?

"\\n"


Q4. What does print() return?

None


Q5. Difference between print() and return?

print() displays a value.

return sends a value back from a function.


Q6. What does sep do?

It specifies the separator between multiple objects
passed to print().


Q7. What does end do?

It specifies what should be printed after the objects.


Q8. How do you print without moving to a new line?

print("Hello", end="")


Q9. How do you print a list without brackets?

print(*arr)


Q10. What is the recommended way to format strings
in modern Python?

F-strings.


Q11. What is the difference between:

print("Age:", age)

and:

print("Age: " + str(age))

The first uses multiple print arguments.

The second concatenates strings.


Q12. Why does this fail?

print("Age: " + age)

Because age is an integer and + requires compatible
string operands in this case.


Q13. What does flush=True do?

It forces the output buffer to be flushed immediately.
"""


# ============================================================
# 53. QUICK REVISION
# ============================================================

"""
BASIC:

print("Hello")


MULTIPLE VALUES:

print("Name:", name, "Age:", age)


SEPARATOR:

print(1, 2, 3, sep=", ")


NO NEW LINE:

print("Hello", end=" ")


F-STRING:

print(f"Name: {name}, Age: {age}")


FORMAT:

print("Name: {} Age: {}".format(name, age))


OLD STYLE:

print("Name: %s Age: %d" % (name, age))


CONCATENATION:

print("Hello " + name)


LIST UNPACKING:

print(*arr)


LIST WITH SEPARATOR:

print(*arr, sep=", ")


DEBUGGING:

print(repr(value))


RETURN VALUE:

result = print("Hello")

result == None


FILE:

print("Hello", file=file)


IMMEDIATE OUTPUT:

print("Loading...", flush=True)
"""

arr = [1, 2, 3, 4, 5]
print(*arr)

x = print("Hello")
print(x) # None

# ============================================================
#                         END
# ============================================================