
# 1️⃣ Basic approach — Count all divisors
# # Take the upper limit from the user
n = int(input("Enter a number: "))

# Check every number from 1 to n
for i in range(1, n + 1):

    # We will count how many numbers divide i completely
    # A prime number must have exactly 2 divisors:
    # 1 and the number itself
    count = 0

    # Check every number from 1 to i
    # We use i + 1 because the ending value of range()
    # is excluded
    for j in range(1, i + 1):

        # If remainder is 0, j is a divisor of i
        if i % j == 0:
            count += 1

    # If i has exactly 2 divisors, it is prime
    if count == 2:
        print(i)





# 2️⃣ Better approach — Check only up to √n
# Take the upper limit from the user
n = int(input("Enter a number: "))

# Check every number from 2 to n
# We start from 2 because 1 is NOT a prime number
for i in range(2, n + 1):

    # Assume that i is prime initially
    # We will change this to False if we find a divisor
    is_prime = True

    # We only check divisors up to √i
    #
    # Why?
    # If i has a factor greater than √i,
    # it must have another factor smaller than √i.
    #
    # Therefore, if no divisor is found up to √i,
    # i must be prime.
    #
    # int(i ** 0.5) gives the integer part of √i.
    # +1 is required because range() excludes its ending value.
    for j in range(2, int(i ** 0.5) + 1):

        # If i is completely divisible by j,
        # then i is NOT prime.
        if i % j == 0:
            is_prime = False

            # No need to check further divisors
            # because we already know i is not prime.
            break

    # If no divisor was found, is_prime remains True
    if is_prime:
        print(i)




# 3️⃣ Best for learning functions — is_prime()
# Function to check whether a number is prime
def is_prime(n):

    # Numbers less than 2 are not prime
    #
    # 0 → Not Prime
    # 1 → Not Prime
    # Negative numbers → Not Prime
    if n < 2:
        return False

    # We only need to check divisors up to √n
    # because a factor greater than √n must have
    # a corresponding factor smaller than √n.
    for i in range(2, int(n ** 0.5) + 1):

        # If n is completely divisible by i,
        # then n has a divisor other than 1 and itself.
        # Therefore, n is not prime.
        if n % i == 0:
            return False

    # If we reach here, no divisor was found.
    # Therefore, n is prime.
    return True


# Take the upper limit from the user
n = int(input("Enter a number: "))

# Check every number from 2 to n
# We start from 2 because 1 is not prime.
for i in range(2, n + 1):

    # Call the function to check whether i is prime
    if is_prime(i):
        print(i)



# 4️⃣ More optimized — Skip even numbers
# Take the upper limit from the user
n = int(input("Enter a number: "))

# 2 is the only even prime number.
# We print it separately.
if n >= 2:
    print(2)

# Start from 3 and increase by 2 each time.
#
# This gives:
# 3, 5, 7, 9, 11, 13, ...
#
# We skip all even numbers because every even number
# greater than 2 is automatically NOT prime.
for i in range(3, n + 1, 2):

    # Initially assume that i is prime
    is_prime = True

    # Start checking divisors from 3.
    #
    # We skip 2 because i is already odd,
    # so an odd number cannot be divisible by 2.
    #
    # We also increase j by 2:
    # 3, 5, 7, 9, ...
    #
    # Again, we are checking only odd divisors.
    #
    # We only need to check up to √i.
    for j in range(3, int(i ** 0.5) + 1, 2):

        # If i is divisible by j,
        # then i is not prime.
        if i % j == 0:
            is_prime = False

            # No need to check more divisors
            break

    # If no divisor was found, i is prime
    if is_prime:
        print(i)