# Take a person's age as input and check if they are eligible to vote (18 years or older) and they have valid ID (Yes or No). If they are eligible to vote and have a valid ID print "You are eligible to vote." If they are eligible to vote but do not have a valid ID print "You are eligible to vote but you need a valid ID." If they are not eligible to vote print "You are not eligible to vote."
age = int(input("Enter your age: "))
if age >= 18:
    valid_id = input("Do you have a valid ID? (Yes/No): ")
    if valid_id.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("You are eligible to vote but you need a valid ID.")
else:
    print("You are not eligible to vote.")