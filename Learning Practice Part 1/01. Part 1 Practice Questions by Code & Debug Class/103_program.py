# Take a username as input. Strip any spaces from both sides and check if the cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid".


username = input("Enter username: ")

username = username.strip()

if username and username[0].isalpha():
    print("Valid")
else:
    print("Invalid")