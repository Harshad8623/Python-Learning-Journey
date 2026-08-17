# Find the largest and smallest number in the list without using built in function

lst = [1, 2, 12, 8, 9, 15, 7, 8, 19, 4]
smallest = lst[0]
largest = lst[0]
for i in lst:
    if smallest > i:
        smallest = i
    if largest < i:
        largest = i
print(largest)
print(smallest)

# Time complexity: O(n)
# Extra space: O(1)


# AI suggestion : variable name i works, but num is more readable