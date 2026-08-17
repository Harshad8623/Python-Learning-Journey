# Write a function is_palindrome(text) that returns True if the given string is a palindrome (ignoring case and spaces)


def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


print(is_palindrome("Madam"))
print(is_palindrome("nurses run"))
print(is_palindrome("Hello"))