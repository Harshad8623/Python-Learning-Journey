"""
PART 8 — List / Dictionary / Set Comprehensions (76-78)
"""


# 76. List Comprehension — Squares of Even Numbers
def squares_even_comprehension(numbers):
    return [x*x for x in numbers if x % 2 == 0]

# Equivalent normal loop:
def squares_even_loop(numbers):
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x*x)
    return result


# 77. Dictionary Comprehension — Word Length
def word_lengths_comprehension(words):
    return {word: len(word) for word in words}

# Equivalent loop:
def word_lengths_loop(words):
    result = {}
    for word in words:
        result[word] = len(word)
    return result

# Conditional dictionary comprehension:
def even_number_squares_dict(numbers):
    return {x: x*x for x in numbers if x % 2 == 0}


# 78. Set Comprehension
def unique_squares(numbers):
    return {x*x for x in numbers}

# Conditional set comprehension:
def unique_even_squares(numbers):
    return {x*x for x in numbers if x % 2 == 0}


# INTERVIEW NOTES
# List comprehension: [expression for item in iterable if condition]
# Dict comprehension: {key: value for item in iterable if condition}
# Set comprehension: {expression for item in iterable if condition}
#
# Main benefit: concise and often readable.
# Complexity: normally same Big-O as the equivalent loop.
#
# Common mistake:
# Don't use a comprehension when the logic becomes deeply nested or hard to read.
#
# Example:
# squares = [x*x for x in range(10) if x % 2 == 0]
# Read it as:
# "For every x in range(10), if x is even, put x*x into the list."


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 4, 5, 6]
    words = ["python", "dsa", "interview"]

    print(squares_even_comprehension(nums))
    print(squares_even_loop(nums))
    print(word_lengths_comprehension(words))
    print(word_lengths_loop(words))
    print(unique_squares(nums))
    print(unique_even_squares(nums))
