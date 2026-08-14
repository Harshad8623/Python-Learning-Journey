# ============================================================
# 1. WHAT IS A FUNCTION?
# ============================================================

"""
A function is a reusable block of code designed
to perform a particular task.

Basic syntax:

def function_name(parameters):
    # function body
    statements

To execute/call a function:

function_name(arguments)
"""


# ============================================================
# 2. SIMPLE FUNCTION
# ============================================================

def greet():
    print("Hello!")


# Function call
greet()
greet()
greet()


# ============================================================
# 3. FUNCTION WITH PARAMETER
# ============================================================

def greet(name):
    print("Hello", name)


greet("Harshad")
greet("Vedant")
greet("Rahul")


"""
Here:

name -> parameter
"Harshad" -> argument
"Vedant" -> argument
"Rahul" -> argument
"""


# ============================================================
# 4. PARAMETER VS ARGUMENT
# ============================================================

def greet(name):        # name = PARAMETER
    print(f"Hello {name}!!!")


greet("Rahul")          # "Rahul" = ARGUMENT
greet("Priya")          # "Priya" = ARGUMENT


"""
PARAMETER:
    Variable written inside function definition.

ARGUMENT:
    Actual value passed while calling the function.
"""


# ============================================================
# 5. DEFAULT PARAMETER
# ============================================================

def greet(name="User"):

    print("Hello", name)


greet("Harshad")
greet("Vedant")

# No argument is given.
# Python uses the default value.
greet()

# Output:
# Hello Harshad
# Hello Vedant
# Hello User


# ============================================================
# 6. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================

def add(a, b):

    print(a + b)


add(10, 20)
add(100, 200)


# ============================================================
# 7. FUNCTION TAKING USER INPUT
# ============================================================

def even_odd():

    num = int(input("Enter a Number: "))

    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


# Function call
# even_odd()


# ============================================================
# 8. FUNCTION TO PRINT FACTORS
# ============================================================

def print_factors():

    num = int(input("Enter a Number: "))

    for i in range(1, num + 1):

        if num % i == 0:
            print(i)


# Function call
# print_factors()


# ============================================================
# 9. FUNCTION WITH PARAMETERS
# ============================================================

def addition(a, b, c):

    print(a + b + c, "is sum of 3 numbers")


addition(10, 20, 30)


# ============================================================
# 10. RETURN STATEMENT
# ============================================================

"""
return sends a value back to the caller.

Important:

print() -> displays something

return  -> sends something back
"""


def add(a, b):

    return a + b


result = add(10, 20)

print(result)


# We can directly print the returned value:

print(add(50, 60))


# ============================================================
# 11. print() VS return()
# ============================================================

def add_using_print(a, b):

    print(a + b)


def add_using_return(a, b):

    return a + b


# print() version
result1 = add_using_print(10, 20)

print("result1:", result1)
# result1 will be None


# return version
result2 = add_using_return(10, 20)

print("result2:", result2)
# result2 will be 30


"""
IMPORTANT:

print() -> displays the result

return -> gives the result back to the program

For DSA and interviews, return is generally much more useful.
"""


# ============================================================
# 12. FUNCTION CAN RETURN BOOLEAN
# ============================================================

def can_vote(age):

    if age >= 18:
        return True

    return False


print(can_vote(20))
print(can_vote(15))


# Better version:

def can_vote(age):

    return age >= 18


print(can_vote(20))
print(can_vote(15))


# ============================================================
# 13. FUNCTION CAN RETURN STRING
# ============================================================

def check_number(num):

    if num > 0:
        return "Positive"

    elif num < 0:
        return "Negative"

    else:
        return "Zero"


print(check_number(10))
print(check_number(-5))
print(check_number(0))


# ============================================================
# 14. FUNCTION CAN RETURN LIST
# ============================================================

def get_even_numbers(numbers):

    result = []

    for num in numbers:

        if num % 2 == 0:
            result.append(num)

    return result


numbers = [1, 2, 3, 4, 5, 6]

print(get_even_numbers(numbers))


# ============================================================
# 15. FUNCTION CAN RETURN MULTIPLE VALUES
# ============================================================

