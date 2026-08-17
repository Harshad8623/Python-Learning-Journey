# Create a tuple of 8 numbers. Using slicing, print the first 3, last 3, and every alternate element.

numbers = (1, 2, 3, 5, 2, 6, 2, 4)
print(numbers[:3])
print(numbers[len(numbers)-3:])
print(numbers[::2])