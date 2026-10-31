# Write a program to swap two variables without temp variables

a = 5
b = 10
print("Before Swaping : a, b",a,b)
a,b = b,a
print("After Swaping : a, b",a,b)


# another way
a = 5
b = 10
a = a+b
b = a-b
a = a-b
print(a,b)