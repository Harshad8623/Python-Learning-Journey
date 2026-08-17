"""
PART 5 — Strings (46-60)
"""

# 46. Reverse String without slicing
def reverse_loop(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

# Better for large strings: append then join
def reverse_join(s):
    chars = []
    for ch in s:
        chars.append(ch)
    chars.reverse()
    return "".join(chars)

# Two-pointer style using a list
def reverse_two_pointer(s):
    chars = list(s)
    left, right = 0, len(chars)-1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


# 47. Reverse using slicing
def reverse_slice(s):
    return s[::-1]


# 48. Palindrome String
def palindrome_string(s):
    return s == s[::-1]

def palindrome_two_pointer(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# 49. Count Vowels
def count_vowels(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# 50. Count Consonants
def count_consonants(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


# 51. Frequency of Characters
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Alternative using Counter
def char_frequency_counter(s):
    from collections import Counter
    return dict(Counter(s))


# 52. Anagram Check
def are_anagrams_sort(a, b):
    return sorted(a.lower().replace(" ", "")) == sorted(b.lower().replace(" ", ""))

def are_anagrams_frequency(a, b):
    a = a.lower().replace(" ", "")
    b = b.lower().replace(" ", "")
    if len(a) != len(b):
        return False
    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in b:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return all(value == 0 for value in freq.values())

# Interview: sorting -> O(n log n); frequency hash map -> O(n) average.


# 53. Remove Duplicate Characters
def remove_duplicates(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)

def remove_duplicates_preserve_order_dict(s):
    return "".join(dict.fromkeys(s))


# 54. First Non-Repeating Character
def first_non_repeating(s):
    freq = char_frequency(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


# 55. Word Count
def word_count(sentence):
    return len(sentence.split())

def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq


# 56. Reverse Words in Sentence
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

# Reverse characters of every word:
def reverse_each_word(sentence):
    return " ".join(word[::-1] for word in sentence.split())


# 57. String Rotation
def is_rotation(a, b):
    return len(a) == len(b) and b in (a + a)

# Interview insight: if b is a rotation of a, b occurs in a+a.


# 58. String Compression
def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)

# Example: aaabbc -> a3b2c1


# 59. Check Digits / Alphabets
def check_char_type(ch):
    if len(ch) != 1:
        raise ValueError("Enter one character")
    if '0' <= ch <= '9':
        return "Digit"
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        return "Alphabet"
    return "Special Character"


# 60. Uppercase / Lowercase without built-in functions
def to_upper_manual(s):
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        else:
            result.append(ch)
    return "".join(result)

def to_lower_manual(s):
    result = []
    for ch in s:
        if 'A' <= ch <= 'Z':
            result.append(chr(ord(ch) + 32))
        else:
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    s = "programming"
    print(reverse_loop(s))
    print(reverse_join(s))
    print(reverse_two_pointer(s))
    print(reverse_slice(s))
    print(palindrome_two_pointer("madam"))
    print(char_frequency("banana"))
    print(are_anagrams_frequency("listen", "silent"))
    print(remove_duplicates("programming"))
    print(first_non_repeating("aabbcdde"))
    print(reverse_words("Python is easy"))
    print(is_rotation("abcd", "cdab"))
    print(compress_string("aaabbc"))
    print(to_upper_manual("Hello World"))
