# Take the users age as input and check if they are eligible to vote (18 years or older). and whether they are senior citizen (60 years or older).

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

if age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not a senior citizen.")