# Take a phone number as input in the format +91-98765-43210. Remove all dashes and the country code. Print the cleaned 10-digit number.

phone = input("Enter phone number: ")

phone = phone.replace("-", "")
phone = phone.replace("+91", "")

print(phone)