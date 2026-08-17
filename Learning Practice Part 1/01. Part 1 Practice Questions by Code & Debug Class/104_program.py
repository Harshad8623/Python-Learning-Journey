# Take a paragraph as input. Print the count of unique words in it (case insensitive).

paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
unique_words = set(words)

print("Number of unique words:", len(unique_words))