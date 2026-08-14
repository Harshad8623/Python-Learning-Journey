# ============================================================
#                       PYTHON OPERATORS
# ============================================================

"""
Operators are symbols/keywords used to perform operations
on values and variables.

Main categories of Python operators:

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Membership Operators
7. Identity Operators
8. Unary Operators
9. Conditional Expression
10. Walrus Operator
11. Matrix Multiplication Operator
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

"""
+       Addition
-       Subtraction
*       Multiplication
/       Division
//      Floor Division
%       Modulus
**      Exponentiation
"""

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# ============================================================
# 2. ADDITION
# ============================================================

print(10 + 5)

# Strings can also be concatenated using +

print("Hello " + "Harshad")


# ============================================================
# 3. SUBTRACTION
# ============================================================

print(10 - 5)


# ============================================================
# 4. MULTIPLICATION
# ============================================================

print(10 * 5)

# String repetition

print("Python " * 3)


# ============================================================
# 5. DIVISION /
# ============================================================

"""
/ always returns a floating-point result.
"""

print(10 / 2)
print(5 / 2)

# Output:
# 5.0
# 2.5


# ============================================================
# 6. FLOOR DIVISION //
# ============================================================

"""
// performs floor division.

It returns the FLOOR of the result.

Important:
It does NOT simply remove the decimal portion.
"""

print(5 // 2)      # 2
print(7 // 3)      # 2
print(29 // 10)    # 2

print(-5 // 2)     # -3


"""
Why?

-5 / 2 = -2.5

Floor of -2.5 = -3

Therefore:

-5 // 2 = -3
"""


# ============================================================
# 7. int() VS FLOOR DIVISION
# ============================================================

"""
int() truncates toward ZERO.

It does NOT perform mathematical floor.
"""

print(int(2.98))      # 2
print(int(-2.98))     # -2

print(2.98 // 1)      # 2.0
print(-2.98 // 1)     # -3.0


# VERY IMPORTANT:

"""
int(-2.98) = -2
-2.98 // 1 = -3.0

They are NOT the same operation.
"""


# ============================================================
# 8. MODULUS %
# ============================================================

"""
% returns the remainder.
"""

print(10 % 3)       # 1
print(15 % 5)       # 0
print(29 % 10)      # 9


# ============================================================
# 9. MODULUS - DSA IMPORTANCE
# ============================================================

"""
% is extremely important in DSA.

Common uses:

- Even / odd
- Divisibility
- Digit extraction
- Circular arrays
- Hashing
- Number problems
"""

num = 10

if num % 2 == 0:

    print("Even")

else:

    print("Odd")


# Extract last digit

num = 12345

print(num % 10)     # 5


# ============================================================
# 10. EXPONENTIATION **
# ============================================================

print(2 ** 3)       # 8
print(5 ** 2)       # 25
print(10 ** 0)      # 1


# ============================================================
# 11. COMPARISON OPERATORS
# ============================================================

"""
Comparison operators return True or False.

==      Equal
!=      Not equal
>       Greater than
<       Less than
>=      Greater than or equal to
<=      Less than or equal to
"""

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ============================================================
# 12. = VS ==
# ============================================================

"""
=  -> Assignment

== -> Comparison
"""

x = 10

if x == 10:

    print("x is 10")


# ============================================================
# 13. CHAINED COMPARISON
# ============================================================

"""
Python allows chained comparisons.
"""

age = 25

if 18 <= age <= 60:

    print("Age is between 18 and 60.")


# Equivalent to:

if age >= 18 and age <= 60:

    print("Valid age.")


# ============================================================
# 14. LOGICAL OPERATORS
# ============================================================

"""
and
or
not
"""

x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)


# ============================================================
# 15. AND
# ============================================================

"""
and returns True only when BOTH conditions are True.

True  and True   -> True
True  and False  -> False
False and True   -> False
False and False  -> False
"""

age = 25
has_id = True

if age >= 18 and has_id:

    print("Entry allowed.")


# ============================================================
# 16. OR
# ============================================================

"""
or returns True when at least one condition is True.

