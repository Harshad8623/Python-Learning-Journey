# Take a sentence as input. Capitalize only the first letter of each word that is longer than 3 characters. Keep the rest as is.


sentence = input("Enter a sentence: ")

words = sentence.split()
result = []

for word in words:
    if len(word) > 3:
        word = word[0].upper() + word[1:]
    result.append(word)

print(" ".join(result))