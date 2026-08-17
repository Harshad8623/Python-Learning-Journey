# Take a string as input. Check if it is a valid Indian PAN card number. Format: 5 uppercase letters + 4 digits + 1 uppercase letter (Total 10 characters). Example: ABCDE1234F.


pan = input("Enter PAN number: ")

if (
    len(pan) == 10
    and pan[:5].isalpha()
    and pan[:5].isupper()
    and pan[5:9].isdigit()
    and pan[9].isalpha()
    and pan[9].isupper()
):
    print("Valid")
else:
    print("Invalid")