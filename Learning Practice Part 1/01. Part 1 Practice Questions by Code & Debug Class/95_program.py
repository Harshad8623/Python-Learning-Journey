# Read a sentence from the user. Count and print the total number of vowels (a, e, i, o, u, case-insensitive) present in it, using a for loop.

sentence = input("Enter a sentence : ").lower()
count = 0
for i in sentence:
    if i in {'a', 'e', 'i', 'o', 'u'}:
        count += 1
print(count)