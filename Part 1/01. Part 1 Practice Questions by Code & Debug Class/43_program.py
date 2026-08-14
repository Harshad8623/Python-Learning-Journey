# write a function called absolute_value that takes a number and returns its absolute value without using the built in abs() function
def absolute_value(num):
    if num == 0:
        return 0
    elif num > 0:
        return num
    else:
        return num * -1
print(absolute_value(12))
print(absolute_value(0))
print(absolute_value(-18))
print(absolute_value(7))