True  or True   -> True
True  or False  -> True
False or True   -> True
False or False  -> False
"""

day = "Sunday"

if day == "Saturday" or day == "Sunday":

    print("Weekend")


# ============================================================
# 17. NOT
# ============================================================

"""
not reverses a Boolean value.

not True  -> False
not False -> True
"""

is_raining = False

if not is_raining:

    print("Go outside.")


# ============================================================
# 18. IMPORTANT: and / or RETURN VALUES
# ============================================================

"""
This is an important Python interview concept.

and and or don't necessarily return True/False.

They can return one of the operands.
"""

print(10 and 20)
print(0 and 20)

print(10 or 20)
print(0 or 20)


"""
Output:

20
0

10
20
"""


# ============================================================
# 19. SHORT-CIRCUIT EVALUATION
# ============================================================

"""
Python uses short-circuit evaluation.

AND:

If the first value is falsy,
Python doesn't need to evaluate the second.

OR:

If the first value is truthy,
Python doesn't need to evaluate the second.
"""

x = 0

result = x and 100

print(result)


# ============================================================
# 20. BITWISE OPERATORS
# ============================================================

"""
Bitwise operators work on binary representation.

&   Bitwise AND
|   Bitwise OR
^   Bitwise XOR
~   Bitwise NOT
<<  Left Shift
>>  Right Shift
"""

p = 5
q = 3

"""
5 = 0101
3 = 0011
"""


print("AND:", p & q)
print("OR:", p | q)
print("XOR:", p ^ q)
print("NOT:", ~p)
print("Left Shift:", p << 1)
print("Right Shift:", p >> 1)


# ============================================================
# 21. BITWISE AND
# ============================================================

"""
0101
0011
----
0001

Result = 1
"""

print(5 & 3)


# ============================================================
# 22. BITWISE OR
# ============================================================

"""
0101
0011
----
0111

Result = 7
"""

print(5 | 3)


# ============================================================
# 23. BITWISE XOR
# ============================================================

"""
0101
0011
----
0110

Result = 6
"""

print(5 ^ 3)


# ============================================================
# 24. XOR IMPORTANT DSA PROPERTY
# ============================================================

"""
XOR properties:

x ^ x = 0
x ^ 0 = x

This is heavily used in DSA problems.
"""

print(5 ^ 5)     # 0
print(5 ^ 0)     # 5


# ============================================================
# 25. BITWISE NOT
# ============================================================

"""
~x = -(x + 1)

Therefore:

~5 = -6
"""

print(~5)
print(~10)


# ============================================================
# 26. LEFT SHIFT <<
# ============================================================

"""
Left shift moves bits to the left.

For positive integers:

x << n

is equivalent to:

x * (2 ** n)
"""

print(5 << 1)    # 10
print(5 << 2)    # 20


# ============================================================
# 27. RIGHT SHIFT >>
# ============================================================

"""
Right shift moves bits to the right.

For positive integers:

x >> n

is approximately:

x // (2 ** n)
"""

print(20 >> 1)   # 10
print(20 >> 2)   # 5


# ============================================================
# 28. ASSIGNMENT OPERATORS
# ============================================================

"""
=
+=
-=
*=
/=
%=
**=
//=
&=
|=
^=
<<=
>>=
"""

x = 10

x += 5
print(x)

x -= 5
print(x)

x *= 2
print(x)

x /= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)

x //= 2
print(x)


# ============================================================
# 29. BITWISE ASSIGNMENT
# ============================================================

x = 10

x &= 3
print(x)

x |= 3
print(x)

x ^= 3
print(x)


# ============================================================
# 30. SHIFT ASSIGNMENT
# ============================================================

x = 5

x <<= 1

print(x)


x >>= 1

print(x)


# ============================================================
# 31. MEMBERSHIP OPERATORS
# ============================================================

"""
in
not in

