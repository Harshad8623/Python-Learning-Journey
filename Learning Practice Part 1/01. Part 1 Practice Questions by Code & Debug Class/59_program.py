#  Reverse a list without using the .reverse() method or list slicing ([::-1])

lst = [1,5,7,3,5,4,1,2,6,9]
lst_rev = []
for i in range(len(lst)):
    a = lst.pop()
    lst_rev.append(a)
print(lst)
print(lst_rev)

# AI suggetion : Answer is correct but Your solution modifies the original list

lst = [1,5,7,3,5,4,1,2,6,9]
lst_rev = []
for i in range(len(lst)-1, -1, -1):
    lst_rev.append(lst[i])
print(lst)
print(lst_rev)


# AI suggestion : Good but Reverse the list in-place without using another list, .reverse(), or slicing.

# Then you should use two-pointer swapping.
lst = [1, 5, 7, 3, 5, 4, 1, 2, 6, 9]
left = 0
right = len(lst) - 1
while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1

print(lst)