def calculate(a, b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print(result)


# Unpacking returned values

add_result, sub_result, mul_result = calculate(10, 5)

print(add_result)
print(sub_result)
print(mul_result)


"""
Python is actually returning a tuple:

return addition, subtraction, multiplication

is similar to:

return (addition, subtraction, multiplication)
"""


# ============================================================
# 16. EARLY RETURN
# ============================================================

def is_positive(num):

    if num <= 0:
        return False

    return True


print(is_positive(10))
print(is_positive(-5))


# ============================================================
# 17. PRIME NUMBER FUNCTION
# ============================================================

def is_prime(n):

    if n < 2:
        return False

    count = 0

    for i in range(1, n + 1):

        if n % i == 0:
            count += 1

    return count == 2


print(is_prime(12))
print(is_prime(7))
print(is_prime(-4))
print(is_prime(0))
print(is_prime(-7))


"""
Your original is_prime() logic was basically correct,
but adding:

if n < 2:
    return False

makes the intention clearer.

Prime numbers start from 2.

Examples:

2 -> Prime
3 -> Prime
5 -> Prime
7 -> Prime
11 -> Prime

0 -> Not Prime
1 -> Not Prime
negative numbers -> Not Prime
"""


# ============================================================
# 18. BETTER PRIME NUMBER FUNCTION - DSA VERSION
# ============================================================

"""
Instead of checking all numbers from 1 to n,
we only need to check up to sqrt(n).

This reduces time complexity.
"""


def is_prime(n):

    if n < 2:
        return False

    i = 2

    while i * i <= n:

        if n % i == 0:
            return False

        i += 1

    return True


print(is_prime(2))
print(is_prime(7))
print(is_prime(12))
print(is_prime(97))


# ============================================================
# 19. POSITIONAL ARGUMENTS
# ============================================================

def student(name, age):

    print("Name:", name)
    print("Age:", age)


student("Harshad", 21)


"""
Arguments are matched according to their position.

"Harshad" -> name
21        -> age
"""


# ============================================================
# 20. KEYWORD ARGUMENTS
# ============================================================

def student(name, age):

    print("Name:", name)
    print("Age:", age)


student(name="Harshad", age=21)


# Order does not matter with keyword arguments

student(age=21, name="Harshad")


# ============================================================
# 21. POSITIONAL + KEYWORD ARGUMENTS
# ============================================================

def student(name, age, city):

    print(name, age, city)


student("Harshad", age=21, city="Latur")


"""
IMPORTANT RULE:

Positional arguments must come BEFORE keyword arguments.

Correct:

student("Harshad", age=21)


Incorrect:

student(name="Harshad", 21)
"""


# ============================================================
# 22. DEFAULT ARGUMENTS
# ============================================================

def introduce(name, city="Latur"):

    print(name, city)


introduce("Harshad")
introduce("Rahul", "Pune")


# ============================================================
# 23. MULTIPLE DEFAULT PARAMETERS
# ============================================================

def student(name="Unknown", age=0, city="Unknown"):

    print(name, age, city)


student()
student("Harshad")
student("Harshad", 21)
student("Harshad", 21, "Latur")


# ============================================================
# 24. IMPORTANT DEFAULT ARGUMENT RULE
# ============================================================

"""
Non-default parameters must come BEFORE default parameters.

Correct:

def greet(name, age=18):
    pass


Incorrect:

def greet(age=18, name):
    pass

This causes SyntaxError.
"""


# ============================================================
# 25. *args
# ============================================================

"""
*args allows a function to accept
any number of positional arguments.

Inside the function, args is a TUPLE.
"""


def addition(*args):

    print(args)
    print(type(args))


addition(10, 20)
addition(10, 20, 30)
addition(10, 20, 30, 40, 50)


# ============================================================
# 26. PRACTICAL *args EXAMPLE
# ============================================================

def addition(*args):

    total = 0

    for num in args:
        total += num

    return total


print(addition(10, 20))
print(addition(10, 20, 30))
print(addition(1, 2, 3, 4, 5))


# ============================================================
# 27. **kwargs
# ============================================================

"""
**kwargs allows a function to accept
any number of keyword arguments.

Inside the function, kwargs is a DICTIONARY.
"""


def student_info(**kwargs):

    print(kwargs)
    print(type(kwargs))


student_info(
    name="Harshad",
    age=21,
    city="Latur"
)


# ============================================================
# 28. PRACTICAL **kwargs
# ============================================================

def student_info(**kwargs):

    for key, value in kwargs.items():

        print(key, ":", value)


student_info(
    name="Harshad",
    age=21,
    branch="CSE"
)


# ============================================================
# 29. *args AND **kwargs TOGETHER
# ============================================================

def test(*args, **kwargs):

    print("Positional:", args)
    print("Keyword:", kwargs)


test(
    10,
    20,
    30,
    name="Harshad",
    age=21
)


# ============================================================
# 30. PARAMETER ORDER
# ============================================================

"""
When using all types of parameters, the general order is:

def function(
    normal_parameter,
    *args,
    keyword_parameter,
    **kwargs
):


Example:
"""


def example(a, b=10, *args, **kwargs):

    print(a)
    print(b)
    print(args)
    print(kwargs)


example(
    1,
    2,
    3,
    4,
    name="Harshad",
    city="Latur"
)


# ============================================================
# 31. RECURSION
# ============================================================

"""
Recursion means a function calls itself.

Every recursive function needs:

1. Base case
2. Recursive case
"""


def countdown(n):

    # Base case
    if n == 0:
        return

    print(n)

    # Recursive call
    countdown(n - 1)


countdown(5)


# ============================================================
# 32. FACTORIAL USING RECURSION
# ============================================================

def factorial(n):

    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


print(factorial(5))

# 5 * 4 * 3 * 2 * 1
# 120


# ============================================================
# 33. FACTORIAL USING LOOP
# ============================================================

def factorial(n):

    result = 1

    for i in range(1, n + 1):

        result *= i

    return result


print(factorial(5))


# ============================================================
# 34. LOCAL VARIABLE IN FUNCTION
# ============================================================

def test():

    message = "Hello"

    print(message)


test()

# message cannot normally be accessed here:
#
# print(message)


# ============================================================
# 35. GLOBAL VARIABLE IN FUNCTION
# ============================================================

name = "Harshad"


def greet():

    print(name)


greet()


# ============================================================
# 36. GLOBAL KEYWORD
# ============================================================

count = 0


def increase():

    global count

    count += 1


increase()
increase()

print(count)


"""
global is required when you want to REASSIGN
a global variable inside a function.

But avoid unnecessary global variables in real programs.
Returning values is generally better.
"""


# ============================================================
# 37. FUNCTIONS AS FIRST-CLASS OBJECTS
# ============================================================

"""
In Python, functions are objects.

Therefore we can:

- Store a function in a variable
- Pass a function to another function
- Return a function from a function
"""


def square(x):

    return x * x


operation = square

print(operation(5))


# ============================================================
# 38. PASSING FUNCTION AS ARGUMENT
# ============================================================

def square(x):

    return x * x


def execute(function, value):

    return function(value)


print(execute(square, 5))


# ============================================================
# 39. LAMBDA WITH FUNCTIONS
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda x: x * x, numbers)
)

