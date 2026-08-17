# write a function called min_of_three that takes three numbers and returns the smallest without using any built in function
def min_of_three(a, b, c):
    if a < b:
        if a < c:
            return a
        return c
    else:
        if b < c:
            return b
        return c
print(min_of_three(10, 20, 3))
print(min_of_three(10, 20, 30))
print(min_of_three(10, 2, 3))
print(min_of_three(10, 10, 10))
print(min_of_three(-10, 20, 3))