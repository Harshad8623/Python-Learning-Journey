# write a function called find_max that takes three number as parameteres and prints the largest one

def find_max(a, b, c):
    if a > b:
        if a > c:
            largest = a
        else:
            largest = c
    else:
        if b > c:
            largest = b
        else:
            largest = c
    print(largest, "is largest number")
find_max(19,12,18)
find_max(10,12,18)
find_max(18,12,18)
find_max(12,12,18)
find_max(10,12,18)
find_max(10,10,10)