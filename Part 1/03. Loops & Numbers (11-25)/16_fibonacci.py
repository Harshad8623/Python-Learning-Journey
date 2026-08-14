# 1️⃣ Basic for loop approach
# Take the number of terms from the user
n = int(input("Enter number of terms: "))
# First two Fibonacci numbers
a = 0
b = 1
# Repeat the loop n times
for i in range(n):
    # Print the current Fibonacci number
    print(a, end=" ")
    # Calculate the next number
    # The next number is the sum of the previous two numbers
    c = a + b
    # Move the values forward
    # b becomes the new a
    a = b
    # c becomes the new b
    b = c




# 2️⃣ Without using a third variable
# Number of Fibonacci terms
n = int(input("Enter number of terms: "))
# First two terms
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    # Update a and b together
    a, b = b, a + b




# 3️⃣ Fibonacci using while loop
# Take number of terms
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 0

# Continue until we print n terms
while i < n:
    print(a, end=" ")
    # Calculate next term
    c = a + b
    # Move to next two numbers
    a = b
    b = c
    # Increase counter
    i += 1



# 4️⃣ Fibonacci using a function
def fibonacci(n):
    # First two Fibonacci numbers
    a = 0
    b = 1
    # Generate n terms
    for i in range(n):
        print(a, end=" ")
        # Calculate next term
        a, b = b, a + b
n = int(input("Enter number of terms: "))
fibonacci(n)



# 5️⃣ Fibonacci using recursion ⭐
def fibonacci(n):

    # Base cases
    # Fibonacci(0) = 0
    # Fibonacci(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Every Fibonacci number is the sum
    # of the previous two Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter the position: "))
print(fibonacci(n))