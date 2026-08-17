name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
print(f"Hello {name},\nYour are {age} years old.")


num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
sum = num1 + num2
print(f"The sum of two numbers is : {sum}")


# Convert an integer to float and print
a = 10
print(f"Before conversion : {a} and its type is : {type(a)}")
a = float(a)
print(f"After conversion : {a} and its type is : {type(a)}")


# Convert a string '42' to integer and add 8
string_num = "42"
int_num = int(string_num)
result = int_num + 8
print(f"The result of adding 8 to the integer value of '{string_num}' is: {result}")


# Print the result of 17 // 5 and 17 % 5
print(f"The result of 17 // 5 is: {17 // 5}")
print(f"The result of 17 % 5 is: {17 % 5}")


# Print the ASCII value of any character
char = input("Enter a character: ")
if len(char) == 1:
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is: {ascii_value}")
else:
    print("Please enter a single character.")



# Concatenate first name and last name
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
full_name = f"{f_name} {l_name}"
print(f"Your full name is: {full_name}")    

# or
# full_name = f_name + " " + l_name


# Print 'Python' repeated 3 times
print("Python " * 3)


# Use comparison operators: print True/False for 10 > 5, 3 == 3, 7 != 7
print(f"Is 10 greater than 5? {10 > 5}")
print(f"Is 3 equal to 3? {3 == 3}")
print(f"Is 7 not equal to 7? {7 != 7}")


# Calculate simple interest: P=1000, R=5, T=2
P = 1000
R = 5
T = 2
SI = (P * R * T) / 100
print(f"Simple Interest: {SI}")