# Write a lambda function that takes a number and returns its cube store it in a variable and call it
num = int(input("Enter a Number : "))
result = lambda num : num ** 3
print(result(num))