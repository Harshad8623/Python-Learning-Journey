# Take a sentence as input. Reverse the order of words (not the characters in each word). Example: "Python is fun" → "fun is Python".


sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_words = words[::-1]
print(" ".join(reversed_words))