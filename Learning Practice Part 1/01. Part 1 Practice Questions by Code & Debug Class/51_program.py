# Create a list of 6 hypothetical students marks using built in functions print the highest mark, lowest mark, total sum of marks, and average mark format the average to two decimal points

marks = [75, 80, 86, 68, 76, 90]
print(max(marks))
print(min(marks))
print(sum(marks))
print(f"{sum(marks) / len(marks) :.2f}")


num = 12.34567
print(format(num, ".2f"))

num = 12.34567
print(round(num, 2))
# But round() returns a number, while formatting produces a string

