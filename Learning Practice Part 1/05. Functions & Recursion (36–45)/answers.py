"""
PART 4 — Functions & Recursion (36-45)
"""

# 36. Add Numbers using Function
def add(a, b):
    return a + b


# 37. Prime using Function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 38. Factorial using Function
def factorial(n):
    if n < 0:
        raise ValueError("Negative factorial is invalid")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 39. Fibonacci using Function
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# 40. GCD using Function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


# 41. Recursive Factorial
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Negative factorial is invalid")
    # Base case prevents infinite recursion.
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# 42. Recursive Fibonacci
def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# WARNING: naive recursion is O(2^n).
# Better recursive version with memoization:
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Interview: memoized Fibonacci becomes O(n) time and O(n) space.


# 43. Sum of List using Recursion
def recursive_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + recursive_sum(arr, index + 1)

# Alternative recursion by removing the first element:
def recursive_sum_slicing(arr):
    if not arr:
        return 0
    return arr[0] + recursive_sum_slicing(arr[1:])

# Note: slicing creates new lists, so index-based recursion is generally better.


# 44. Function using *args
def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total

def maximum(*args):
    if not args:
        return None
    result = args[0]
    for value in args[1:]:
        if value > result:
            result = value
    return result


# 45. Function using **kwargs
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

def build_profile(**kwargs):
    return kwargs


# Interview questions to answer:
# 1. Why use a function? Reusability, abstraction, testing, maintainability.
# 2. What is recursion? A function calling itself.
# 3. What must recursion have? A base case and progress toward it.
# 4. What is *args? Variable number of positional arguments.
# 5. What is **kwargs? Variable number of keyword arguments.
# 6. Why can recursion be dangerous? Call-stack growth / RecursionError.
# 7. Why is iterative Fibonacci usually preferred? Better time/space behavior.


if __name__ == "__main__":
    print(add(5, 7))
    print(is_prime(29))
    print(factorial(5))
    print(fibonacci(8))
    print(gcd(48, 18))
    print(factorial_recursive(5))
    print(fibonacci_recursive(8))
    print(fibonacci_memo(40))
    print(recursive_sum([1, 2, 3, 4]))
    print(sum_all(1, 2, 3, 4, 5))
    show_profile(name="Harshad", role="Student")
