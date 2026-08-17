# Take a sentence as input. Print each word's length next to it. Example: Python (6) is (2) great (5).


sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word, "(", len(word), ")", end=" ")