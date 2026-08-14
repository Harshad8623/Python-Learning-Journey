# ============================================================
#                  PYTHON ESCAPE SEQUENCES
# ============================================================

"""
Escape sequences are special character combinations
starting with a backslash (\).

They are used to represent special characters inside strings.

Example:

\n  -> New line
\t  -> Tab
\\  -> Backslash
\"  -> Double quote
\'  -> Single quote
"""


# ============================================================
# 1. NEW LINE \n
# ============================================================

"""
\n moves the cursor to the next line.
"""

print("Hello\nWorld")

# Output:
# Hello
# World


# ============================================================
# 2. TAB \t
# ============================================================

"""
\t inserts a horizontal tab.
"""

print("Hello\tWorld")

# Output looks approximately like:
# Hello   World


# Example:

print("Name\tAge\tCity")
print("Harshad\t21\tLatur")


# ============================================================
# 3. CARRIAGE RETURN \r
# ============================================================

"""
\r moves the cursor to the beginning of the
CURRENT line.

It does NOT necessarily create a new line.

Characters printed after \r can overwrite
characters already printed on that line.
"""

print("Hello\rWorld")


"""
Depending on the terminal, you may see:

World

because "World" overwrites "Hello".
"""


# ============================================================
# 4. BACKSPACE \b
# ============================================================

"""
\b moves the cursor one position backward.

Its visible behavior depends on the terminal.
"""

print("Hello\bWorld")


# Conceptually:

"""
Hello
    ^
Backspace moves one position backward.
"""


# ============================================================
# 5. FORM FEED \f
# ============================================================

"""
\f is the form-feed character.

Historically, it was used to move to the
next page in printers.

It is rarely needed in modern Python programs.
"""

print("Hello\fWorld")


# ============================================================
# 6. VERTICAL TAB \v
# ============================================================

"""
\v represents a vertical tab.

It is rarely used in normal Python programming.
"""

print("Hello\vWorld")


# ============================================================
# 7. BELL / ALERT \a
# ============================================================

"""
\a represents the ASCII bell character.

Some terminals may produce a beep,
while others may show no visible effect.
"""

print("Hello\aWorld")


# ============================================================
# 8. BACKSLASH \\
# ============================================================

"""
\\ is used when we want to print an actual
backslash character.
"""

print("Hello\\World")

# Output:
# Hello\World


# ============================================================
# 9. SINGLE QUOTE \'
# ============================================================

"""
\' allows us to include a single quote
inside a single-quoted string.
"""

print('Hello\'World')

# Output:
# Hello'World


# Without escaping, this causes a problem:

# print('Hello'World')

# SyntaxError


# ============================================================
# 10. DOUBLE QUOTE \"
# ============================================================

"""
\" allows us to include a double quote
inside a double-quoted string.
"""

print("Hello\"World")

# Output:
# Hello"World


# Without escaping:

# print("Hello"World")

# SyntaxError


# ============================================================
# 11. USING SINGLE QUOTES WITHOUT ESCAPING
# ============================================================

"""
If the outer string uses double quotes,
a single quote usually doesn't need escaping.
"""

print("It's Python")


# ============================================================
# 12. USING DOUBLE QUOTES WITHOUT ESCAPING
# ============================================================

"""
If the outer string uses single quotes,
a double quote usually doesn't need escaping.
"""

print('He said "Hello"')


# ============================================================
# 13. MIXED QUOTES
# ============================================================

print("He said 'Hello'")

print('He said "Hello"')


# ============================================================
# 14. COMBINING ESCAPE SEQUENCES
# ============================================================

print("Hello\nWorld\tPython")


# ============================================================
# 15. MULTIPLE NEW LINES
# ============================================================

print("Hello\n\nWorld")


# Output:

"""
Hello

World
"""


# ============================================================
# 16. TAB + NEW LINE
# ============================================================

print("Name:\tHarshad\nAge:\t21")


# ============================================================
# 17. BACKSPACE + TAB
# ============================================================

print("Hello\t\bWorld")


"""
The exact visible result can vary depending on
the terminal because \b moves the cursor backward.
"""


# ============================================================
# 18. ESCAPE SEQUENCES INSIDE VARIABLES
# ============================================================

message = "Hello\nWorld"

print(message)


# ============================================================
# 19. ESCAPE SEQUENCES WITH f-STRINGS
# ============================================================

name = "Harshad"
age = 21

print(f"Name:\t{name}\nAge:\t{age}")


# ============================================================
# 20. RAW STRINGS
# ============================================================

"""
Prefixing a string with r creates a raw string.

Escape sequences are generally treated literally.

Example:

r"\n"

prints the characters:

\n

instead of creating a new line.
"""

print(r"\n")

print(r"Hello\nWorld")


