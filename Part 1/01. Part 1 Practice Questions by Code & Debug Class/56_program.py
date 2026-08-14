# Gien two lists of same length write a python program using loop to create a new list where each element is the sum of the corrsponding elements from both original lists

lst1 = [10, 20, 30, 40]
lst2 = [5, 10, 15, 20]
lst = []
for i in range(0,4):
    lst.append(lst1[i] + lst2[i])
print(lst)