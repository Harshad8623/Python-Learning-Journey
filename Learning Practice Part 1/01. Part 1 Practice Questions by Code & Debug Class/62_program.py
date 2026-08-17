# Separate a list of integers into two distinct lists: one containing all the even numbers and the other containing all the odd numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(evens)
print(odds)