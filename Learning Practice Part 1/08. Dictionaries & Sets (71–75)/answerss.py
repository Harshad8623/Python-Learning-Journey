"""
PART 7 — Dictionaries & Sets (71-75)
"""


# 71. Word Frequency Counter
def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        # Basic cleanup for punctuation
        word = word.strip(".,!?;:'\"()[]{}")
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq

def word_frequency_counter(text):
    from collections import Counter
    words = []
    for word in text.lower().split():
        word = word.strip(".,!?;:'\"()[]{}")
        if word:
            words.append(word)
    return dict(Counter(words))


# 72. Merge Two Dictionaries
def merge_dicts(a, b):
    result = a.copy()
    result.update(b)
    return result

# If duplicate keys should have SUMMED values:
def merge_dicts_sum(a, b):
    result = a.copy()
    for key, value in b.items():
        result[key] = result.get(key, 0) + value
    return result

# Modern Python:
def merge_dicts_operator(a, b):
    return a | b


# 73. Common Keys
def common_keys(a, b):
    return set(a.keys()) & set(b.keys())

def common_keys_loop(a, b):
    result = []
    for key in a:
        if key in b:
            result.append(key)
    return result


# 74. Dictionary Sorting by Value
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def sort_dict_by_value_descending(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

# Interview: sorting dominates complexity -> O(n log n).


# 75. Remove Duplicates using Set
def remove_duplicates(arr):
    return list(set(arr))

# Preserve order:
def remove_duplicates_order(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# Interview questions:
# Q: Why is dictionary lookup usually O(1)?
# A: Hashing maps a key to a bucket/index on average.
#
# Q: Can a list be a dictionary key?
# A: No. Dictionary keys must be hashable; lists are mutable/unhashable.
#
# Q: Difference between set and dictionary?
# A: Set stores unique values; dict stores key-value pairs.
#
# Q: Does set preserve insertion order?
# A: Do not rely on set ordering. Python dictionaries preserve insertion order.


if __name__ == "__main__":
    text = "Python is easy and Python is powerful."
    print(word_frequency(text))
    print(merge_dicts({"a": 1}, {"b": 2}))
    print(merge_dicts_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}))
    print(common_keys({"a": 1, "b": 2}, {"b": 9, "c": 3}))
    print(sort_dict_by_value({"a": 5, "b": 2, "c": 8}))
    print(remove_duplicates_order([1, 2, 2, 3, 1]))
