# Write a lambda function that takes a number and returns "Positive" or "Negative"
result = lambda num : "Positive" if num > 0 else "Negative"
check_num = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")

print(result(10))
print(result(0))
print(result(-7))
print(check_num(10))
print(check_num(0))
print(check_num(-7))