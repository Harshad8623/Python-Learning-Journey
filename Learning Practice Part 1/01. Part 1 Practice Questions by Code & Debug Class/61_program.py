# Given a list, remove all duplicate elements while preserving the original order of the unique items.

lst = [1, 2, 3, 1, 2, 5, 7, 9, 4, 2, 5, 4, 9, 6, 9]
new_lst = set(lst) # Here possibility of keeping order of elements is not
print(new_lst)
# A set is excellent for removing duplicates, but if the question specifically requires preserving the original order

# Better Solution
lst = [1, 2, 3, 1, 2, 5, 7, 9, 4, 2, 5, 4, 9, 6, 9]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)
# current solution is O(n²) in the worst case



# Another Better Solution
lst = [1, 2, 3, 1, 2, 5, 7, 9, 4, 2, 5, 4, 9, 6, 9]
new_lst = []
seen = set()
for i in lst:
    if i not in seen:
        new_lst.append(i)
        seen.add(i)
print(new_lst)