print(squares)


# ============================================================
# 40. DOCSTRING
# ============================================================

def add(a, b):
    """
    This function returns the sum of two numbers.
    """

    return a + b


print(add(10, 20))

# You can access documentation using:
print(add.__doc__)


# ============================================================
# 41. TYPE HINTS
# ============================================================

def add(a: int, b: int) -> int:

    return a + b


print(add(10, 20))


"""
Type hints tell humans/tools what type
we expect.

They do NOT automatically enforce the type.
"""


# ============================================================
# 42. FUNCTION WITH LIST
# ============================================================

def find_max(numbers):

    maximum = numbers[0]

    for num in numbers:

        if num > maximum:
            maximum = num

    return maximum


numbers = [10, 25, 5, 40, 15]

print(find_max(numbers))


# ============================================================
# 43. FUNCTION WITH STRING
# ============================================================

def count_vowels(text):

    count = 0

    for char in text.lower():

        if char in "aeiou":
            count += 1

    return count


print(count_vowels("Harshad"))


# ============================================================
# 44. FUNCTION FOR DSA - LINEAR SEARCH
# ============================================================

def linear_search(numbers, target):

    for i in range(len(numbers)):

        if numbers[i] == target:
            return i

    return -1


numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))
print(linear_search(numbers, 100))


"""
Return:

index -> if found
-1    -> if not found
"""


# ============================================================
# 45. FUNCTION FOR DSA - COUNT EVEN NUMBERS
# ============================================================

def count_even(numbers):

    count = 0

    for num in numbers:

        if num % 2 == 0:
            count += 1

    return count


numbers = [1, 2, 3, 4, 5, 6]

print(count_even(numbers))


