"""
PART 6 — Lists (61-70)
"""


# 61. Largest Element
def largest(arr):
    if not arr:
        raise ValueError("Empty list")
    maximum = arr[0]
    for x in arr[1:]:
        if x > maximum:
            maximum = x
    return maximum

def largest_builtin(arr):
    return max(arr)


# 62. Second Largest
def second_largest_two_pass(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        raise ValueError("Need at least two distinct values")
    return sorted(unique)[-2]

def second_largest_one_pass(arr):
    first = second = float("-inf")
    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    if second == float("-inf"):
        raise ValueError("Need at least two distinct values")
    return second

# Interview: one-pass solution is O(n) time and O(1) extra space.


# 63. Smallest Element
def smallest(arr):
    if not arr:
        raise ValueError("Empty list")
    minimum = arr[0]
    for x in arr[1:]:
        if x < minimum:
            minimum = x
    return minimum


# 64. Second Smallest
def second_smallest_one_pass(arr):
    first = second = float("inf")
    for x in arr:
        if x < first:
            second = first
            first = x
        elif first < x < second:
            second = x
    if second == float("inf"):
        raise ValueError("Need at least two distinct values")
    return second


# 65. Remove Duplicates
def remove_duplicates_set(arr):
    return list(set(arr))  # order is not guaranteed

def remove_duplicates_order(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# 66. Merge Lists
def merge_lists(a, b):
    return a + b

def merge_lists_manual(a, b):
    result = []
    for x in a:
        result.append(x)
    for x in b:
        result.append(x)
    return result

# If lists are sorted, sorted merge is a separate DSA problem.


# 67. Rotate List
def rotate_right_slice(arr, k):
    if not arr:
        return arr
    k %= len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]

def rotate_left_slice(arr, k):
    if not arr:
        return arr
    k %= len(arr)
    return arr[k:] + arr[:k]

def rotate_right_in_place(arr, k):
    # Reversal algorithm: O(n) time, O(1) extra space.
    n = len(arr)
    if n == 0:
        return
    k %= n

    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)


# 68. Frequency of Elements
def frequency_elements(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq


# 69. Most Frequent Element
def most_frequent(arr):
    if not arr:
        return None
    freq = frequency_elements(arr)
    best = arr[0]
    for x in arr:
        if freq[x] > freq[best]:
            best = x
    return best

def most_frequent_counter(arr):
    from collections import Counter
    return Counter(arr).most_common(1)[0][0] if arr else None


# 70. Flatten Nested List
def flatten_recursive(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result

def flatten_iterative(arr):
    result = []
    stack = list(reversed(arr))
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.append(item)
    return result

# Interview insight: iterative version explicitly uses a stack,
# connecting directly to DFS/tree traversal.


if __name__ == "__main__":
    a = [4, 2, 7, 2, 9, 4, 1]
    print(largest(a))
    print(second_largest_one_pass(a))
    print(smallest(a))
    print(second_smallest_one_pass(a))
    print(remove_duplicates_order(a))
    print(merge_lists([1,2], [3,4]))
    print(rotate_right_slice([1,2,3,4,5], 2))
    x = [1,2,3,4,5]
    rotate_right_in_place(x, 2)
    print(x)
    print(frequency_elements(a))
    print(most_frequent(a))
    print(flatten_recursive([1, [2, [3, 4]], 5]))
