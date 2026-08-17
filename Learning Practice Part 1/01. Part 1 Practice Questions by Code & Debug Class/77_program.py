# Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum.

a = []
for i in range(5):
    a.append(int(input(f"Enter {i+1} Number : ")))

a = tuple(a)
print(min(a))
print(max(a))


# Another pythonic Way

a = tuple(int(input(f"Enter {i+1} Number : ")) for i in range(5))

print("Tuple:", a)
print("Minimum:", min(a))
print("Maximum:", max(a))