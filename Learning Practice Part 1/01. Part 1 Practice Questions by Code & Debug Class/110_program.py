# Write a function most_common_word(text) that returns the word that appears most frequently in a given paragraph. Ignore case. If multiple words have the same count, return any one.


def most_common_word(text):
    words = text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    most_common = max(frequency, key=frequency.get)

    return most_common


text = input("Enter a paragraph: ")
print("Most common word:", most_common_word(text))