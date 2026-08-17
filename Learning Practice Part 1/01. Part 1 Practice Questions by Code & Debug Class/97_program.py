# Take an email as input. Validate that it contains exactly one @ and at least one .. Print "Valid" or "Invalid".

email = input("Enter your Email : ")

if email.count("@") == 1 and "." in email:
    print("Valid")
else:
    print("Invalid")