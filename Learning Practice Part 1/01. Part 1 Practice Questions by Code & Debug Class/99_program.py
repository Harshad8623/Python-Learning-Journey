# Take a sentence as input. Split it into words and print how many words start with a vowel.

sentence = input("Enter a sentence: ")

words = sentence.split()
count = 0

for word in words:
    if word[0].lower() in "aeiou":
        count += 1

print("Number of words starting with a vowel:", count)