# ============================================================
# 46. FUNCTION FOR DSA - REVERSE LIST
# ============================================================

def reverse_list(numbers):

    result = []

    for i in range(len(numbers) - 1, -1, -1):

        result.append(numbers[i])

    return result


numbers = [1, 2, 3, 4, 5]

print(reverse_list(numbers))


# ============================================================
# 47. FUNCTION FOR DSA - CHECK SORTED
# ============================================================

def is_sorted(numbers):

    for i in range(len(numbers) - 1):

        if numbers[i] > numbers[i + 1]:
            return False

    return True


print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 5, 3, 4]))


# ============================================================
# 48. FUNCTION FOR DSA - SUM OF LIST
# ============================================================

def list_sum(numbers):

    total = 0

    for num in numbers:
        total += num

    return total


print(list_sum([1, 2, 3, 4, 5]))


# ============================================================
# 49. IMPORTANT FUNCTION CONCEPT:
#    RETURN IMMEDIATELY ENDS FUNCTION
# ============================================================

def test():

    print("Before return")

    return 100

    # This will NEVER execute
    print("After return")


result = test()

print(result)


# ============================================================
# 50. FUNCTION WITHOUT RETURN
# ============================================================

def test():

    print("Hello")


result = test()

print(result)


"""
If a function doesn't explicitly return anything,
Python automatically returns:

None
"""


# ============================================================
# 51. RETURN VS PRINT - IMPORTANT INTERVIEW QUESTION
# ============================================================

def square_print(n):

    print(n * n)


def square_return(n):

    return n * n


# print() only displays
result1 = square_print(5)

print(result1)
# None


# return gives value back
result2 = square_return(5)

print(result2)
# 25


# ============================================================
# 52. COMMON FUNCTION MISTAKE
# ============================================================

"""
Don't write:

def add(a, b):
    print(a + b)


if you need to use the result later.

Prefer:

def add(a, b):
    return a + b


Then:

result = add(10, 20)

print(result)
"""


# ============================================================
# 53. TIME COMPLEXITY OF FUNCTIONS
# ============================================================

"""
A function itself does not have a fixed time complexity.

Its complexity depends on the operations inside it.

Example:

def greet():
    print("Hello")

Time:
O(1)


Example:

def print_numbers(n):

    for i in range(n):
        print(i)

Time:
O(n)


Example:

def print_pairs(n):

    for i in range(n):

        for j in range(n):
            print(i, j)

Time:
O(n²)
"""


# ============================================================
# 54. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

"""
1. What is a function?

A reusable block of code designed to perform
a specific task.


2. What is a parameter?

A variable defined in a function definition.


3. What is an argument?

The actual value passed to a function.


4. What is return?

return sends a value back to the caller
and immediately exits the function.


5. print() vs return?

print() -> displays output
return -> sends output back


6. What is a default argument?

A parameter with a predefined value.

Example:

def greet(name="User"):
    ...


7. What are positional arguments?

Arguments matched according to position.


8. What are keyword arguments?

Arguments passed using parameter names.

Example:

greet(name="Harshad")


9. What is *args?

Accepts variable number of positional arguments.

Stored as a tuple.


10. What is **kwargs?

Accepts variable number of keyword arguments.

Stored as a dictionary.


11. What is recursion?

A function calling itself.


12. What is a base case?

The condition that stops recursion.


13. What is scope?

The region where a variable can be accessed.


14. What is LEGB?

Local
Enclosing
Global
Built-in


15. What is a docstring?

A string used to document a function.


16. What are type hints?

Annotations indicating expected types.


17. Can a function return multiple values?

Yes.

Example:

return a, b, c

Python returns them as a tuple.


18. What happens if there is no return?

Python returns None.
"""


# ============================================================
# 55. QUICK REVISION
# ============================================================

"""
FUNCTION:

def greet():
    print("Hello")


PARAMETER:

def greet(name):
    ...


ARGUMENT:

greet("Harshad")


DEFAULT PARAMETER:

def greet(name="User"):
    ...


RETURN:

def add(a, b):
    return a + b


POSITIONAL:

add(10, 20)


KEYWORD:

add(a=10, b=20)


*args:

def test(*args):
    ...


**kwargs:

def test(**kwargs):
    ...


RECURSION:

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


GLOBAL:

x = 10

def test():

    global x
    x = 20


LAMBDA:

square = lambda x: x * x
"""


# ============================================================
#                         END
# ============================================================