# Normal string:

print("Hello\nWorld")


# Raw string:

print(r"Hello\nWorld")


# ============================================================
# 21. RAW STRING - WINDOWS PATH
# ============================================================

"""
Raw strings are particularly useful for
Windows file paths.
"""

path = r"C:\Users\Harshad\Documents\Python"

print(path)


# Without raw string:

path = "C:\\Users\\Harshad\\Documents\\Python"

print(path)


"""
Both can represent:

C:\Users\Harshad\Documents\Python
"""


# ============================================================
# 22. IMPORTANT: RAW STRING LIMITATION
# ============================================================

"""
A raw string cannot normally end with a single
backslash.

Wrong:

# path = r"C:\Users\Harshad\"


Instead:

path = r"C:\Users\Harshad" + "\\"

"""


# ============================================================
# 23. UNICODE ESCAPE \u
# ============================================================

"""
\u is used to represent a Unicode character
using 4 hexadecimal digits.
"""

print("\u0041")

# Output:
# A


print("\u2764")

# Output:
# ❤


# ============================================================
# 24. UNICODE ESCAPE \U
# ============================================================

"""
\U uses 8 hexadecimal digits.
"""

print("\U0001F600")

# 😀


# ============================================================
# 25. HEX ESCAPE \x
# ============================================================

"""
\x is used to represent a character using
two hexadecimal digits.
"""

print("\x41")

# Output:
# A


print("\x48\x69")

# Output:
# Hi


# ============================================================
# 26. OCTAL ESCAPE
# ============================================================

"""
Python also supports octal escape sequences.

Example:

\101

represents the character A.
"""

print("\101")


# ============================================================
# 27. COMMON ESCAPE SEQUENCES TABLE
# ============================================================

"""
Escape       Meaning

\\n          New line
\\t          Horizontal tab
\\r          Carriage return
\\b          Backspace
\\f          Form feed
\\v          Vertical tab
\\a          Bell / alert
\\\\          Backslash
\\'          Single quote
\\"          Double quote
\\uXXXX      Unicode character (4 hex digits)
\\UXXXXXXXX  Unicode character (8 hex digits)
\\xXX        Character using hexadecimal value
\\ooo        Character using octal value
"""


# ============================================================
# 28. MOST IMPORTANT ESCAPE SEQUENCES
# ============================================================

"""
For everyday Python programming, focus mainly on:

\\n   -> New line
\\t   -> Tab
\\\\   -> Backslash
\\'   -> Single quote
\\"   -> Double quote

Also know:

\\r
\\b
\\u
\\U
\\x

The others are much less commonly used.
"""


# ============================================================
# 29. INTERVIEW QUESTION
# ============================================================

"""
Q: What is an escape sequence?

Answer:

An escape sequence is a special sequence of characters
beginning with a backslash (\\) that represents a special
character or behavior inside a string.
"""


# ============================================================
# 30. INTERVIEW QUESTION
# ============================================================

"""
Q: Why do we use \\n?

Answer:

It represents a newline character and moves the cursor
to the next line.
"""


# ============================================================
# 31. INTERVIEW QUESTION
# ============================================================

"""
Q: Difference between \\n and \\t?

\\n -> New line
\\t -> Horizontal tab
"""


# ============================================================
# 32. INTERVIEW QUESTION
# ============================================================

"""
Q: What is a raw string?

Answer:

A raw string is created using the r or R prefix.

It treats backslashes mostly as literal characters
instead of interpreting them as escape sequences.

Example:

r"C:\Users\Harshad"
"""


# ============================================================
# 33. INTERVIEW QUESTION
# ============================================================

"""
Q: How can you print a backslash?

Use:

\\\\

Example:

print("\\\\")

Output:

\
"""


# ============================================================
# 34. INTERVIEW QUESTION
# ============================================================

"""
Q: How can you print quotes inside a string?

Use escaping:

\\'
\\"

Or use the opposite type of quotation mark.

Example:

print("It's Python")

print('He said "Hello"')
"""


# ============================================================
# 35. ESCAPE SEQUENCES + DSA
# ============================================================

"""
Escape sequences are not a major DSA topic.

However, they are useful when handling:

- strings
- input/output
- formatting
- file paths
- text processing
- parsing

For coding rounds, \\n and \\t are the most useful.
"""


# ============================================================
# 36. QUICK PRACTICE
# ============================================================

"""
Try predicting the output before running each one:

1.
print("Hello\nWorld")

2.
print("Hello\tWorld")

3.
print("A\\B\\C")

4.
print("He said \"Python\"")

5.
print('It\\'s Python')

6.
print(r"Hello\nWorld")

7.
print("\u0041")

8.
print("\x41")
"""


# ============================================================
#                         END
# ============================================================