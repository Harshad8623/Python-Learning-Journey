# Write a program that checks a list and a target number . Use a loop to determmine if the target number exists in the lists. Do not use the in operator

lst = [10, 20,30, 40,56, 23, 45, 85, 96, 63, 54]
target= 56
for i in lst:
    if i == target:
        print(target, "exists in list")
        break
else:
    print(target, "does not exists in list")
print("\n")




lst = [10, 20, 30, 40, 56, 23, 45, 85, 96, 63, 54]
target = 56
found = False
for i in lst:
    if i == target:
        found = True
        break
if found:
    print(target, "exists in list")
else:
    print(target, "does not exist in list")