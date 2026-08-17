# Given a list of numbers (which may contain duplicates), write a Python script that takes an integer as input from the user and removes all occurrences of that integer from the list.

my_list = [10, 20, 10, 30, 20, 10, 40]
new_list = my_list[::] # if we use new_list = my_list then we do not get answer
num = int(input("Enter a Number : "))
for i in my_list:
    if i == num:
        new_list.remove(i)
print(my_list)
print(new_list)


# Another Solution
my_list = [10, 20, 10, 30, 20, 10, 40]
num = int(input("Enter a Number : "))
new_list = []
for i in my_list:
    if i != num:
        new_list.append(i)
print(my_list)
print(new_list)