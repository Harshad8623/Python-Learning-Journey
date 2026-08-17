"""
PART 2 — Loops & Numbers (11-25)
"""

# 11. Multiplication Table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def multiplication_table_list(n):
    return [n*i for i in range(1, 11)]


# 12. Sum of first N numbers
def sum_n_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_n_formula(n):
    return n * (n + 1) // 2

# Interview: loop is O(n); formula is O(1).


# 13. Factorial using loop
def factorial_loop(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 14. Prime Number
def is_prime_basic(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_sqrt(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Interview point: checking only up to sqrt(n) reduces O(n) to O(sqrt(n)).


# 15. Print all primes till N
def primes_till_n(n):
    result = []
    for x in range(2, n + 1):
        if is_prime_sqrt(x):
            result.append(x)
    return result

# Advanced: Sieve of Eratosthenes
def primes_sieve(n):
    if n < 2:
        return []
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for multiple in range(p*p, n+1, p):
                prime[multiple] = False
        p += 1
    return [i for i in range(2, n+1) if prime[i]]

# Interview: sieve is approximately O(n log log n).


# 16. Fibonacci
def fibonacci_loop(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for _ in range(2, n):
        result.append(result[-1] + result[-2])
    return result

def fibonacci_two_variables(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# 17. Sum of digits
def sum_digits(n):
    n = abs(n)
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def sum_digits_string(n):
    return sum(int(ch) for ch in str(abs(n)))


# 18. Reverse a number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev

def reverse_number_string(n):
    sign = "-" if n < 0 else ""
    digits = str(abs(n))
    return int(sign + digits[::-1])


# 19. Palindrome number
def palindrome_number(n):
    return n >= 0 and n == reverse_number(n)

def palindrome_number_string(n):
    s = str(n)
    return s == s[::-1]


# 20. Armstrong number
def is_armstrong(n):
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n

def is_armstrong_math(n):
    if n < 0:
        return False
    original = n
    digits = 1 if n == 0 else 0
    temp = n
    while temp:
        digits += 1
        temp //= 10
    temp = n
    total = 0
    while temp:
        total += (temp % 10) ** digits
        temp //= 10
    return total == original


# 21. GCD
def gcd_euclid(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    a, b = abs(a), abs(b)
    return a if b == 0 else gcd_recursive(b, a % b)


# 22. LCM
def lcm_using_gcd(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_euclid(a, b)

def lcm_by_loop(a, b):
    if a == 0 or b == 0:
        return 0
    value = max(abs(a), abs(b))
    while value % abs(a) != 0 or value % abs(b) != 0:
        value += 1
    return value


# 23. Perfect Number
def is_perfect(n):
    if n <= 1:
        return False
    total = 1
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            total += divisor
            other = n // divisor
            if other != divisor:
                total += other
        divisor += 1
    return total == n


# 24. Strong Number
def is_strong(n):
    if n < 0:
        return False
    total = 0
    temp = n
    if temp == 0:
        return False
    while temp:
        digit = temp % 10
        total += factorial_loop(digit)
        temp //= 10
    return total == n


# 25. Count digits
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n:
        count += 1
        n //= 10
    return count

def count_digits_string(n):
    return len(str(abs(n)))


if __name__ == "__main__":
    print("Primes:", primes_till_n(50))
    print("Sieve:", primes_sieve(50))
    print("Fibonacci:", fibonacci_loop(10))
    print("GCD:", gcd_euclid(48, 18))
    print("LCM:", lcm_using_gcd(12, 18))
    print("Perfect:", is_perfect(28))
    print("Strong:", is_strong(145))