Used to check whether a value exists
inside an iterable.
"""

numbers = [1, 2, 3, 4, 5]

print(3 in numbers)
print(10 in numbers)

print(10 not in numbers)


# ============================================================
# 32. MEMBERSHIP WITH STRING
# ============================================================

name = "Harshad"

print("H" in name)
print("z" in name)


# ============================================================
# 33. MEMBERSHIP WITH DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

"""
For dictionaries:

in checks KEYS by default.
"""

print("name" in student)
print("Harshad" in student)


# ============================================================
# 34. IDENTITY OPERATORS
# ============================================================

"""
is
is not

Identity checks whether two variables
refer to the SAME OBJECT.
"""

a = [1, 2, 3]

b = a

c = [1, 2, 3]

print(a is b)
print(a is c)


# ============================================================
# 35. == VS is
# ============================================================

"""
==

Checks value equality.


is

Checks object identity.
"""

x = [10, 20]
y = [10, 20]

print(x == y)      # True
print(x is y)      # False


# ============================================================
# 36. IDENTITY WITH None
# ============================================================

"""
Recommended:

if value is None:

NOT:

if value == None:
"""

value = None

if value is None:

    print("Value is None.")


# ============================================================
# 37. UNARY OPERATORS
# ============================================================

"""
Unary operators operate on ONE operand.

+   Unary plus
-   Unary minus
~   Bitwise NOT
not Logical NOT
"""

x = 10

print(+x)
print(-x)
print(~x)
print(not x)


# ============================================================
# 38. CONDITIONAL EXPRESSION
# ============================================================

"""
Also called:

- Ternary operator
- Conditional expression

Syntax:

value_if_true if condition else value_if_false
"""

num = 10

result = "Even" if num % 2 == 0 else "Odd"

print(result)


# ============================================================
# 39. WALRUS OPERATOR :=
# ============================================================

"""
:= is called the WALRUS OPERATOR.

It assigns a value AND allows that value
to be used inside an expression.

Introduced in Python 3.8.
"""

if (n := len("Python")) > 5:

    print("Length:", n)


# Another example:

while (text := input("Enter text (type exit to stop): ")) != "exit":

    print("You entered:", text)


# ============================================================
# 40. MATRIX MULTIPLICATION @
# ============================================================

"""
@ is the matrix multiplication operator.

It is mainly used with libraries such as NumPy.

Example:

A @ B

means matrix multiplication.
"""

# Example conceptually:

"""
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = A @ B

print(C)
"""


# ============================================================
# 41. OPERATOR PRECEDENCE
# ============================================================

"""
When multiple operators are used,
Python follows operator precedence.

A simplified order is:

1. Parentheses ()
2. Exponentiation **
3. Unary +, -, ~
4. *, /, //, %
5. +, -
6. <<, >>
7. &
8. ^
9. |
10. Comparisons
11. not
12. and
13. or
14. Conditional expression
15. Assignment / walrus depending on context

IMPORTANT:

Use parentheses when the expression is complicated.
"""

result = 10 + 5 * 2

print(result)

# 5 * 2 happens first
# 10 + 10
# Result = 20


# ============================================================
# 42. PARENTHESES CHANGE PRECEDENCE
# ============================================================

result = (10 + 5) * 2

print(result)

# 15 * 2
# 30


# ============================================================
# 43. EXPONENTIATION PRECEDENCE
# ============================================================

result = 2 + 3 ** 2

print(result)

# 3 ** 2 = 9
# 2 + 9 = 11


# ============================================================
# 44. MODULUS + CONDITIONAL
# ============================================================

num = 25

if num % 5 == 0:

    print("Divisible by 5.")


# ============================================================
# 45. OPERATORS IN DSA
# ============================================================

"""
Operators are extremely important in DSA.

Common examples:

%   -> Even/odd, divisibility, digits
//  -> Integer division
==  -> Searching/comparison
>   -> Finding maximum
<   -> Finding minimum
+=  -> Running sum
-=  -> Sliding window
^   -> XOR problems
&   -> Bit manipulation
<<  -> Bit manipulation
>>  -> Bit manipulation
in  -> Searching / membership
"""


# ============================================================
# 46. DSA EXAMPLE - EVEN / ODD
# ============================================================

num = 17

if num % 2 == 0:

    print("Even")

else:

    print("Odd")


# ============================================================
# 47. DSA EXAMPLE - SUM
# ============================================================

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:

    total += num


print(total)


# ============================================================
# 48. DSA EXAMPLE - MAXIMUM
# ============================================================

numbers = [10, 50, 20, 80, 30]

maximum = numbers[0]

for num in numbers:

    if num > maximum:

        maximum = num


print(maximum)


# ============================================================
# 49. DSA EXAMPLE - TWO POINTER
# ============================================================

numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:

    print(numbers[left], numbers[right])

    left += 1
    right -= 1


# ============================================================
# 50. DSA EXAMPLE - DIGIT EXTRACTION
# ============================================================

num = 12345

last_digit = num % 10

print(last_digit)


# Remove last digit:

num = 12345

num = num // 10

print(num)


"""
This combination:

num % 10
num // 10

is extremely important for number-based
coding problems.
"""


# ============================================================
# 51. REVERSE NUMBER
# ============================================================

num = 12345

reverse = 0

while num > 0:

    digit = num % 10

    reverse = reverse * 10 + digit

    num //= 10


print(reverse)


# ============================================================
# 52. BIT MANIPULATION - CHECK ODD/EVEN
# ============================================================

"""
For integers:

n & 1

can be used to check whether n is odd.
"""

num = 7

if num & 1:

    print("Odd")

else:

    print("Even")


# ============================================================
# 53. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. How many main types of operators are there in Python?

Common categories:

Arithmetic
Comparison
Logical
Bitwise
Assignment
Membership
Identity


Q2. Difference between / and //?

/  -> Normal division, returns float.

// -> Floor division.


Q3. Difference between // and int()?

// performs floor.

int() truncates toward zero.


Q4. What does % return?

The remainder.


Q5. What is the use of % in DSA?

Even/odd
Divisibility
Digit extraction
Circular calculations
Hashing


Q6. Difference between = and ==?

=  -> assignment
== -> comparison


Q7. Difference between == and is?

== -> value equality
is -> object identity


Q8. What are logical operators?

and
or
not


Q9. What are membership operators?

in
not in


Q10. What are identity operators?

is
is not


Q11. What is XOR?

Bitwise exclusive OR.

Important property:

x ^ x = 0
x ^ 0 = x


Q12. What is ~x?

Bitwise NOT.

For integers:

~x = -(x + 1)


Q13. What is <<?

Left bit shift.


Q14. What is >>?

Right bit shift.


Q15. What is := ?

Walrus operator.

It assigns and evaluates an expression.


Q16. What is @ ?

Matrix multiplication operator.


Q17. What is operator precedence?

Rules that determine which operators
are evaluated first.


Q18. What is short-circuit evaluation?

Python stops evaluating logical expressions
when the final result is already known.
"""


# ============================================================
# 54. QUICK REVISION TABLE
# ============================================================

"""
ARITHMETIC:

+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor division
%    Modulus
**   Power


COMPARISON:

==   Equal
!=   Not equal
>    Greater
<    Less
>=   Greater/equal
<=   Less/equal


LOGICAL:

and
or
not


BITWISE:

&    AND
|    OR
^    XOR
~    NOT
<<   Left shift
>>   Right shift


ASSIGNMENT:

=
+=
-=
*=
/=
%=
**=
//=
&=
|=
^=
<<=
>>=


MEMBERSHIP:

in
not in


IDENTITY:

is
is not


SPECIAL:

:=   Walrus
@    Matrix multiplication
"""


# ============================================================
#                         END
# ============================================================