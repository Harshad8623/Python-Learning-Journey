# Write a function get_stats(nums) that takes a tuple of numbers and returns a tuple containing the sum, average, minimum, and maximum. Unpack the returned tuple and print each value.

def get_stats(nums):
    return sum(nums), f"{sum(nums) / len(nums):.2f}", min(nums), max(nums)

total, avg, minimum, maximum = get_stats((2, 3, 1, 6, 9, 7))
print(total)
print(float(avg))
print(minimum)
print(maximum)

# Another Better Version
def get_stats(nums):
    total = sum(nums)
    average = round(total / len(nums), 2)
    return total, average, min(nums), max(nums)

total, avg, minimum, maximum = get_stats((2, 3, 1, 6, 9, 7))

print(total)
print(avg)
print(minimum)
print(maximum)